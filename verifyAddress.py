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

try:
    address = {
    'country_code': 'In',
    'country_area': 'महाराष्ट्र',
    'city': 'मुंबई',
    'city_area': 'कांदिवली',
    'postal_code': '400067',
    'street_address': 'कांदिवली'
    }
    address1 = {
    'country_code': 'US',
    'country_area': 'California',
    'city': 'Mountain View',
    'postal_code': '9',
    'street_address': '1600 Amphitheatre Pkwy'}
    a = normalize_address(address1)
    print(a)
    print(format_address(address1, latin=True))
except InvalidAddress as e:
    print(type(e.errors))

# print(get_validation_rules({'country_code': 'IN', 'country_area': 'Maharashtra'}))
