#!/usr/bin/env python

import time
import json

# Defaults
visitors = 0


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
        visitors += 1
        store(visitors)
        log(visitors)
        time.sleep(2)
except KeyboardInterrupt:
    pass
