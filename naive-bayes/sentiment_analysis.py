import json
import tweepy
import nltk
from preprocess import PreProcessTweet
from search_fixed import buildtestset

# ------------------------------------------------------------------------

with open('data/twitter_credentials.json', 'r') as file:
    creds = json.load(file)
# instantiate object
auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth)
# ------------------------------------------------------------------------

testdataset = buildtestset()


# ------------------------------------------------------------------------

def buildtrainingset(corpusfile, tweetdatafile):
    import csv

    corpus = []

    with open(corpusfile, 'r') as csvfile:
        linereader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        for row in linereader:
            corpus.append({"tweet_id": row[2], "label": row[1], "topic": row[0]})

    trainingdataset = []

    for tweet in corpus:
        try:
            pass
            #status = api.get_status(tweet['tweet_id'])
            #print('Tweet fetched' + status.text)
            #tweet['text'] = status.text
            #trainingdataset.append(tweet)
        except:
            continue
    # write the tweets to empty CSV file
    with open(tweetdatafile, 'w') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',', quotechar="\"")
        for tweet in trainingdataset:
            try:
                pass
                #linewriter.writerow([tweet["tweet_id"], tweet["text"], tweet["label"], tweet["topic"]])
            except Exception as e:
                print(e)
    return trainingdataset


# ------------------------------------------------------------------------


def buildvocabulary(preprocessedtrainingdata):
    all_words = []

    for (words, sentiment) in preprocessedtrainingdata:
        all_words.extend(words)
    wordlist = nltk.FreqDist(all_words)
    wordfeatures = wordlist.keys()

    return wordfeatures


# ------------------------------------------------------------------------


def extractfeatures(tweet):
    tweetwords = set(tweet)
    features = {}
    for word in wordfeatures:
        features['contain(%s)' % word] = (word in tweetwords)
    return features


# ------------------------------------------------------------------------

corpusRead = './corpus.csv'
tweetDataFileWrite = './tweetdatafile.csv'
trainingdata = buildtrainingset(corpusRead, tweetDataFileWrite)
# trainingdata = './tweetdatafile.csv'


# ------------------------------------------------------------------------

tweetprocessor = PreProcessTweet()
preprocessedtrainingset = tweetprocessor.processtweets(trainingdata)
preprocessedtestdataset = tweetprocessor.processtweets(testdataset)

# ------------------------------------------------------------------------

wordfeatures = buildvocabulary(preprocessedtrainingdata)
trainingfeatures = nltk.classify.apply_features(extractfeatures, preprocessedtrainingdata)

# ------------------------------------------------------------------------

NBayesClassifier = nltk.NaiveBayesClassifier.train(trainingfeatures)
NBResultsLabels = [NBayesClassifier.classify(extractfeatures(tweet[0])) for tweet in preprocessedtestdataset]
# get the majority vote

if NBResultsLabels.count('positive') > NBResultsLabels.count('negative'):
    print('positive sentiment overall')
    print(
        'positive sentiment percentage = ' + str(100 * NBResultsLabels.count('positive') / len(NBResultsLabels)) + '%')
else:
    print('negative sentiment overall')
    print(
        'negative sentiment percentage = ' + str(100 * NBResultsLabels.count('negative') / len(NBResultsLabels)) + '%')
