"""
    Here is the list of recognized fields:

    country_code is a two-letter ISO 3166-1 country code
    country_area is a designation of a region, province or state, recognized values include official names, designated abbreviations, official translations and latin transliterations
    city is a city or town name, recognized values include official names, official translations and latin transliterations
    city_area is a sublocality like a district, recognized values include official names, official translations and latin transliterations
    street_address is the (possibly multiline) street address
    postal_code is a postal code or zip code
    sorting_code is a sorting code
    name is a person's name
    company_name is a name of a company or organization
"""

from i18naddress import InvalidAddress, normalize_address, latinize_address, format_address, get_validation_rules

import requests
import json



address = {
'country_code': 'In',
'country_area': 'महाराष्ट्र',
'city': 'Judai',
'city_area': 'aaaaaaaaaaaaaaa',
'postal_code': '400067',
'street_address': 'aaaaaaaaaaaaaaa'
}

response_API = requests.get('https://api.postalpincode.in/pincode/' + address["postal_code"])
data = response_API.text
data = json.loads(data)[0]

found_city = 0
found_street = 0

# name, district, division, region,  block
if data['Status'] == 'Success':
    post_office_data = data['PostOffice']
    for data in post_office_data:
        if address["city"] in data["District"] or address["city"] in data["Division"] or address["city"] in data["Block"]:
            found_city = 1
        arr1 = data["Name"].split(" ")
        arr2 = data["Division"].split(" ")
        arr3 = data["Block"].split(" ")

        # using remove() to
        # perform removal
        while("" in arr1) :
            arr1.remove("")

        while("" in arr2) :
            arr2.remove("")

        while("" in arr3) :
            arr3.remove("")

        print(arr1, arr2, arr3)

        for d in arr1:
            if d in address["street_address"] or d in address["city_area"]:
                print(d)
                found_street = 1
        
        for d in arr2:
            if d in address["street_address"] or d in address["city_area"]:
                print(d)
                found_street = 1

        for d in arr3:
            if d in address["street_address"] or d in address["city_area"]:
                print(d)
                found_street = 1

print(found_city, found_street)

try:
    address = {
    'country_code': 'In',
    'country_area': 'महाराष्ट्र',
    'city': 'Judai',
    'city_area': 'aaaaaaaaaaaaaaa',
    'postal_code': '400067',
    'street_address': 'aaaaaaaaaaaaaaa'
    }
    address1 = {
    'country_code': 'US',
    'country_area': 'California',
    'city': 'Mountain View',
    'postal_code': '400067',
    'street_address': '1600 Amphitheatre Pkwy'}
    a = latinize_address(address1)
    print(a)
    print(format_address(address1, latin=True))

    found_city = 0

    if found_city == 0:
        raise InvalidAddress(errors = "Invalid city", message = "Please enter a valid city for pincode")
except InvalidAddress as e:
    print(e.errors)

# print(get_validation_rules({'country_code': 'IN', 'country_area': 'Maharashtra'}))
