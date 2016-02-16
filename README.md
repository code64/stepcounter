# CODE64 Raspberry Pi Stepcounter

- [Tutorial and making of](https://code64.de/visionerdy/raspberry-pi-stepcounter/) 
- [Update and further information](https://code64.de/visionerdy/raspberry-pi-stepcounter-v2/)


### How to use

Install [Gspread](https://github.com/burnash/gspread) and get your service account keys from the [Google Developer Console](https://console.developers.google.com/) as JSON key. 

Make sure to provide the correct path to the JSON file within `logger.py` and also update the spreadsheet key to match your own.

You'll need to share your spreadsheet with the email address within your JSON key file (see `client_email`).


### Reboot

Setup a cronjob to always launch the logger on startup via `launcher.sh` while logging errors to our own logfile:

```
@reboot sh /home/pi/logger/launcher.sh >/home/pi/logger/logs/cronlog 2>&1
```


### Links

- [Gspread](https://github.com/burnash/gspread)
- [Gspread API Reference](http://gspread.readthedocs.org/en/latest/)
