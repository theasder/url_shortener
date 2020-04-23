FROM python:latest

RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib

COPY server.py /server/
COPY README.md /server/
COPY migration.sql /server/
COPY requirements.txt /server/

WORKDIR /server/

RUN pip install --no-cache-dir -r requirements.txt
CMD python server.py

