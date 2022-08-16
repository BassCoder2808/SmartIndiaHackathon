import requests
import urllib.parse

address = 'Rail Mitra, Plot no 125, Sector 1, Charkop, Kandivali, Mumbai, 400067'
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

response = requests.get(url).json()
print(response)
# print("latitude: "+response[0]["lat"])
# print("longitude: "+response[0]["lon"])