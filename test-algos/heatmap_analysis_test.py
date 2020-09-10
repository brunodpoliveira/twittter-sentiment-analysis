from geopy.geocoders import Nominatim
import gmplot
from data_analysis_test import tweets

geolocator = Nominatim(user_agent="test-app")

# go through  tweets, add locs to coords dict
coords = {'latitude': [], 'longitude': []}
for count, user_loc in enumerate(tweets.location):
    try:
        location = geolocator.geocode(user_loc)

        if location:
            coords['latitude'].append(location.latitude)
            coords['longitude'].append(location.longitude)

    # if too many connection requests
    except:
        pass

# create and center a gmp object to show the map
gmap = gmplot.GoogleMapPlotter(30, 0, 3)

# insert points on map passing a list of coords
gmap.heatmap(coords['latitude'], coords['longitude'], radius=20)

# save the map to a html file
gmap.draw("python_heatmap.html")
