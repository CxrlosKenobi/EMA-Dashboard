from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
import configparser

import sqlite3
import os

config = configparser.ConfigParser()
config.read('config.txt')
engine = create_engine(config.get('database', 'con'))

inp = input('\nAre you sure to delete data.db ? y/n: ')
if inp == 'n':
    exit()

os.system('rm -rf data.db && touch data.db')
conn = sqlite3.connect('data.db')
cur = conn.cursor()
print('\n[ ok ] Now connected to the database!')

cur.execute(
"""
CREATE TABLE data(
    date VARCHAR(15),
    time VARCHAR(15),
    pm25 VARCHAR(15),
    pm10 VARCHAR(15),
    PRIMARY KEY (time),
    UNIQUE (time)
);
"""
)

conn.commit()
cur.close()

print('[ ok ] Db has been sucesfully created!')

db = SQLAlchemy()

class Data(db.Model):
    date = db.Column(db.String(15), primary_key=True, unique=True) 
    time = db.Column(db.String(15))
    pm25 = db.Column(db.String(15))
    pm10 = db.Column(db.String(15))

Data_tbl = Table('data', Data.metadata)


def create_data_table():
    Data.metadata.create_all(engine)

def add_data(date, time, pm25, pm10):
    ins = Data_tbl.insert().values(
        date=date,
        time=time,
        pm25=pm25,
        pm10=pm10
    )
    conn = engine.connect()
    conn.execute(ins)
    conn.close()


## Rand 
inp = input('\nAre you sure to delete datarand.db ? y/n: ')
if inp == 'n':
    exit()

os.system('rm -rf datarand.db && touch datarand.db')
conn = sqlite3.connect('datarand.db')
cur = conn.cursor()
print('\n[ ok ] Now connected to the rand database!')

cur.execute(
"""
CREATE TABLE data (
    timestamp VARCHAR(15),
    timeinsec VARCHAR(15),
    pm25 VARCHAR(15),
    pm10 VARCHAR(15)
    PRIMARY KEY (timestamp),
    UNIQUE (timestamp)
);
"""
)
conn.commit()
cur.close()

print('[ ok ] Db (rand) has been sucesfully created!')

db = SQLAlchemy()

class Data(db.Model):
    date = db.Column(db.String(15), primary_key=True, unique=True) 
    time = db.Column(db.String(15))
    pm25 = db.Column(db.String(15))
    pm10 = db.Column(db.String(15))


Data_tbl = Table('data', Data.metadata)


def create_data_table():
    Data.metadata.create_all(engine)

def add_data(date, time, pm25, pm10):
    ins = Data_tbl.insert().values(
        date=date,
        time=time,
        pm25=pm25,
        pm10=pm10
        
    )
    conn = engine.connect()
    conn.execute(ins)
    conn.close()
