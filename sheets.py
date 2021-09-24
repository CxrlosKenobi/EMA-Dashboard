from google.auth import credentials
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import json 

scopes = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheeets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

with open('credentials.json') as f:
    credentials = json.load(f)

gc = gspread.service_account_from_dict(credentials)
sh = gc.open('DataCollector')
data = sh.sheet1.get_all_values()


pprint(data)
