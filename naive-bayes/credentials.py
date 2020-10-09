import json

# Enter keys/secrets below as strings

credentials = {}
credentials['CONSUMER_KEY'] = 'J7UpsIsqb2Q4hhS0oqmxwxyUO'
credentials['CONSUMER_SECRET'] = '6jnwMUXaIo1xxSqVNnhXhubwhFOoQ1tNc1VTvN1BngBWHLapZZ'
credentials['ACCESS_TOKEN'] = '1301885931998371840-AfGQ0LSiBbdkrTFueFjPO1C0g2c9tR'
credentials['ACCESS_SECRET'] = 'xN54XK90ci9MeXybp8tn98TWrpVZFNDUPQtGZwJGV0Nlw'

# Save to file
with open("twitter_credentials.json","w") as file: json.dump(credentials, file)
