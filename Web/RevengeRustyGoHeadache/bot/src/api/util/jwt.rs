use crate::config::{self};
use clap::Parser;
use jsonwebtoken::{encode, EncodingKey, Header};
use once_cell::sync::Lazy;
use regex::Regex;
use serde::{Deserialize, Serialize};
use uuid::Uuid;
use chrono::Duration;

static SECRET: Lazy<String> = Lazy::new(|| {
    let mut secret_key = config::ApiConfig::parse().jwt_secret_key;
    let re = Regex::new(r"\[([Uu][Uu][Ii][Dd])\]").unwrap();
    secret_key = re
        .replace_all(&secret_key, Uuid::new_v4().simple().to_string())
        .to_string();
    secret_key
});

#[derive(Debug, Deserialize, Serialize)]
pub struct Claims {
    pub id: Uuid,
    pub ip: String,
    pub exp: usize,
}

impl Claims {
    pub fn new(user_id: Uuid, ip: String) -> Self {
        let exp = (chrono::Utc::now() + Duration::minutes(config::ApiConfig::parse().jwt_expired as i64))
            .timestamp() as usize;

        Claims { id: user_id, ip, exp }
    }

    pub fn generate_token(&self) -> String {
        let secret = SECRET.clone();
        encode(
            &Header::default(),
            self,
            &EncodingKey::from_secret(secret.as_bytes()),
        )
        .expect("Failed to generate token")
    }
}

pub async fn get_secret() -> String {
    SECRET.clone()
}
