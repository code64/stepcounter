Raspberry Pi Stepcounter
====

Full tutorial and making of: http://code64.de/visionerdy/raspberry-pi-stepcounter/

Update and further information: http://code64.de/visionerdy/update-raspberry-pi-stepcounter/


How to use
-----------

Install [Gspread](https://github.com/burnash/gspread) and get your service account keys from the [Google Developer Console](https://console.developers.google.com/) as JSON key. 

Make sure to provide the correct path to the JSON file within `logger.py` and also update the spreadsheet key to match your own.

You'll need to share your spreadsheet with the email address within your JSON key file (see `client_email`).


Links
-----------

- [Gspread](https://github.com/burnash/gspread)
- [Gspread API Reference](http://gspread.readthedocs.org/en/latest/)