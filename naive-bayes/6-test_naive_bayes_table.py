import pandas as pd
import numpy as np
# ------------------------------------------------------------------------

f_table = pd.read_csv('data/f_table.csv')
f_table = f_table[f_table['word'] != 'happy']
f_table = f_table[f_table['word'] != 'happy,']
f_table = f_table[f_table['word'] != 'fun']
f_table = f_table[f_table['word'] != 'fun,']
f_table = f_table[f_table['word'] != 'joy']
f_table = f_table[f_table['word'] != 'joy,']
f_table = f_table[f_table['word'] != 'afraid']
f_table = f_table[f_table['word'] != 'afraid,']
f_table = f_table[f_table['word'] != 'sad']
f_table = f_table[f_table['word'] != 'sad,']
f_table = f_table[f_table['word'] != 'angry']
f_table = f_table[f_table['word'] != 'angry,']
f_table = f_table.drop_duplicates(subset='word')

# ------------------------------------------------------------------------

test_sentence = input('Type test sentence: ')
# check create_naive_bayes and the print(instance_pos/neg) outputs and put the numbers here
instance_pos = 35935.0
instance_neg = 36060.0

test_words = test_sentence.split()
prob_pos = float(instance_pos / (instance_pos + instance_neg))
prob_neg = 1 - prob_pos

word_pos = 1.0 * prob_pos
word_neg = 1.0 * prob_neg

# ------------------------------------------------------------------------

for i in range(len(test_words)):
    word = test_words[i]
    print(word)
    index_val = f_table.index[f_table['word'] == word]
    if len(index_val) > 0:
        print(index_val[0])
        val_pos = f_table['pos'].iloc[index_val[0]]
        val_neg = f_table['neg'].iloc[index_val[0]]
        word_pos = word_pos * val_pos / instance_pos
        word_neg = word_neg * val_neg / instance_neg

# ------------------------------------------------------------------------

if word_pos > word_neg:
    print('positive - probability', word_pos / (word_pos + word_neg))
else:
    print('negative - probability', word_neg / (word_pos + word_neg))
