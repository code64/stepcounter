import RPi.GPIO as GPIO
import time
import gdata.spreadsheet.service
import os
import subprocess

email = 'EMAIL'
password = 'PASSWORD'
spreadsheet_key = 'SPREADSHEET_KEY'
worksheet_id = 'WORKSHEED_ID' # Probably od6

pin = 18
count = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def log_visitor():

   spr_client = gdata.spreadsheet.service.SpreadsheetsService()
   spr_client.email = email
   spr_client.password = password
   spr_client.source = 'MCBW IR Logger'
   spr_client.ProgrammaticLogin()

   dict = {}
   dict['date'] = time.strftime('%d/%m/%Y')
   dict['time'] = time.strftime('%H:%M:%S')
   dict['event'] = 'MCBW'
   dict['visitor'] = '1'

   entry = spr_client.InsertRow(dict, spreadsheet_key, worksheet_id)
   if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
     print 'Saved.'
   else:
     print 'Failed.'
   return 0

try:
    while True:
        if GPIO.input(pin) == True:
            log_visitor()
            count += 1
            time.sleep(2)
except KeyboardInterrupt:
    GPIO.output(status, False)
    GPIO.cleanup()