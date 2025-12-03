# Zeabur-ready Dockerfile

FROM python:3.10-slim

WORKDIR /app

# Copy backend
COPY app/ ./app/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app/main.py"]
