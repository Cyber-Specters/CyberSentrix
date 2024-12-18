use anyhow::{Ok, Result};
use argon2::{
    password_hash::{
        rand_core::{OsRng, RngCore},
        SaltString,
    },
    Argon2, PasswordHasher,
};
use clap::Parser;
use once_cell::sync::OnceCell;
use sea_orm::{ActiveModelTrait, ConnectOptions, Database, DatabaseConnection, Set};
use std::time::Duration;
use tracing::info;
use uuid::Uuid;

use crate::{config, database::migration::migrate, entity};

static DB_CONNECTION: OnceCell<DatabaseConnection> = OnceCell::new();

pub struct DatabaseHeadache;

impl DatabaseHeadache {
    pub async fn connect(connection_string: &str, run_migrations: bool) -> Result<()> {
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
            Self::init_admin()
                .await
                .is_err()
                .then(|| anyhow::anyhow!("admin credentials could not be initialized"));
        }

        Ok(())
    }
    pub fn get_db() -> DatabaseConnection {
        return DB_CONNECTION
            .get()
            .ok_or_else(|| anyhow::anyhow!("Database connection is not initialized"))
            .unwrap()
            .clone();
    }
    pub async fn init_admin() -> Result<()>{
        let rand_password = OsRng.next_u64();
        let hashed_password = Argon2::default()
            .hash_password(
                rand_password.to_string().as_bytes(),
                &SaltString::generate(&mut OsRng),
            )
            .unwrap()
            .to_string();
        let user = entity::user::ActiveModel {
            id: Set(Uuid::new_v4()),
            name: Set(String::from("admin")),
            email: Set(config::ApiConfig::parse().admin_email),
            password: Set(hashed_password),
            ..Default::default()
        }
        .insert(&Self::get_db())
        .await
        .unwrap();

        // let inserted_user = user.insert(&Self::get_db()).await.unwrap();
        info!(
            "admin credentials: {:?} {:?}",
            user.email,
            rand_password.to_string()
        );

        Ok(())
    }
}
