import json
import time
import gspread
import RPi.GPIO as GPIO
from oauth2client.client import SignedJwtAssertionCredentials

# Hardware interface
pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

# Log visitor to spreadsheet
def log_visitor():

    # OAuth
    json_key = json.load(open('######.json')) # SERVICE ACCOUNT KEY
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    gc = gspread.authorize(credentials)

    # Spreadsheet
    wks = gc.open_by_key('######') # SPREADSHEET KEY
    ws = wks.get_worksheet(0)

    # Append row: time, date, event, visitor
    ws.append_row([time.strftime('%H:%M:%S'), time.strftime('%d/%m/%Y'), 'MC', '1'])

# Listen for trigger
try:
    while True:
        if GPIO.input(pin) == True:
            log_visitor()
except KeyboardInterrupt:
    GPIO.cleanup()