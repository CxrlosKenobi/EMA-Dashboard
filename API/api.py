from google.oauth2.service_account import Credentials
from google.auth import credentials
from pprint import pprint
import datetime as dt
import time as t
import gspread
import random
import json 

with open('sender.json') as f:
    sender = json.load(f)
with open('listener.json') as f:
    listener = json.load(f)

def get_current_time():
    now = dt.datetime.now()
    total_time = (now.hour * 3600) + (now.minute * 60) + (now.second)
    return total_time

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
    gc = gspread.service_account_from_dict(sender)
    sh = gc.open('DataCollector')

    sheetData = sh.sheet1.get_all_values()

    newData = generateData()
    sheetData.append(newData)
    sh.sheet1.update(sheetData)

    print('[ ok ] Data sucessfully appended to sheet')
    

def dataReader():
    # Read the last 20 rows of the sheet
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/spreadsheeets',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive'
    ]
    gc = gspread.service_account_from_dict(listener)
    sh = gc.open('DataCollector')

    sheetData = sh.sheet1.get_all_values()

    # Return the last 20 rows
    return sheetData[-1]




def main():
    for i in range(10):
        connection(credentials)
        t.sleep(.5)


if __name__ == '__main__':
    main()
