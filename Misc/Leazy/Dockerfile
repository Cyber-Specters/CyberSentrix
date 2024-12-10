FROM ubuntu:22.04

# auto y pada pertanyaan
ENV DEBIAN_FRONTEND=noninteractive

ENV PORT=3000
ENV FLAG=SENTRIX{BotClientSid3ReqForgery}
ENV AUTHORIZED_IP=47.245.121.0

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


RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY bot.js .

EXPOSE 3000

CMD ["node", "bot.js"]