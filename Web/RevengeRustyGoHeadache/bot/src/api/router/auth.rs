use axum::{routing::post, Extension, Router};
use tracing::info;

pub struct Auth;

impl Auth {
    pub fn app() -> Router {
        Router::new()
            // .route("/signup", post(Self::signup))
            // .route("/signin", post(Self::signin_user_endpoint))
            // .route("/signout", post(Self::signout_user_endpoint))
            // .route("/whoami", get(Self::get_current_user_endpoint))
            // .route("/refresh", get(Self::refresh_user_endpoint))
            // .route("/", put(Self::update_user_endpoint))
    }
    // to-do creating the signup with db using a file
    // pub async fn signup(
    //     Extension(services): Extension<Services>,
    //     ValidationExtractor(request): ValidationExtractor<SignUpUserDto>,
    // ) -> AppResult<Json<UserAuthenicationResponse>> {
    //     info!(
    //         "recieved request to create user {:?}/{:?}",
    //         request.email.as_ref().unwrap(),
    //         request.name.as_ref().unwrap()
    //     );

    //     let created_user = services.users.signup_user(request).await?;

    //     Ok(Json(UserAuthenicationResponse { user: created_user }))
    // }

}