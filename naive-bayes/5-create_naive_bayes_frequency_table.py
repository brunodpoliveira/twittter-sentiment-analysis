import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# ------------------------------------------------------------------------

happy = pd.read_csv('data/happy_split.csv')
fun = pd.read_csv('data/fun_split.csv')
joy = pd.read_csv('data/joy_split.csv')
afraid = pd.read_csv('data/afraid_split.csv')
sad = pd.read_csv('data/sad_split.csv')
angry = pd.read_csv('data/angry_split.csv')

word_bag = pd.read_csv('data/word_bag.csv')
word_bag = word_bag.drop_duplicates()

# ------------------------------------------------------------------------

# Classify tweets in pos(1) or neg(0)
happy['type'] = 1
fun['type'] = 1
joy['type'] = 1
afraid['type'] = 0
sad['type'] = 0
angry['type'] = 0

# ------------------------------------------------------------------------

# join all df into a big df for train/test split
df = pd.concat([happy, fun, joy, afraid, sad, angry]).reset_index(drop=True)

train, test = train_test_split(df, test_size=0.2)

train_pos = train[train['type'] == 1]
train_neg = train[train['type'] == 0]

instance_pos = len(train_pos)
instance_neg = len(train_neg)

# ------------------------------------------------------------------------

frequency = pd.DataFrame()
frequency['word'] = word_bag['word']

word_bank = [0] * len(frequency)
pos = [0] * len(frequency)
neg = [0] * len(frequency)

# ------------------------------------------------------------------------

# scan all words in freq table
for i in range(len(frequency)):
    # get the word in f table at given row
    word = frequency['word'].iloc[i]
    word_bank[i] = word

    # convert word and single colon onto both sides of the word
    check = str("'") + word + str("'")
    # count word instances
    count = 0

    # ------------------------------------------------------------------------

    # iterating through pos train set
    for j in range(len(train_pos)):
        appears = train_pos['text'].iloc[j].count(check)
        if appears > 0:
            count = count + 1
    pos[i] = count

    # ------------------------------------------------------------------------

    # iterating through neg train set
    count = 0
    for k in range(len(train_neg)):
        appears = train_neg['text'].iloc[k].count(check)
        if appears > 0:
            count = count + 1
    neg[i] = count
    print(i)
# ------------------------------------------------------------------------

d = {'word': word_bank, 'pos': pos, 'neg': neg}
f_table = pd.DataFrame(data=d)

f_table.to_csv('data/f_table.csv')
# copy paste these numbers to test naive bayes
print('instance_pos:', instance_pos)
print('instance_neg:', instance_neg)

