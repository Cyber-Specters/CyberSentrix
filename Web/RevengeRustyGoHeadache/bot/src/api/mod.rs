use std::{net::{Ipv4Addr, SocketAddr}, sync::Arc};
use crate::config::ApiConfig;
use anyhow::Context;
use axum::{routing::get, Router};
use tracing::{debug, info};

mod router;
pub mod types;
mod util;
mod middleware;
// mod services;

pub struct Api;

async fn hello_world() -> &'static str {
    "Hello world!"
}


impl Api {
    pub async fn run(config: Arc<ApiConfig>) -> anyhow::Result<()> {
        let addr = SocketAddr::from((Ipv4Addr::UNSPECIFIED, config.port));
        info!("server started http://{addr}");
        debug!("Running in environment: {:?}", config.cargo_env);
        let router = Router::new()
        .nest("/v1", router::app())
        .route("/", get(hello_world));
        let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
        axum::serve(listener, 
            router.into_make_service_with_connect_info::<SocketAddr>())
            .with_graceful_shutdown(Self::shutdown_signal())
            .await
            .context("error while starting API server")
            .unwrap();
        Ok(())
    }
    async fn shutdown_signal() {
        tokio::signal::ctrl_c()
            .await
            .expect("expect tokio signal ctrl-c");
        println!("signal shutdown");
    }
}