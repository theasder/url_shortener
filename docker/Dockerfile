FROM python:alpine3.6

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY . /var/www
WORKDIR /var/www

RUN pip install --no-cache-dir -r requirements.txt

RUN ["python3", "models.py"]
CMD ["python3", "server.py"]
