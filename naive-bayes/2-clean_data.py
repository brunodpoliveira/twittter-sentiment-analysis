import pandas as pd
import string

# adjust file name before starting program
# lineterminator avoids parser error
df = pd.read_csv('data/fun.csv', lineterminator='\n')

# remove rows w/ nan in them
df = df.dropna(axis=0, how='any')


# ------------------------------------------------------------------------

# non readable text gets converted into nothing
def remove_text(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])


# ------------------------------------------------------------------------

# remove text
df['text'] = df['text'].apply(remove_text)

# make text lower case
df['text'] = df['text'].apply(lambda x: x.lower())

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

# get each unique keyword from dataframe

array = df['text'].str.split(' ', expand=True).stack().value_counts()

# print(array)

# ------------------------------------------------------------------------

# dataframe of the words and their frequency
d = {'word': array.index, 'frequency': array}
df2 = pd.DataFrame(data=d)

# remove words mentioned less than 10 times
df2['frequency'] = df2['frequency'][df2['frequency'] > 10]

df2 = df2.dropna(axis=0, how='any')

# df2 = df2.drop([':(', 'https://t', ':((', ':(((', ':((((', ':(((((', ':', '(', ''])
df2 = df2.drop([':(', 'https://t', ':', '(', ''])

# ------------------------------------------------------------------------

# adjust file name before starting program
df2.to_csv('data/fun_words.csv', header=True, index=False, encoding='utf-8')
