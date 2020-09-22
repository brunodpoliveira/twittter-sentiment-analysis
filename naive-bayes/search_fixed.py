from twython import Twython
import json
import pandas as pd

# show all of the list, w/no truncation
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

with open('data/twitter_credentials.json', 'r') as file:
    creds = json.load(file)

# instantiate object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])


def buildtestset():
    # create query

    query = {'q': input("Type query:"),
             'result_type': 'popular',
             'count': 100,
             'lang': 'en',
             }
    # search tweets

    dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
    for status in python_tweets.search(**query)['statuses']:
        dict_['user'].append(status['user']['screen_name'])
        dict_['date'].append(status['created_at'])
        dict_['text'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])
    # structure data in a pandas df
    df = pd.DataFrame(dict_)
    df.sort_values(by='favorite_count', inplace=True, ascending=False)
    # print(df)
