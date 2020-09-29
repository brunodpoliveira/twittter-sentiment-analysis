import json
import tweepy
from textblob import TextBlob

# ------------------------------------------------------------------------

with open('data/twitter_credentials.json', 'r') as file:
    creds = json.load(file)
# instantiate object
auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth)

public_tweets = api.search('dogs')
# ------------------------------------------------------------------------

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0] > 0:
        print('Positive')
    elif analysis.sentiment[0] < 0:
        print('Negative')
    else:
        print('Neutral')
    print("")

# ------------------------------------------------------------------------
