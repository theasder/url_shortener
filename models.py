from sqlalchemy import Table, Column, Integer, String, create_engine, MetaData
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import mapper

DATABASE = {
    'drivername': 'postgresql',
    'host': '0.0.0.0',
    'port': '5432',
    'username': 'auth',
    'password': 'auth',
    'database': 'auth_test'
}

engine = create_engine(URL(**DATABASE))
metadata = MetaData()

url_table = Table('URL', metadata,
    Column('hash', String, primary_key=True),
    Column('link', String)
)

logs_table = Table('Logs', metadata,
    Column('hash', String, primary_key=True),
    Column('milliseconds', Integer),
    Column('IP', String),
    Column('referrer', String)
)


class Log(object):
    def __init__(self, hash_, milliseconds, ip, referrer):
        self.hash = hash_
        self.milliseconds = milliseconds
        self.ip = ip
        self.referrer = referrer


class URL(object):
    def __init__(self, link, hash_):
        self.hash = hash_
        self.link = link


mapper(URL, url_table)
mapper(Log, logs_table)
