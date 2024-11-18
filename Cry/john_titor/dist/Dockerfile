# Gunakan image Python versi terbaru sebagai basis
FROM python:3.10-slim

# Set directory kerja di dalam container
WORKDIR /app

# Install dependencies termasuk socat dan netcat-openbsd
RUN apt-get update && \
    apt-get install -y netcat-openbsd socat && \
    pip install pycryptodome && \
    rm -rf /var/lib/apt/lists/*

# Salin file yang diperlukan ke dalam container
COPY main.py /app
COPY flag.txt /app

# Ekspos port 8000 di dalam container
EXPOSE 8000

# Jalankan Netcat sebagai listener dan hubungkan ke main.py dengan socat
CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"python /app/main.py"
