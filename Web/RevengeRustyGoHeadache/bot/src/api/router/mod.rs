use axum::{middleware::from_fn, routing::*};

use crate::{api::middleware, get_admin_id};

mod auth;
mod admin;

pub async fn health() -> String {
    let id = get_admin_id().await.unwrap().to_string();
    format!("🚀🚀🚀 Server Running and db also running, welcome back {}", id)
}

pub fn app() -> Router {
    Router::new()
        .nest("/auth", auth::Auth::app())
        .nest("/admin", admin::Admin::app())
        .route("/health", get(health))
        .layer(from_fn(middleware::auth::jwt))

}