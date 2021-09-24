from google.oauth2.service_account import Credentials
from google.auth import credentials
from pprint import pprint
import datetime as dt
import time as t
import gspread
import random
import json 

def dataReader(credentials):
    # Read the last 20 rows of the sheet
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/spreadsheeets',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive'
    ]
    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open('DataCollector')

    sheetData = sh.sheet1.get_all_values()

    # Return the last 20 rows
    pprint(sheetData[-20:])


while True:
    with open('../listener.json') as f:
        credentials = json.load(f)
        dataReader(credentials)
        t.sleep(10)




    