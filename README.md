# Raspberry Pi Sensor

- [Tutorial and making of](https://code64.de/visionerdy/raspberry-pi-stepcounter/) 
- [Update and further information](https://code64.de/visionerdy/raspberry-pi-stepcounter-v2/)


## Twitter

Posts check-ins to [Twitter](https://twitter.com/).


### Setup

Install [Python Twitter](https://github.com/bear/python-twitter) and register your app at the [Twitter Application Management Center](https://apps.twitter.com/).

Enter the Twitter consumer and access tokens (key and secret) within the `~/.tweetrc` config file.

Now you should be able to run `python tweet.py` from the terminal.


### Links

- [Python Twitter](https://github.com/bear/python-twitter)
- [Twitter API](https://dev.twitter.com/)


-----


## Google Sheets

Posts check-ins to [Google Sheets](https://www.google.com/sheets/about). 


### Setup

Install [Gspread](https://github.com/burnash/gspread) and get your service account keys from the [Google Developer Console](https://console.developers.google.com/) as JSON key. 

Make sure to provide the correct path to the JSON file within `logger.py` and also update the sheet key to match your own.

You'll need to share your sheet with the email address within your JSON key file (see `client_email`).


### Reboot

Setup a cronjob to always launch the logger on startup via `launcher.sh` while logging errors to our own logfile:

```
@reboot sh /home/pi/logger/launcher.sh >/home/pi/logger/logs/cronlog 2>&1
```


### Links

- [Gspread](https://github.com/burnash/gspread)
- [Gspread API Reference](http://gspread.readthedocs.org/en/latest/)
