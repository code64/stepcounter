#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime
import ConfigParser
import os
import twitter
import random
from random import randint
import RPi.GPIO as GPIO
import sys


# Parse twitter-python config file
def get_tweetrc(key):
    config = ConfigParser.ConfigParser()
    config.read(os.path.expanduser('~/.tweetrc'))
    return config.get('Tweet', key)


# Software interface
visitors = int(sys.argv[1]) if len(sys.argv) > 1 else 0
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
        'Unser Stepcounter zeigt aktuell %d Stufen an. #mcbw64',
        'Auf zur Agentur mit der schönen Aussicht. Heute Abend gesamt %d Stufen. #mcbw64',
        'Jeder unserer Besucher braucht 83 Stufen hier hinauf. Alle zusammen haben bisher %d Stufen erklommen. Awesome! #mcbw64'
    ],
    'meters': [
        'Unsere fleissigen Besucher haben schon %d Höhenmeter geschafft. Weiter so! #mcbw64',
        'Der Weg ist das Ziel: Bisher wurden %d Meter erreicht. #mcbw64',
        'It\'s a long way to the top if you wanna rock\'n\'roll! Genauer gesagt %d Höhenmeter. #mcbw64',
        'Die Frauenkirche ist fast 100 Meter hoch. Wir haben schon %d Meter geschafft. #mcbw64',
        'Nichts für Menschen mit Höhenangst: zusammen haben wir %d Höhenmeter erreicht. #mcbw64',
        'Unser Stepcounter zählt fleissig mit: Bisher wurden %d Höhenmeter erreicht. #mcbw64',
        'Höhenluft schnuppern: Bei @CODE64 wurden heute %d Meter geklettert! #mcbw64',
        'High way to @CODE64: %d Meter schafften die #MCBW Besucher bisher! #mcbw64',
        'Nicht 8 Miles high, aber immerhin schon %d Meter zeigt unser Stepcounter an. #mcbw64'
    ]
}


# Get random message from dictionary
def get_message(key):
    length = len(msg[key])
    return msg[key][randint(0, length - 1)]


# Take picture
def get_picture(count):
    now = datetime.now()
    media = "./img/%d-%d-%d-%d%d_%d.jpg" % (now.year, now.month, now.day, now.minute, now.second, count)
    os.system("sudo fswebcam -r 1280x720 -D 1 --no-banner -d /dev/video0 -v " + media)
    return media


# Post update with media to twitter
def tweet(count):
    try:
        key = random.choice(env.keys())
        message = get_message(key) % (count * env[key])
        media = get_picture(count)

        # Arguments: status, media, possibly_sensitive
        status = api.PostMedia(message, media, False)
        print 'Visitor #%d just posted: %s' % (count, status.text)
    except Exception as error:
        print error


# Listen for trigger
try:
    while True:
        if GPIO.input(pin):
            visitors += 1
            tweet(visitors)
            time.sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()
