import os
import datetime

from sqlalchemy import Table, Column, Integer, String, DateTime, create_engine, MetaData
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import mapper


DATABASE = {
    'drivername': os.environ['DB_TYPE'],
    'host': os.environ['HOST'],
    'port': os.environ['IMAGE_PORT'],
    'username': os.environ['POSTGRES_USER'],
    'password': os.environ['POSTGRES_PASSWORD'],
    'database': os.environ['POSTGRES_DB']
}

engine = create_engine(URL(**DATABASE))
metadata = MetaData()

url_table = Table('URL', metadata,
    Column('hash', String(255), primary_key=True),
    Column('link', String(255))
)

logs_table = Table('Logs', metadata,
    Column('hash', String(255), primary_key=True),
    Column('time', DateTime),
    Column('IP', String(255)),
    Column('referrer', String(255))
)


class Log(object):
    def __init__(self, short_link, seconds, ip, referrer):
        self.hash = short_link
        self.time = datetime.datetime.fromtimestamp(seconds)
        self.ip = ip
        self.referrer = referrer


class URL(object):
    def __init__(self, link, short_link):
        self.hash = short_link
        self.link = link


mapper(URL, url_table)
mapper(Log, logs_table)
