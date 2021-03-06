# Raspberry Pi Sensor

- [Tutorial and making of](https://code64.de/visionerdy/raspberry-pi-stepcounter/)
- [Raspberry Pi Stepcounter v2](https://code64.de/visionerdy/raspberry-pi-stepcounter-v2/)
- [Raspberry Pi Stepcounter v3](https://code64.de/visionerdy/raspberry-pi-stepcounter-v3/)


## Examples

Currently there are three different examples to utilize the sensor via the Raspberry Pi GPIO pins. 
Each example also has a script without the GPIO dependency to allow quick tests without the hardware interface.


### Example 1: Twitter

Posts check-ins to [Twitter](https://twitter.com/).


#### Setup

Install [Python Twitter](https://github.com/bear/python-twitter) and register your app at the [Twitter Application Management Center](https://apps.twitter.com/).

Enter the Twitter consumer and access tokens (respectively key and secret) within your `~/.tweetrc` config file.

Now you should be able to run `python ./twitter/logger.py` from the terminal to post the default messages (randomly) to Twitter.


Optional: 

- Append the _number of visitors_ (integer) to overwrite the starting point: `python ./twitter/logger.py 3`


#### Reboot

Setup a cronjob to always launch the logger on startup via `./twitter/launcher.sh` while logging errors to your logfile:

```
@reboot sh /path/to/logger/twitter/launcher.sh > /path/to/logger/twitter/logs/cronlog 2>&1
```


#### Links

- [Python Twitter](https://github.com/bear/python-twitter)
- [Twitter API](https://dev.twitter.com/)



### Example 2: JSON

Write check-ins to a JSON file.


#### Setup

Run `python ./json/logger.py` from the terminal to update your JSON file: `./json/logs/data.json`

There is also a simple tech-demo using the HTML5 server-sent event (SSE) EventSource API within the `./json/demo` folder.


Optional: 

- Append the _number of visitors_ (integer) to overwrite the starting point: `python ./json/logger.py 3`


#### Reboot

Setup a cronjob to always launch the logger on startup via `./json/launcher.sh` while logging errors to your logfile:

```
@reboot sh /path/to/logger/json/launcher.sh > /path/to/logger/json/logs/cronlog 2>&1
```


#### Links

- [Server-Sent Events](https://en.wikipedia.org/wiki/Server-sent_events)



### Example 3: Google Sheets

Posts check-ins to [Google Sheets](https://www.google.com/sheets/about).


#### Setup

Install [Gspread](https://github.com/burnash/gspread) and get your service account keys from the [Google Developer Console](https://console.developers.google.com/) as JSON key.

Make sure to provide the correct path to the JSON file within `./google/logger.py` and also update the sheet key to match your own.

You'll need to share your sheet with the email address within your JSON key file (see `client_email`).


#### Reboot

Setup a cronjob to always launch the logger on startup via `./google/launcher.sh` while logging errors to your logfile:

```
@reboot sh /path/to/logger/google/launcher.sh > /path/to/logger/google/logs/cronlog 2>&1
```


#### Links

- [Gspread](https://github.com/burnash/gspread)
- [Gspread API Reference](http://gspread.readthedocs.org/en/latest/)



## Support

Always feel free to [raise an issue](https://github.com/code64/stepcounter/issues) on GitHub.
