import twitter
from twython import Twython
import json
import pandas as pd

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# instantiate object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])


