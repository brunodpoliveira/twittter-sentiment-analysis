import pandas as pd

# ------------------------------------------------------------------------

happy = pd.read_csv('data/happy_words.csv')
fun = pd.read_csv('data/fun_words.csv')
joy = pd.read_csv('data/joy_words.csv')
fearful = pd.read_csv('data/fearful_words.csv')
sad = pd.read_csv('data/sad_words.csv')
angry = pd.read_csv('data/angry_words.csv')

word_bag = pd.concat([happy, sad, fearful, angry]).drop_duplicates().reset_index(drop=True)

print(word_bag)
word_bag.to_csv('data/word_bag.csv')
