FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/main.py ./

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000", "--proxy-headers"]
