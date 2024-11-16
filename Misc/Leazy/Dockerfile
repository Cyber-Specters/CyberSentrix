FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies, including curl
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
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Node.js (replace with your desired version)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy project files
COPY bot.js .

# Command to run the application
CMD ["node", "bot.js"]
