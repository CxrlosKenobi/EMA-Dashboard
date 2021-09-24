from datetime import datetime
import datetime as dt
import time as t
import random
import sqlite3
import pandas as pd

def get_current_time():
    now = dt.datetime.now()
    total_time = (now.hour * 3600) + (now.minute * 60) + (now.second)
    return total_time

db = sqlite3.connect('datarand.db')
cur = db.cursor()

for i in range(1, 1800):
    print(f'[ {i} ] Running ...')
    now = datetime.now()
    #   Asign random values to test
    timestamp = now.strftime('%d/%m, %H:%M:%S')
    timeinsec = get_current_time()
   
    pm10 = random.randint(0, 100)
    pm25 = random.randint(0, 100)

    
    packet = f"""{now.strftime('%d/%m, %H:%M:%S')};{get_current_time()};{pm10};{pm25}"""

    cur.execute('''
        INSERT INTO data VALUES (?, ?, ?, ?)''', (timestamp, timeinsec, pm10, pm25))
    t.sleep(1)
    db.commit()

cur.close()
