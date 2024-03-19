FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./src /code/app
COPY ./.env /.env

CMD ["uvicorn", "app.main:app", "--host", "192.168.1.11", "--port", "8000", "--proxy-headers"]
