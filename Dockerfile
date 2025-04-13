
FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn requests

# Expor as portas que as APIs irão usar
EXPOSE 8000
EXPOSE 8001
