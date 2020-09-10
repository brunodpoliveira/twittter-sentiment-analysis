from twython import TwythonStreamer
import csv
import json

# Load credentials from json file
with open('twitter_credentials.json', 'r') as file:
    creds = json.load(file)


# filter the data
def process_tweet(tweet):
    d = {'hashtags': [hashtag['text'] for hashtag in tweet['entities']['hashtags']], 'text': tweet['text'],
         'user': tweet['user']['screen_name'], 'user_loc': tweet['user']['location']}
    return d


class MyStreamer(TwythonStreamer):

    # received data
    def on_success(self, data):
        # english
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)
            # print(tweet_data)

    def on_error(self, status_code, data, headers=None):
        print(status_code, data)
        self.disconnect()

    # create a class that inherit TwythonStreamer
    @staticmethod
    def save_to_csv(tweet):
        with open(r'saved_tweets.csv', 'a') as savefile:
            writer = csv.writer(savefile)
            # commented line only necessary when creating file -
            # make sure to clean it up later
            # writer.writerow(['hashtags', 'text', 'user', 'user_loc'])
            writer.writerow(list(tweet.values()))


# instantiate from our streaming class
stream = MyStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],
                    creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
# stream start
stream.statuses.filter(track='python')
