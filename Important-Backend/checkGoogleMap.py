# import googlemaps
# from datetime import datetime

# gmaps = googlemaps.Client(key='AIzaSyCVtJ6jb6vro5RvWz31GDDSgjmHxvEdu-U')

# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print(geocode_result)

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# print(reverse_geocode_result)

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                     "Parramatta, NSW",
#                                     mode="transit",
#                                     departure_time=now)


"""
Simple Program to help you get started with Google's APIs
"""
import urllib.request, json
#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCA-EgW2VVPJO6pdSWxUKV9Ws3AVjdLiqo'
#Asks the user to input Where they are and where they want to go.
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')
#Building the URL for the request
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()
#Loads response as JSON
directions = json.loads(response)
print(directions)