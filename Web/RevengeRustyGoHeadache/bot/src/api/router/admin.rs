use std::vec;

use axum::{routing::post, Extension, Router};
use clap::Parser;
use fantoccini::{ClientBuilder, Locator};
use sea_orm::sea_query::Expr;
use sea_orm::{EntityTrait, QueryFilter};
use tracing::info;

use crate::api::types::user::AdminReq;
use crate::api::util::validate::ValidationExtractor;
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

    pub async fn submit(
        Extension(ext): Extension<Ext>,
        ValidationExtractor(mut req): ValidationExtractor<AdminReq>,
    ) -> AppResult<String> {
        let operator = ext.operator.ok_or(Error::Unauthorized)?;
        info!("operator: {:?}", operator);
        let user = crate::entity::user::Entity::find()
            .filter(Expr::expr(Expr::col(crate::entity::user::Column::Id)).eq(operator.id.clone()))
            .one(&crate::database::DatabaseHeadache::get_db())
            .await
            .map_err(|_| {
                Error::InternalServerErrorWithContext("Database query failed".to_string())
            })?
            .ok_or_else(|| Error::NotFound("User not found".to_string()))?;
        if user.email != config::ApiConfig::parse().admin_email {
            return Err(Error::AnyhowError(anyhow::anyhow!("Not an admin")));
        }
        let mut capabilities = ::serde_json::Map::new();
        let chrome_opts = ::serde_json::json!({ "args": ["--headless","--disable-web-security"] });
        capabilities.insert("goog:chromeOptions".to_string(), chrome_opts);

        let client: Result<fantoccini::Client, fantoccini::error::NewSessionError> =
            ClientBuilder::native()
                .capabilities(capabilities)
                .connect(&format!(
                    "http://localhost:{}",
                    config::ApiConfig::parse().bot_port
                ))
                .await;

        if client.is_err() {
            return Err(Error::AnyhowError(anyhow::anyhow!(
                "Failed to connect to bot"
            )));
        }

        let client = client.unwrap();
        let _ = client
            .goto("http://localhost:3001/healthcheck")
            .await
            .map_err(|_| Error::AnyhowError(anyhow::anyhow!("Failed to go")));
      
        let result = client
            .execute_async(&req.status_sc, vec![])
            .await
            .map_err(|e| {
                Error::AnyhowError(anyhow::anyhow!("Failed to extract because of : {}", e))
            })
            .unwrap();
        let _ = client
            .wait()
            .for_element(Locator::Css(
                r#"a.button-download[href="/learn/get-started"]"#,
            ))
            .await;
        client.close().await.map_err(|_| {
            Error::InternalServerErrorWithContext("Error closing the browser".to_string())
        })?;
        let convert_result = serde_json::to_string(&result)
            .map_err(|e| {
                Error::AnyhowError(anyhow::anyhow!("Failed to extract because of : {}", e))
            })
            .unwrap();
        Ok(convert_result)
    }
}
