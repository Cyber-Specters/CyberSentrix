use std::sync::Arc;
use clap::Parser;
// use fantoccini::ClientBuilder;
use dotenvy::dotenv;

mod config; 
mod api;   
mod log;

use config::ApiConfig;
use log::Logger;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    dotenv().ok();
    let config = Arc::new(ApiConfig::parse());
    let _guard = Logger::init(config.cargo_env);

    // for the chromedriver
    // api::Api::run(config.clone()).await?;
    // let client = ClientBuilder::native()
    //     .connect(&format!("http://localhost:{}", config.bot_port))
    //     .await
    //     .expect("Failed to connect");
    // client.goto("https://www.rust-lang.org/").await.expect("failed to open");
    // client.close().await.expect("failed to close");
    Ok(())
}
