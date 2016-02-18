#!/usr/bin/env python

import time
import ConfigParser
import os
import twitter
import random
from random import randint
import RPi.GPIO as GPIO


# Parse twitter-python config file
def get_tweetrc(key):
    config = ConfigParser.ConfigParser()
    config.read(os.path.expanduser('~/.tweetrc'))
    return config.get('Tweet', key)


# Software interface
visitors = 0
api = twitter.Api(consumer_key=get_tweetrc('consumer_key'),
                  consumer_secret=get_tweetrc('consumer_secret'),
                  access_token_key=get_tweetrc('access_key'),
                  access_token_secret=get_tweetrc('access_secret'))

# Hardware interface
pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

# Dictionary with available environments
env = {
    'stairs': 83,
    'meters': 14
}

# Dictionary with available messages
msg = {
    'stairs': [
        'MCBW64 Status: %d steps so far! #mcbw64',
        'You\'ve just added 83 steps to a total of %d steps! #mcbw64'
    ],
    'meters': [
        'MCBW64 Status: %d meters so far! #mcbw64',
        'Today we\'ve mounted %d meters! #mcbw64'
    ]
}


# Get random message from dictionary
def get_message(key):
    length = len(msg[key])
    return msg[key][randint(0, length - 1)]


# Post update to twitter
def tweet(count):
    try:
        key = random.choice(env.keys())
        status = api.PostUpdate(get_message(key) % (count * env[key]))
        print 'Visitor #%d just posted: %s' % (count, status.text)
    except Exception as error:
        print error


# Listen for trigger
try:
    while True:
        if GPIO.input(pin):
            visitors += 1
            tweet(visitors)
            time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
