# import googlemaps
# from datetime import datetime

# gmaps = googlemaps.Client(key='')

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
endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?'
api_key = ''
#Asks the user to input Where they are and where they want to go.
origin = 'rail mitra plot number 125, sector 1 charkop, kandivali west, mumbai 400067'
# destination = input('Where do you want to go?: ').replace(' ','+')
#Building the URL for the request
nav_request = 'address={}&key={}'.format(origin,api_key)
request = endpoint + nav_request
request = request.replace(" ", "%20")
#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()
#Loads response as JSON
directions = json.loads(response)
print(directions)




# google_maps_api= "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}"
# api_key = 'AIzaSyCA-EgW2VVPJO6pdSWxUKV9Ws3AVjdLiqo'
# address = 'rail mitra plot number 125, sector 1 charkop, kandivali west, mumbai 400067'
# location_data = google_maps_api.format(address,api_key)
# # coords = location_data.json()["results"][0]["geometry"]["location"]
# # lat,lng = coords["lat"],coords["lng"]
# response = urllib.request.urlopen(location_data).read()
# #Loads response as JSON
# directions = json.loads(response)
# print(directions)
