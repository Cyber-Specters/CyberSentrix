use std::sync::Arc;
use clap::Parser;
use dotenvy::dotenv;

mod config; 
pub mod api;   
pub mod database;
mod entity;
mod log;

use config::ApiConfig;
use log::Logger;
pub use database::*;
pub use entity::*;
use tracing::info;


#[tokio::main]
async fn main() -> anyhow::Result<()> {
    dotenv().ok();
    let config = Arc::new(ApiConfig::parse());
    let _guard = Logger::init(config.cargo_env);
    info!("environment loaded and configuration parsed, initializing Postgres connection and running migrations...");
    let _db = DatabaseHeadache::connect(&config.database_file, config.run_migrations)
        .await
        .expect("could not initialize the database connection pool");

    api::Api::run(config.clone()).await?;
    // let client = ClientBuilder::native()
    //     .connect(&format!("http://localhost:{}", config.bot_port))
    //     .await
    //     .expect("Failed to connect");
    // client.goto("https://www.rust-lang.org/").await.expect("failed to open");
    // client.close().await.expect("failed to close");
    Ok(())
}
