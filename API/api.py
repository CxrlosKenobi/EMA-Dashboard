from google.oauth2.service_account import Credentials
from google.auth import credentials
import datetime as dt
from pprint import pprint
import time as t
import gspread
import random
import json 


def get_current_time():
    now = dt.datetime.now()
    total_time = (now.hour * 3600) + (now.minute * 60) + (now.second)
    return total_time

def generateData():
    now = dt.datetime.now()
    timestamp = now.strftime('%d/%m, %H:%M:%S')
    timeinsec = get_current_time()

    hdc1080_hu = random.randint(0, 100)
    hdc1080_te = random.randint(20, 22)

    dataRow = [timestamp, hdc1080_hu, hdc1080_te]
    
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
    with open('credentials.json') as f:
        credentials = json.load(f)
    for i in range(120):
        connection(credentials)
        t.sleep(1)

if __name__ == '__main__':
    main()
