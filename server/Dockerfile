
FROM python:latest

RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib

ADD server.py /server/
ADD README.md /server/
ADD migration.sql /server/
ADD requirements.txt /server/

WORKDIR /server/

RUN pip install --no-cache-dir -r requirements.txt
RUN python server.py

