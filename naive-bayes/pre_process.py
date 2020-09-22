import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords


class PreProcessTweet:

    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])

    def process_tweets(self, listoftweets):
        processedtweets = []
        try:
            for tweet in listoftweets:
                processedtweets.append((self._processtweet(tweet['text']), tweet['label']))
        except Exception as e:
            print("error process tweets")

    def _process_tweet(self, tweet):
        tweet = tweet.lower()  # convert text to lowercase
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove urls
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
        tweet = word_tokenize(tweet)  # remove repeated charachters (e.g helloooo - hello)
        return [word for word in tweet if word not in self._stopwords]
