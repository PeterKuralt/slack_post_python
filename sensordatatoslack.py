import requests
import json
import config
from datetime import datetime

#defining values
message = "Anything you want, from sensor data to messages"
today = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

#storing values
slackstring = "I am sending message {} at {}".format(message, today)
slackdata = {"text":slackstring}

#gathering url and secret from config.py
secret = config.secret
url_slack = config.url
#setting headers
headers = {"Content-Type":"application/json","secret":secret}

#sending the data to slack using requests
r = requests.post(url = url_slack, data=json.dumps(slackdata), headers=headers)
