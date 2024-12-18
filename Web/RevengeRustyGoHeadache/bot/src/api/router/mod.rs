use axum::{middleware::from_fn, routing::*};

use crate::api::middleware;

mod auth;
mod admin;

pub async fn health() -> &'static str {
    "🚀🚀🚀 Server Running"
}

pub fn app() -> Router {
    Router::new()
        .nest("/auth", auth::Auth::app())
        .nest("/admin", admin::Admin::app())
        .route("/health", get(health))
        .layer(from_fn(middleware::auth::jwt))

        // .layer(from_fn(middleware::auth::jwt))       

}