package utils

import (
	"errors"
	"strings"

	"github.com/golang-jwt/jwt/v5"
)

var blacklist = map[string]string{
	"[":        "Blocked string in the address",
	"127.":     "Blocked IPv4 address",
	"#":        "Blocked string in the address",
	"?":        "Blocked string in the address",
	"&":        "Blocked string in the address",
	"::":       "Blocked string in the address",
	"192.168.": "Blocked private IPv4 address",
	"10.":      "Blocked private IPv4 range",
	"172.16.":  "Blocked private IPv4 range",
}

var BadWords = []string{
	"fuck", "shit", "bitch", "asshole", "dick", "pussy", "cock", "bastard", "slut",
	"whore", "cunt", "douchebag", "motherfucker", "rape", "incest", "nude", "porn", "fuckhead",
	"retard", "stupid", "idiot", "cockroach", "bimbo", "twat", "ass", "dickhead", "prick",
	"cum", "jizz", "tits", "boobs", "sperm", "vagina", "testicles", "balls", "fag", "flag", "freak", "bastard",
	"chink", "gook", "spic", "nigger", "kike", "cracker", "gypsy", "wetback", "paki", "cholo",
	"honky", "sandnigger", "slut", "prostitute", "escort", "hooker", "tranny", "transvestite",
	"hermaphrodite", "bestiality", "zoophilia", "pedophile", "molester", "child porn", "rape",
	"kill", "die", "suicide", "terrorist", "bomb", "weapon", "gun", "knife", "knife fight",
	"gore", "murder", "massacre", "shooting", "behead", "execution", "butcher", "slaughter", "torture",
}

var allowlist = map[string]string{
	".com": "Allowed commercial domain",
	".net": "Allowed network domain",
	".org": "Allowed organization domain",
	".edu": "Allowed educational domain",
	".gov": "Allowed government domain",
	".us":  "Allowed US domain",
	".id":  "Allowed Indonesian domain",
	".biz": "Allowed business domain",
	".io":  "Allowed tech startup domain",
}

func VerifyToken(tokenStr, secret, tokenType string) (string, error) {
	token, err := jwt.Parse(tokenStr, func(_ *jwt.Token) (interface{}, error) {
		return []byte(secret), nil
	})

	if err != nil || !token.Valid {
		return "", err
	}

	claims, ok := token.Claims.(jwt.MapClaims)
	if !ok {
		return "", errors.New("invalid token claims")
	}

	jwtType, ok := claims["type"].(string)
	if !ok || jwtType != tokenType {
		return "", errors.New("invalid token type")
	}

	userID, ok := claims["sub"].(string)
	if !ok {
		return "", errors.New("invalid token sub")
	}

	return userID, nil
}

func IsBlacklisted(input string) (bool, string) {
	if !strings.HasPrefix("https://", input) || !strings.HasPrefix("http://", input) {
		return true, "Blocked URL, use a valid scheme!"
	}
	for prefix, message := range blacklist {
		if strings.Contains(input, prefix) {
			return true, message
		}
	}
	return false, ""
}

func IsAllowlisted(input string) (bool, string) {
	for suffix, message := range allowlist {
		if strings.HasSuffix(input, suffix) {
			return true, message
		}
	}
	domain := strings.Split(input, ".")
	return false, domain[len(domain)-1]
}
