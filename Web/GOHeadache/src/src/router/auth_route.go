package router

import (
	"app/src/controller"
	m "app/src/middleware"
	"app/src/service"

	"github.com/gofiber/fiber/v2"
)

func AuthRoutes(
	v1 fiber.Router, a service.AuthService, u service.UserService,
	t service.TokenService,
) {
	authController := controller.NewAuthController(a, u, t)

	auth := v1.Group("/auth")

	auth.Post("/register", authController.Register)
	auth.Post("/login", authController.Login)
	auth.Post("/logout", authController.Logout)
	auth.Post("/verify-email", m.Auth(u), authController.VerifyEmail)
	auth.Post("/refresh-tokens", authController.RefreshTokens)
}
