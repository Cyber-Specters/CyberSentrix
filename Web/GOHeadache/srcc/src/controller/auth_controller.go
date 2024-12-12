package controller

import (
	"app/src/model"
	"app/src/response"
	"app/src/service"
	"app/src/validation"

	"github.com/gofiber/fiber/v2"
)

type AuthController struct {
	AuthService  service.AuthService
	UserService  service.UserService
	TokenService service.TokenService
}

func NewAuthController(
	authService service.AuthService, userService service.UserService,
	tokenService service.TokenService,
) *AuthController {
	return &AuthController{
		AuthService:  authService,
		UserService:  userService,
		TokenService: tokenService,
	}
}

func (a *AuthController) Register(c *fiber.Ctx) error {
	req := new(validation.Register)

	if err := c.BodyParser(req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	user, err := a.AuthService.Register(c, req)
	if err != nil {
		return err
	}

	tokens, err := a.TokenService.GenerateAuthTokens(c, user)
	if err != nil {
		return err
	}

	return c.Status(fiber.StatusCreated).
		JSON(response.SuccessWithTokens{
			Code:    fiber.StatusCreated,
			Status:  "success",
			Message: "Register successfully",
			User:    *user,
			Tokens:  *tokens,
		})
}

func (a *AuthController) Login(c *fiber.Ctx) error {
	req := new(validation.Login)

	if err := c.BodyParser(req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	user, err := a.AuthService.Login(c, req)
	if err != nil {
		return err
	}

	tokens, err := a.TokenService.GenerateAuthTokens(c, user)
	if err != nil {
		return err
	}

	return c.Status(fiber.StatusOK).
		JSON(response.SuccessWithTokens{
			Code:    fiber.StatusOK,
			Status:  "success",
			Message: "Login successfully",
			User:    *user,
			Tokens:  *tokens,
		})
}

func (a *AuthController) Logout(c *fiber.Ctx) error {
	req := new(validation.Logout)

	if err := c.BodyParser(req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	if err := a.AuthService.Logout(c, req); err != nil {
		return err
	}

	return c.Status(fiber.StatusOK).
		JSON(response.Common{
			Code:    fiber.StatusOK,
			Status:  "success",
			Message: "Logout successfully",
		})
}

func (a *AuthController) VerifyEmail(c *fiber.Ctx) error {

	req := new(validation.VerifyEmail)
	if err := c.BodyParser(req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}
	user, _ := c.Locals("user").(*model.User)

	if err := a.AuthService.VerifyEmail(c, user, req); err != nil {
		return err
	}

	return c.Status(fiber.StatusOK).
		JSON(response.Common{
			Code:    fiber.StatusOK,
			Status:  "success",
			Message: "Verified email successfully",
		})
}

func (a *AuthController) RefreshTokens(c *fiber.Ctx) error {
	req := new(validation.RefreshToken)

	if err := c.BodyParser(req); err != nil {
		return fiber.NewError(fiber.StatusBadRequest, "Invalid request body")
	}

	tokens, err := a.AuthService.RefreshAuth(c, req)
	if err != nil {
		return err
	}

	return c.Status(fiber.StatusOK).
		JSON(response.RefreshToken{
			Code:   fiber.StatusOK,
			Status: "success",
			Tokens: *tokens,
		})
}
