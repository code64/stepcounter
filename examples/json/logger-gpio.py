#!/usr/bin/env python

import time
import json
import RPi.GPIO as GPIO
import sys

# Defaults
visitors = int(sys.argv[1]) if len(sys.argv) > 1 else 0

# Hardware interface
pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)


# Log visitor to console
def log(count):
    print 'Logged visitor #%d' % count


# Update JSON file
def store(count):
    # Prepare dictionary
    data = {
        'data': str(count)
    }
    # Open and write to file
    with open('./logs/data.json', 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()


# Listen for trigger
try:
    while True:
        if GPIO.input(pin):
            visitors += 1
            store(visitors)
            log(visitors)
            time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
