import json
import tweepy
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pandas as pd

# ------------------------------------------------------------------------

with open('data/twitter_credentials.json', 'r') as file:
    creds = json.load(file)
# instantiate object
auth = OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# ------------------------------------------------------------------------

search_query = input("Type query:")

users = tweepy.Cursor(api.search, q=search_query).items()
count = 0
start = 0
error_count = 0


# ------------------------------------------------------------------------

# search params
wait_query = 100
wait_time = 2.0
total_number = 15000
# halt for x minutes just in case twitter throttles us
just_in_case = 1
text = [0] * total_number
second_count = 0
# 1 - happy | 2 - fun | 3 - joy | 4 - fearful | 5 - sad | 6 - angry
# adjust number before starting program
id_values = [1] * total_number

# ------------------------------------------------------------------------

while second_count < total_number:
    try:
        user = next(users)
        count += 1

        # break
        if count % wait_query == 0:
            time.sleep(wait_time)
    except tweepy.TweepError:
        print('sleeping...')
        time.sleep(60 * just_in_case)
        user = next(users)

    except StopIteration:
        break
    try:
        # print('writing to json tweet number: ' + str(count))
        text_value = user._json['text']
        language = user._json['lang']
        print(text_value)
        # print(language)

        if 'RT' not in text_value:
            if language == 'en':
                text[second_count] = text_value
                second_count = second_count + 1
                print('current saved is:', second_count)
    except UnicodeEncodeError:
        error_count += 1
        print('unicode_encode_error,error_count = ' + str(error_count))

# ------------------------------------------------------------------------

print('creating dataframe:')
d = {'text': text, 'id': id_values}
df = pd.DataFrame(data=d)
# adjust file name before starting program
df.to_csv('data/happy.csv', header=True, index=False, encoding='utf-8')
print('complete')
