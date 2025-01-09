
FROM rust:slim AS builder

RUN apt-get update -y && \
  apt-get install -y pkg-config make g++ libssl-dev && \
  rustup target add x86_64-unknown-linux-gnu

WORKDIR /bot

COPY /bot/ /bot

RUN cargo build --release --target x86_64-unknown-linux-gnu

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get install -y \
    build-essential \
    curl \
    supervisor \
    libssl-dev \
    nginx \
    unzip
    # chromium-browser

# Install required dependencies and Google Chrome with chromedriver version 121.0.6167.85
RUN apt-get install -y \
        libasound2 \
        libatk-bridge2.0-0 \
        libgbm-dev \
        libgtk-4-1 \
        libnss3 \
        xdg-utils \
        wget && \
    wget -q -O chrome-linux64.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/linux64/chrome-linux64.zip && \
    unzip chrome-linux64.zip && \
    rm chrome-linux64.zip && \
    mv chrome-linux64 /opt/chrome/ && \
    ln -s /opt/chrome/chrome /usr/local/bin/ && \
    wget -q -O chromedriver-linux64.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/linux64/chromedriver-linux64.zip && \
    unzip -j chromedriver-linux64.zip chromedriver-linux64/chromedriver && \
    rm chromedriver-linux64.zip && \
    mv chromedriver /usr/local/bin/

# RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
# RUN rm google-chrome-stable_current_amd64.deb 


# RUN CHROMEDRIVER_VERSION=$(google-chrome --product-version) && \
#     wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/$CHROMEDRIVER_VERSION/linux64/chromedriver-linux64.zip && \
#     unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
#     mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
#     rm /tmp/chromedriver.zip


ENV DISPLAY=:99

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - 

RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y nodejs         

# CONFIGURING NVM
# ENV NVM_DIR=/root/.nvm
# ENV NVM_VERSION v0.40.1
# ENV NODE_VERSION=v20.18.0

# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# ENV NODE_PATH $NVM_DIR/$NODE_VERSION/lib/node_modules
# ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# RUN echo "source $NVM_DIR/nvm.sh && \
#     nvm install $NODE_VERSION && \
#     nvm alias default $NODE_VERSION && \
#     nvm use default" | bash
# -----------------------

RUN npm install pm2 -g

ADD supervisord.conf /etc/supervisor/conf.d/

ADD nginx.conf /etc/nginx/nginx.conf

WORKDIR /browser

COPY /browser/ .
RUN npm install

WORKDIR /bot

COPY /bot/.env /bot/

COPY --from=builder /bot/target/x86_64-unknown-linux-gnu/release/bot /bot/

RUN chmod +x bot

COPY flag.txt /

CMD ["/usr/bin/supervisord"]