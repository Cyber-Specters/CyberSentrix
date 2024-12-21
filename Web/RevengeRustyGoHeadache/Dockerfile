
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
    libssl-dev

ENV NVM_DIR=/root/.nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash && \
    . "$NVM_DIR/nvm.sh" && \
    nvm install --lts && \
    nvm use --lts && \
    nvm alias default lts/* && \
    echo "export NVM_DIR=$NVM_DIR" >> /root/.bashrc && \
    echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"' >> /root/.bashrc && \
    echo '[ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"' >> /root/.bashrc

RUN . "$NVM_DIR/nvm.sh" && npm install pm2 -g

ADD supervisord.conf /etc/supervisor/conf.d/

WORKDIR /browser

COPY /browser/ .
RUN . "$NVM_DIR/nvm.sh" && npm install
RUN . "$NVM_DIR/nvm.sh" && pm2 start server.js

WORKDIR /bot

COPY /bot/.env /bot/
# COPY /bot/target/x86_64-unknown-linux-gnu/release/bot /bot/
COPY --from=builder /bot/target/x86_64-unknown-linux-gnu/release/bot /bot/

RUN chmod +x bot

COPY flag.txt /

CMD ["/bot/bot"]
