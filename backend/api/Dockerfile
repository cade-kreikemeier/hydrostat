FROM python:3.11-slim

WORKDIR /app

COPY ./api/requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir 

COPY ../.env .
COPY ../db/models.py .
COPY ./api/app/ .
