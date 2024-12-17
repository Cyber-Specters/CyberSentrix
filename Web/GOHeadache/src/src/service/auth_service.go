package service

import (
	"app/src/config"
	"app/src/model"
	"app/src/response"
	"app/src/utils"
	"app/src/validation"
	"errors"
	"fmt"
	"net"
	"strings"

	"github.com/go-playground/validator/v10"
	"github.com/gofiber/fiber/v2"
	"github.com/sirupsen/logrus"
	"gorm.io/gorm"
)

type AuthService interface {
	Register(c *fiber.Ctx, req *validation.Register) (*model.User, error)
	Login(c *fiber.Ctx, req *validation.Login) (*model.User, error)
	Logout(c *fiber.Ctx, req *validation.Logout) error
	RefreshAuth(c *fiber.Ctx, req *validation.RefreshToken) (*response.Tokens, error)
	VerifyEmail(c *fiber.Ctx, user *model.User, req *validation.VerifyEmail) error
}

type authService struct {
	Log          *logrus.Logger
	DB           *gorm.DB
	Validate     *validator.Validate
	UserService  UserService
	TokenService TokenService
}

func NewAuthService(
	db *gorm.DB, validate *validator.Validate, userService UserService, tokenService TokenService,
) AuthService {
	return &authService{
		Log:          utils.Log,
		DB:           db,
		Validate:     validate,
		UserService:  userService,
		TokenService: tokenService,
	}
}

func (s *authService) VerifyEmail(c *fiber.Ctx, user *model.User, req *validation.VerifyEmail) error {
	if err := s.Validate.Struct(req); err != nil {
		return err
	}
	if blacklisted, msg := utils.IsBlacklisted(req.Refferal); blacklisted {
		return fiber.NewError(fiber.StatusUnauthorized, msg)
	}
	if allowed, domain := utils.IsAllowlisted(req.Refferal); !allowed {
		return fiber.NewError(fiber.StatusUnauthorized, fmt.Sprintf("Unauthorized domain tld %s", domain))
	}
	addrs, err := net.LookupHost(req.Refferal)
	if err != nil {
		return err
	}

	if addrs[0] != c.Context().LocalIP().String() {
		s.Log.Errorf("Not from local %s, but from %s", c.Context().LocalIP().String(), addrs[0])
		return fiber.NewError(fiber.StatusUnauthorized, fmt.Sprintf("Unauthorized Refferal, Not from local %s, but from %s", c.Context().LocalIP().String(), addrs[0]))
	}
	updateUser := &model.User{
		VerifiedEmail: true,
	}
	result := s.DB.WithContext(c.Context()).Where("id = ?", user.ID).Updates(updateUser)
	if errors.Is(result.Error, gorm.ErrDuplicatedKey) {
		return fiber.NewError(fiber.StatusConflict, "Email is already in use")
	}

	if result.RowsAffected == 0 {
		return fiber.NewError(fiber.StatusNotFound, "User not found")
	}
	return nil
}
func (s *authService) Register(c *fiber.Ctx, req *validation.Register) (*model.User, error) {
	if err := s.Validate.Struct(req); err != nil {
		return nil, err
	}

	hashedPassword, err := utils.HashPassword(req.Password)
	if err != nil {
		s.Log.Errorf("Failed hash password: %+v", err)
		return nil, err
	}

	user := &model.User{
		Name:     req.Name,
		Email:    req.Email,
		Password: hashedPassword,
	}

	result := s.DB.WithContext(c.Context()).Create(user)
	if errors.Is(result.Error, gorm.ErrDuplicatedKey) {
		return nil, fiber.NewError(fiber.StatusConflict, "Email already taken")
	}

	if result.Error != nil {
		s.Log.Errorf("Failed create user: %+v", result.Error)
	}

	return user, result.Error
}

func (s *authService) Login(c *fiber.Ctx, req *validation.Login) (*model.User, error) {
	if err := s.Validate.Struct(req); err != nil {
		return nil, err
	}

	user, err := s.UserService.GetUserByEmail(c, req.Email)
	if err != nil {
		return nil, fiber.NewError(fiber.StatusUnauthorized, "Invalid email or password")
	}
	if user.VerifiedEmail {
		if req.Token != "" {
			userID, err := utils.VerifyToken(req.Token, config.JWTSecret, config.TokenTypeAccess)
			if err != nil {
				return nil, fiber.NewError(fiber.StatusUnauthorized, "Please authenticate")
			}

			if userID == user.ID.String() {
				config.RoleRights[user.Role] = append(config.RoleRights[user.Role], user.Name)

			}
		}
		userName := strings.Fields(user.Name)
		if len(userName) > 1 {
			for i, _ := range userName {
				for _, badword := range utils.BadWords {
					if strings.Contains(userName[i], badword) {
						return nil, fiber.NewError(fiber.StatusUnauthorized, "Your username contains a badword, your account got banned")
					}
				}
			}
		} else {

			if strings.Contains(user.Name, "flag") {
				return nil, fiber.NewError(fiber.StatusUnauthorized, "Your username contains a badword, your account got banned")
			}
		}
		config.RoleRights[user.Role] = append(config.RoleRights[user.Role], userName...)
	} else { // NIH YANG JADI BIKIN UNINTENDEED > LUPA PASANG ELSE CIK
		return nil, fiber.NewError(fiber.StatusUnauthorized, "Please verify your email")
	}
	fmt.Printf("config.RoleRights: %+v\n", config.RoleRights)
	if !utils.CheckPasswordHash(req.Password, user.Password) {
		return nil, fiber.NewError(fiber.StatusUnauthorized, "Invalid email or password")
	}

	return user, nil
}

func (s *authService) Logout(c *fiber.Ctx, req *validation.Logout) error {
	if err := s.Validate.Struct(req); err != nil {
		return err
	}

	token, err := s.TokenService.GetTokenByUserID(c, req.RefreshToken)
	if err != nil {
		return fiber.NewError(fiber.StatusNotFound, "Token not found")
	}

	err = s.TokenService.DeleteToken(c, config.TokenTypeRefresh, token.UserID.String())

	return err
}

func (s *authService) RefreshAuth(c *fiber.Ctx, req *validation.RefreshToken) (*response.Tokens, error) {
	if err := s.Validate.Struct(req); err != nil {
		return nil, err
	}

	token, err := s.TokenService.GetTokenByUserID(c, req.RefreshToken)
	if err != nil {
		return nil, fiber.NewError(fiber.StatusUnauthorized, "Please authenticate")
	}

	user, err := s.UserService.GetUserByID(c, token.UserID.String())
	if err != nil {
		return nil, fiber.NewError(fiber.StatusUnauthorized, "Please authenticate")
	}

	newTokens, err := s.TokenService.GenerateAuthTokens(c, user)
	if err != nil {
		return nil, fiber.ErrInternalServerError
	}

	return newTokens, err
}
