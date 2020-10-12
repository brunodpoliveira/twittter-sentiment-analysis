import pandas as pd
import string

# adjust file name before starting program
# lineterminator avoids parser error
df = pd.read_csv('data/angry.csv', lineterminator='\n')

# remove rows w/ nan in them
df = df.dropna(axis=0, how='any')


# ------------------------------------------------------------------------

# non readable text gets converted into nothing
def remove_text(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])


# remove text
df['text'] = df['text'].apply(remove_text)

# make text lower case
df['text'] = df['text'].apply(lambda x: x.lower())

# ------------------------------------------------------------------------

# remove punctuation + extra lines
# df['text'] = df['text'].apply(lambda x: x.replace('', ' '))

df['text'] = df['text'].apply(lambda x: x.replace('.', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('\n', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('?', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('!', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('"', ' '))
df['text'] = df['text'].apply(lambda x: x.replace(';', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('#', ' '))
df['text'] = df['text'].apply(lambda x: x.replace('&amp', ' '))
df['text'] = df['text'].apply(lambda x: x.replace(',', ' '))

# ------------------------------------------------------------------------

# split all the words in file
df['text'] = df['text'].str.split()

# adjust file name before starting program
df.to_csv('data/angry_split.csv')
