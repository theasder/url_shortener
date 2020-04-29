FROM python:alpine3.6

COPY . /var/www
WORKDIR /var/www

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "tests/test_url.py"]
CMD ["python3", "server.py"]

