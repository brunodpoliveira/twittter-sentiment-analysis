import pandas as pd
from collections import Counter
import ast

tweets = pd.read_csv("saved_tweets.csv")

# Extract hashtags and put them in a list
list_hashtag_strings = [entry for entry in tweets.hashtags]
list_hashtag_lists = ast.literal_eval(','.join(list_hashtag_strings))
hashtag_list = [ht.lower() for list_ in list_hashtag_lists for ht in list_]
# count the most common
counter_hashtags = Counter(hashtag_list)
counter_hashtags.most_common(20)
print(counter_hashtags.most_common(20))
