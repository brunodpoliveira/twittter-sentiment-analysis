import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords


class PreProcessTweet:

    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])

    def processtweets(self, listoftweets):
        processedtweets = []
        for tweet in listoftweets:
            processedtweets.append((self._processtweet(tweet['text']), tweet['label']))
        return processedtweets

    def _processtweet(self, tweet):
        tweet = tweet.lower()  # convert text to lowercase
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove urls
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
        tweet = word_tokenize(tweet)  # remove repeated charachters (e.g helloooo - hello)
        return [word for word in tweet if word not in self._stopwords]
