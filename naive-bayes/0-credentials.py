import json

# Enter keys/secrets below as strings

credentials = {}
credentials['CONSUMER_KEY'] = ''
credentials['CONSUMER_SECRET'] = ''
credentials['ACCESS_TOKEN'] = ''
credentials['ACCESS_SECRET'] = ''

# Save to file
with open("twitter_credentials.json","w") as file: json.dump(credentials, file)
