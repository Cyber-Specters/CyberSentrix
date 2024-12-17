use crate::user;

#[derive(Clone, Debug)]
pub struct Ext {
    pub operator: Option<user::Model>,
    pub client_ip: String,
}