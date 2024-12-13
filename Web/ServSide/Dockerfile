FROM python:3.8.10-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN useradd -m ctf 

WORKDIR /app
COPY src/ /app
RUN chown -R ctf:ctf /app \
    && python3 -m pip install --no-cache-dir -r requirements.txt

USER ctf

CMD ["python3", "main.py"]