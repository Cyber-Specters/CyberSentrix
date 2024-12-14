use axum::routing::*;

mod auth;


pub async fn health() -> &'static str {
    "🚀🚀🚀 Server Running"
}

pub fn app() -> Router {
    Router::new()
        .nest("/auth", auth::Auth::app())
        // .nest("/categories", CategoryController::app())
        .route("/health", get(health))
}