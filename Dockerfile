FROM python:3.12.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgl1 \
    libgles2-mesa-dev \
    libglib2.0-0 \
    wget \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY hand_landmarker.task .

RUN mkdir -p img result

CMD ["python", "src/main.py"]