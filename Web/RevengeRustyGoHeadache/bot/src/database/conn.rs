use anyhow::{Ok, Result};
use std::time::Duration;
use once_cell::sync::OnceCell;
use tracing::info;
use sea_orm::{Database,ConnectOptions, DatabaseConnection};

use crate::database::migration::migrate;


static DB_CONNECTION: OnceCell<DatabaseConnection> = OnceCell::new();


pub struct DatabaseHeadache;

impl DatabaseHeadache {
    pub async fn connect(connection_string: &str, run_migrations: bool) -> Result<()>  {
        info!("Database connection url: {}", connection_string);
        let mut opt = ConnectOptions::new(connection_string);
        opt.max_connections(100)
            .min_connections(5)
            .connect_timeout(Duration::from_secs(8))
            .acquire_timeout(Duration::from_secs(8))
            .idle_timeout(Duration::from_secs(8))
            .max_lifetime(Duration::from_secs(8))
            .sqlx_logging(false)
            .set_schema_search_path("public");
        let db: DatabaseConnection = Database::connect(opt).await.unwrap();      
   
        DB_CONNECTION
            .set(db.clone())
            .map_err(|_| anyhow::anyhow!("Database connection has already been initialized"))?;


        if run_migrations {
            info!("migrations enabled, running...");
            migrate(&Self::get_db()).await;
            // migration::migrate(&get_db()).await;

        }

        Ok(())
    }
    pub fn get_db() -> DatabaseConnection {
        return DB_CONNECTION.get().ok_or_else(|| anyhow::anyhow!("Database connection is not initialized")).unwrap().clone();
    }
}