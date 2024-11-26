FROM python:3.11-slim-bullseye

WORKDIR /app

COPY ./app /app

# Install system dependencies, including supervisord, Python packages, and Playwright + install the dependencies dari playwright
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    bash \
    libmagic-dev \
    libjpeg-dev \
    fonts-dejavu \
    supervisor \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir playwright \
    && playwright install firefox \
    && playwright install-deps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY supervisord.conf /etc/supervisord.conf

EXPOSE 1811

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
