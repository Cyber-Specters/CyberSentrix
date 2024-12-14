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
    pub port: u16
}
