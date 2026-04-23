FROM python:3.12.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip wheel --no-cache-dir -r requirements.txt

COPY .src .src
COPY .result .result
COPY .img .img
COPY hand_landmarker.task hand_landmarker.task

CMD ["python", "main.py"]