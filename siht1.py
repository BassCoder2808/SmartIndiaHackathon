# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="my_user_agent")
# city ="London"
# country ="Uk"
# loc = geolocator.geocode(city+','+ country)
# print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)

from geopy.geocoders import Nominatim

address='Charkop, Kandivali, Mumbai, 400067'
geolocator = Nominatim(user_agent="Your_Name")
location = geolocator.geocode(address)
print(location.address)
print((location.latitude, location.longitude))
