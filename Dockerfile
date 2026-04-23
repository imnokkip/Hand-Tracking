FROM python:3.12.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt



COPY src ./src
COPY main.py .
COPY router.py .

RUN mkdir -p img result

CMD ["python", "main.py"]