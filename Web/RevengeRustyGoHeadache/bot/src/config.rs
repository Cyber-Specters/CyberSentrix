use clap::Parser;

#[derive(clap::ValueEnum, Clone, Debug, Copy)]
pub enum CargoEnv {
    Development,
    Production,
}

#[derive(clap::Parser)]
pub struct ApiConfig {
    #[clap(long, env, value_enum)]
    pub cargo_env: CargoEnv,
    #[clap(long, env, default_value = "6969")]
    pub bot_port: u16,
    #[clap(long, env, default_value = "3000")]
    pub port: u16,
    #[clap(long, env)]
    pub admin_email:String,
    #[clap(long, env)]
    pub jwt_secret_key:String,
    #[clap(long, env, default_value = "3000")]
    pub jwt_expired: i64,
    #[clap(long, env, default_value = "./database.db")]
    pub database_file: String,
    #[clap(long, env)]
    pub run_migrations: bool
}

impl ApiConfig {
    pub fn get_cfg() -> Self {
        ApiConfig::parse()
    }
}
