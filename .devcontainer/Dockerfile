FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    cargo \
    curl \
    git \
    golang-go \
    nano \
    nodejs \
    npm \
    rustc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY requirements.txt /workspace/
RUN pip install --no-cache-dir -r requirements.txt
