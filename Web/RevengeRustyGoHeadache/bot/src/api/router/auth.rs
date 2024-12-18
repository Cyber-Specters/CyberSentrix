use argon2::{
    password_hash::{rand_core::OsRng, SaltString},
    Argon2, PasswordHash, PasswordHasher, PasswordVerifier,
};
use axum::{routing::post, Extension, Json, Router};
use sea_orm::{
    sea_query::{Expr, Func},
    ActiveModelTrait, Condition, EntityTrait, QueryFilter, Set,
};
use tracing::info;
use uuid::Uuid;

use crate::api::{
    types::{
        error::{AppResult, Error},
        traits::Ext,
        user::{AuthResponse, LoginRequest, RegisterRequest, User},
    },
    util::{jwt::Claims, validate::ValidationExtractor},
};

pub struct Auth;

impl Auth {
    pub fn app() -> Router {
        Router::new()
            .route("/signup", post(Self::signup))
            .route("/signin", post(Self::signin))
    }
    pub async fn signup(
        Extension(_ext): Extension<Ext>,
        ValidationExtractor(mut req): ValidationExtractor<RegisterRequest>,
    ) -> AppResult<Json<AuthResponse>> {
        req.email = req.email.to_lowercase();
        req.name = req.name.to_lowercase();

        info!(
            "Received request to create user {:?}/{:?}",
            req.email, req.name
        );

        let is_conflict = crate::entity::user::Entity::find()
            .filter(
                Condition::any()
                    .add(
                        Expr::expr(Func::lower(Expr::col(crate::entity::user::Column::Name)))
                            .eq(req.name.clone()),
                    )
                    .add(
                        Expr::expr(Func::lower(Expr::col(crate::entity::user::Column::Email)))
                            .eq(req.email.clone()),
                    ),
            )
            .one(&crate::database::DatabaseHeadache::get_db())
            .await
            .unwrap()
            .is_some();

        if is_conflict {
            return Err(Error::ObjectConflict("User already exists".to_string()));
        }
        let hashed_password = Argon2::default()
            .hash_password(req.password.as_bytes(), &SaltString::generate(&mut OsRng))
            .unwrap()
            .to_string();

        let created_user = crate::entity::user::ActiveModel {
            id: Set(Uuid::new_v4()),
            name: Set(req.name),
            email: Set(req.email),
            password: Set(hashed_password),
            ..Default::default()
        }
        .insert(&crate::database::DatabaseHeadache::get_db())
        .await
        .unwrap();

        info!(
            "Created user {:?}/{:?}",
            created_user.name, created_user.email
        );
        let response_user: User = (created_user, "a".to_string()).into();
        Ok(Json(AuthResponse {
            user: response_user,
        }))
    }

    pub async fn signin(
        Extension(ext): Extension<Ext>,
        ValidationExtractor(mut req): ValidationExtractor<LoginRequest>,
    ) -> AppResult<Json<AuthResponse>> {
        req.email = req.email.to_lowercase();

        let user = crate::entity::user::Entity::find()
            .filter(
                Expr::expr(Func::lower(Expr::col(crate::entity::user::Column::Email)))
                    .eq(req.email.clone()),
            )
            .one(&crate::database::DatabaseHeadache::get_db())
            .await
            .map_err(|_| {
                Error::InternalServerErrorWithContext("Database query failed".to_string())
            })?
            .ok_or_else(|| Error::NotFound("User not found".to_string()))?;

        let hashed_password = &user.password;
        Argon2::default()
            .verify_password(
                req.password.as_bytes(),
                &PasswordHash::new(hashed_password).map_err(|_| {
                    Error::InternalServerErrorWithContext("Invalid password hash".to_string())
                })?,
            )
            .map_err(|_| Error::InvalidLoginAttmpt)?;

        info!("User {:?} logged in", user.name);

        let claims = Claims::new(
            Uuid::parse_str(&user.name).unwrap_or_else(|_| user.id),
            ext.client_ip,
        );

        let response = AuthResponse {
            user: User {
                id: user.id,
                name: user.name,
                email: user.email,
                access_token: Some(claims.generate_token()),
            },
        };

        Ok(Json(response))
    }
}
