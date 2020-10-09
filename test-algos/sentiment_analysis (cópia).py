import json
import tweepy
import nltk
from pre_process import PreProcessTweet
from search_fixed import build_test_set

# ------------------------------------------------------------------------

with open('data/twitter_credentials.json', 'r') as file:
    creds = json.load(file)
# instantiate object
auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth)

# ------------------------------------------------------------------------

test_data_set = build_test_set()


# ------------------------------------------------------------------------

def build_training_set(corpus_file, tweet_data_file):
    import csv

    corpus = []

    with open(corpus_file, 'r') as csv_file:
        line_reader = csv.reader(csv_file, delimiter=',', quotechar="\"")
        for row in line_reader:
            corpus.append({"tweet_id": row[2], "label": row[1], "topic": row[0]})

    training_data_set = []

    for tweet in corpus:
        try:
            pass
            # status = api.get_status(tweet['tweet_id'])
            # print('Tweet fetched' + status.text)
            # tweet['text'] = status.text
            # training_data_set.append(tweet)
        except:
            continue
    # write the tweets to empty CSV file
    with open(tweet_data_file, 'w') as csv_file:
        line_writer = csv.writer(csv_file, delimiter=',', quotechar="\"")
        for tweet in training_data_set:
            try:
                pass
                # line_writer.writerow([tweet["tweet_id"], tweet["text"], tweet["label"], tweet["topic"]])
            except Exception as e:
                print(e)
    return training_data_set


# ------------------------------------------------------------------------


def build_vocabulary(pre_processed_training_data):
    all_words = []
    try:

        for (words, sentiment) in pre_processed_training_data:
            all_words.extend(words)
        word_list = nltk.FreqDist(all_words)
        word_features = word_list.keys()
    except Exception as e:
        print("error build vocab")


# ------------------------------------------------------------------------


def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features['contain(%s)' % word] = (word in tweet_words)
    return features


# ------------------------------------------------------------------------

corpus_read = './corpus.csv'
tweet_data_file_write = './tweet_data_file.csv'
training_data = build_training_set(corpus_read, tweet_data_file_write)
# training_data = './tweet_data_file.csv'


# ------------------------------------------------------------------------

tweet_processor = PreProcessTweet()
pre_processed_training_set = tweet_processor.process_tweets(training_data)
pre_processed_test_data_set = tweet_processor.process_tweets(test_data_set)

# ------------------------------------------------------------------------

word_features = build_vocabulary(pre_processed_training_set)
training_features = nltk.classify.apply_features(extract_features, pre_processed_training_set)

# ------------------------------------------------------------------------

NBayesClassifier = nltk.NaiveBayesClassifier.train(training_features)
NBResultsLabels = [NBayesClassifier.classify(extract_features(tweet[0])) for tweet in pre_processed_test_data_set]
# get the majority vote

if NBResultsLabels.count('positive') > NBResultsLabels.count('negative'):
    print('positive sentiment overall')
    print(
        'positive sentiment percentage = ' + str(100 * NBResultsLabels.count('positive') / len(NBResultsLabels)) + '%')
else:
    print('negative sentiment overall')
    print(
        'negative sentiment percentage = ' + str(100 * NBResultsLabels.count('negative') / len(NBResultsLabels)) + '%')
