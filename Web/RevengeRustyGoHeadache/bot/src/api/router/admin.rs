use axum::{routing::post, Extension, Router};
use clap::Parser;
use fantoccini::ClientBuilder;
use sea_orm::sea_query::Expr;
use sea_orm::{EntityTrait, QueryFilter};
use tracing::info;

use crate::config::{self};

use crate::api::types::{
    error::{AppResult, Error},
    traits::Ext,
};

pub struct Admin;

impl Admin {
    pub fn app() -> Router {
        Router::new().route("/submit", post(Self::submit))
    }

    pub async fn submit(Extension(ext): Extension<Ext>) -> AppResult<&'static str> {
        let operator = ext.operator.ok_or(Error::Unauthorized)?;

        info!("operator: {:?}", operator);
        let user = crate::entity::user::Entity::find()
            .filter(
                Expr::expr(Expr::col(crate::entity::user::Column::Id))
                    .eq(operator.id.clone()),
            )
            .one(&crate::database::DatabaseHeadache::get_db())
            .await
            .map_err(|_| {
                Error::InternalServerErrorWithContext("Database query failed".to_string())
            })?
            .ok_or_else(|| Error::NotFound("User not found".to_string()))?;
        if user.email != config::ApiConfig::parse().admin_email {
            return Err(Error::AnyhowError(anyhow::anyhow!("Not admin")));
        }
        // check chromdriver port 
        let client: Result<fantoccini::Client, fantoccini::error::NewSessionError> = ClientBuilder::native()
            .connect(&format!("http://localhost:{}", config::ApiConfig::parse().bot_port))
            .await;
            
        if client.is_err() {
            return Err(Error::AnyhowError(anyhow::anyhow!("Failed to connect to bot")));
        }

        let client = client.unwrap();
        client.goto("https://www.rust-lang.org/").await.expect("failed to open");
        // client.execute(script, args)
        client.close().await.expect("failed to close");
        Ok("Done")
    }
}
