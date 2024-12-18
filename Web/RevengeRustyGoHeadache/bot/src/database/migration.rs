use sea_orm::{ConnectionTrait, DbConn, EntityTrait, Schema, Statement};
use tracing::{error, info};

use crate::user::{self};

macro_rules! create_tables {
    ($db:expr, $($entity:expr),*) => {
        $(
            create_table($db, $entity).await;
        )*
    };
}

async fn create_table<E>(db: &DbConn, entity: E)
where
    E: EntityTrait,
{
    let builder = db.get_database_backend();
    let schema = Schema::new(builder);
    
    let table_create_statement = schema.create_table_from_entity(entity);

    
    let stmt: Statement = builder.build(&table_create_statement);
    match db.execute(stmt).await {
        Err(e) => error!("Error executing db: {}", e),
        Ok(_) => {
            info!(
                "successfully migrate the database!",
            );
        }
    }
}




pub async fn migrate(db: &DbConn) {
    create_tables!(
        db,
        user::Entity
    );
}