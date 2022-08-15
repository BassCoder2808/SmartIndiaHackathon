import requests
import urllib.parse

address = 'Rajpath'
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

response = requests.get(url).json()
print("latitude: "+response[0]["lat"])
print("longitude: "+response[0]["lon"])