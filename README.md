# Hand Tracking API

**API для обнаружения и отрисовки ключевых точек рук на изображениях**

---

## 📌 О проекте

`Hand Tracking API` предоставляет REST API для обнаружения рук на изображениях с помощью MediaPipe. Сервис принимает изображение, обрабатывает его с использованием модели `hand_landmarker.task`, определяет 21 ключевую точку на каждой руке и отрисовывает их вместе с соединениями. Результат сохраняется и возвращается пользователю.

Проект написан на **FastAPI** с использованием **MediaPipe** и **OpenCV**для компьютерного зрения и полностью контейнеризирован через Docker для удобного развертывания.

---

## 🚀 Возможности

- **Загрузка изображений** через API эндпоинт.
- **Обнаружение рук** с помощью предобученной модели MediaPipe.
- **Отрисовка 21 ключевой точки** на каждой найденной руке.
- **Отрисовка соединений между точками** для визуализации скелета руки.
- **Автоматическая загрузка модели** при первом запуске.
- **Поддержка форматов:** PNG, JPG, JPEG, BMP, TIFF.
- **Готов к развертыванию** с помощью Docker Compose.

---

## 🛠️ Технологии

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-FF7A00?style=for-the-badge&logo=google&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=uvicorn&logoColor=white)

---

## 🖥️ Запуск через Docker

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/imnokkip/Hand-Tracking
   cd Hand-Tracking
   ```

2. Запусти Docker:
    ```bash
    docker-compose up -d
    ```

3. Проверь, что контейнер запущен:
    ```bash
    docker-compose ps
    ```

4. Открой:
    В браузере http://127.0.0.1:8000/docs для доступа к Swagger-документации.

##📑 Планы по доработке

[]-заменить хранение файлов на сервере, на временное хранение в оперативке
[]-сделать возврат файла, а не количества рук
