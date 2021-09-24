from google.oauth2.service_account import Credentials
from google.auth import credentials
from pprint import pprint
import datetime as dt
import time as t
import gspread
import random
import json 

def generateData():
    now = dt.datetime.now()
    timestamp = now.strftime('%d/%m')
    time = now.strftime('%H:%M:%S')

    pm25 = random.randint(20, 22)
    pm10 = random.randint(0, 100)

    dataRow = [timestamp, time, pm25, pm10]

    return dataRow

def connection(credentials):
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/spreadsheeets',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive'
    ]
    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open('DataCollector')

    sheetData = sh.sheet1.get_all_values()

    newData = generateData()
    sheetData.append(newData)
    sh.sheet1.update(sheetData)

    print('[ ok ] Data sucessfully appended to sheet')

def main():
    with open('../sender.json') as f:
        credentials = json.load(f)

    for i in range(1000):
        print(f'{i} || {connection(credentials)}')
        t.sleep(6)

main()
