FROM ubuntu:22.04

# auto y pada pertanyaan
ENV DEBIAN_FRONTEND=noninteractive

# Set environment variables
ENV PORT=3001
ENV FLAG=SENTRIX{BotClientSid3ReqForgery}
ENV AUTHORIZED_IP=47.245.121.0

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    g++ \
    make \
    python3 \
    python3-pip \
    pkg-config \
    libcairo2-dev \
    libjpeg-dev \
    libpango1.0-dev \
    libgif-dev \
    libpixman-1-dev \
    fontconfig \
    ttf-mscorefonts-installer \
    nginx \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory and copy application files
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY bot.js .

# Copy NGINX configuration file
COPY nginx.conf /etc/nginx/sites-enabled/nginx.conf

# Expose port for both Node.js and NGINX
EXPOSE 3000
EXPOSE 3001

# Start NGINX and Node.js app
CMD service nginx start && node bot.js