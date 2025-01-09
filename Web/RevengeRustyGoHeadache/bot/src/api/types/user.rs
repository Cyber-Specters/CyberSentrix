
use serde::{Deserialize, Serialize};
use validator::Validate;
use uuid::Uuid;


// id         uuid DEFAULT uuid_generate_v4 (),
// name       varchar     not null default '',
// email      varchar     not null default '',
// password   varchar     not null default '',
// created_at timestamptz not null default current_timestamp,
// updated_at timestamptz not null default current_timestamp


#[derive(Clone, Debug, Serialize, Deserialize, Validate)]
pub struct RegisterRequest {
    #[validate(length(min = 3, max = 40))]
    pub name: String,
    #[validate(email)]
    pub email: String,
    pub password: String,
}


#[derive(Clone, Debug, Serialize, Deserialize, Validate)]
pub struct LoginRequest {
    #[validate(email)]
    pub email: String,
    pub password: String,
}

#[derive(Clone, Debug, Serialize, Deserialize, Validate)]
pub struct AdminReq {
    pub status_sc: String,

}

#[derive(Serialize, Deserialize, Default, Debug)]
pub struct User {
    #[serde(skip_serializing, skip_deserializing)]
    pub id: Uuid,
    pub name: String,
    pub email: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub access_token: Option<String>,
}



impl From<(crate::entity::user::Model, String)> for User {
    fn from((user, token): (crate::entity::user::Model, String)) -> Self {
        Self {
            id: user.id,
            name: user.name,
            email: user.email,
            access_token: Some(token), 
        }
    }
}


#[derive(Serialize, Deserialize, Default, Debug)]
pub struct AuthResponse {
    pub user: User,
}
