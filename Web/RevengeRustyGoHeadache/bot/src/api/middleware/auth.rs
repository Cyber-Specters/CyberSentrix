use std::net::SocketAddr;

use crate::{api::{types::{error::Error, traits::Ext}, util}, database};
use axum::{
    body::Body,
    extract::{ConnectInfo, Request},
    http::StatusCode,
    middleware::Next,
    response::{IntoResponse, Response},
    Json,
};
use jsonwebtoken::{decode, DecodingKey, Validation};
use sea_orm::EntityTrait;
use serde_json::json;
use tracing::debug;

pub async fn jwt(ConnectInfo(addr): ConnectInfo<SocketAddr>,mut req: Request<Body>, next: Next) -> Result<Response, Error> {
    let token = req
        .headers()
        .get("Authorization")
        .and_then(|header| header.to_str().ok())
        // .and_then(|header| header.strip_prefix("Bearer "))
        .unwrap_or("");

    let decoding_key: DecodingKey = DecodingKey::from_secret(util::jwt::get_secret().await.as_bytes());
    let validation = Validation::default();
    let result = decode::<util::jwt::Claims>(token, &decoding_key, &validation);

    let client_ip = addr.ip().to_owned().to_string();
    
    debug!("client_ip: {}", client_ip);

    if let Ok(token_data) = result {
        let result = crate::entity::user::Entity::find_by_id(token_data.claims.id)
            .one(&database::DatabaseHeadache::get_db())
            .await;

        if let Err(_err) = result {
            return Ok((
                StatusCode::INTERNAL_SERVER_ERROR,
                Json(json!({
                    "code": StatusCode::INTERNAL_SERVER_ERROR.as_u16(),
                    "msg": "internal_server_error"
                })),
            )
                .into_response());
        }

        let user = result.unwrap();

        if user.is_none() {
            return Err(Error::NotFound("User not found".to_string()));
        }

        let user = user.unwrap();

        // if user.group == Group::Banned {
        //     return Err(WebError::Forbidden(String::from("forbidden")));
        // }

        req.extensions_mut().insert(Ext {
            operator: Some(user.clone()),
            client_ip: client_ip,
        });
    } else {
        req.extensions_mut().insert(Ext {
            operator: None,
            client_ip: client_ip, // You may still want the client IP here
        });
    }

    return Ok(next.run(req).await);
}