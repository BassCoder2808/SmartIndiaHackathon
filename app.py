# 1. Post office lat lon
# 2. Address to lat lon api
# 3. How to find distance between two lat lon
# Horizontal and vertical distance
# https://data.gov.in/node/6818285
# 4. Check building name with database
# 5. Divide given address into building name, flat number, pincode
# fake point
# 1. Aayush
# 2. Anushka
# 3. Jai
# 4. 
# 5. Vedant and Jaiwin

# Imports for WebApp
from flask import *

# Importing geopy library (For Coordinates)
from geopy.geocoders import Nominatim

# library for encrypting string
from cryptography.fernet import Fernet

# importing functions
from fourWordsAlgo import getFourWords, decode

# Imports for PlusCodeApi
import requests
import json


# Global Variables
GENERATED = False
VERIFIED = False




app = Flask(__name__,template_folder='template',static_folder='static')
key = Fernet.generate_key()

# function to encrypt string
def encryptMessage(message):
    # generate a key for encryption and decryption
    # You can use fernet to generate
    # the key or use random key generator
    # here I'm using fernet to generate key

    global key

    # Instance the Fernet class with the key

    fernet = Fernet(key)

    # then use the Fernet class instance
    # to encrypt the string string must
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())

    return encMessage.decode()


# function to decrypt string
def decryptMessage(message):
    # generate a key for encryption and decryption
    # You can use fernet to generate
    # the key or use random key generator
    # here I'm using fernet to generate key

    global key

    # Instance the Fernet class with the key

    fernet = Fernet(key)

    # decrypt the encrypted string with the
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methods
    decMessage = fernet.decrypt(message).decode()

    return decMessage

# Function which takes Address and Gives Coordinates

def findcoordinates(address):

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(address)
    # print(getLoc.address)
    # print("Latitude = ", getLoc.latitude, "\n")
    # print("Longitude = ", getLoc.longitude)

    return getLoc.address,getLoc.latitude,getLoc.longitude

# Function to find plus code using Coordinates

def findpluscode(lat,long):
    s1 = str(lat) + ',' +str(long)
    parameters = {
        # 'address' : '19.108914019118583, 72.86535472954193'
        'address' : str(s1)
    }
    response = requests.get("https://plus.codes/api", params=parameters)
    r = json.loads(response.text)
    return r['plus_code']['global_code']


# Function to find Address using Coordinates

def findaddressusingcoordinates(lat,long):
    s1 = str(lat) + ',' + str(long)
    geoLoc = Nominatim(user_agent="GetLoc")
    locname = geoLoc.reverse(s1)
    return str(locname.address)






@app.route("/")
def LandingPage():
    return render_template('LandingPage.html')


@app.route("/main")
def Main():
    return render_template('MainPage.html', generated = GENERATED)


@app.route("/about")
def AboutPage():
    return render_template('About.html')


@app.route("/generate", methods=['GET', 'POST'])
def GenerateCode():
    global GENERATED

    if request.method == "POST":
        GENERATED = True
        flat_building = str(request.form['flat_building'])
        street = str(request.form['street'])
        city = str(request.form['city'])
        state = str(request.form['state'])
        country = str(request.form['country'])
        pincode = str(request.form['pincode'])

        # print(flat_building)
        # print(street)
        # print(city)
        # print(state)
        # print(country)
        # print(pincode)

        # This Address dosent contain flat and Building
        address = str(street + ',' + city + ',' + country + ',' + pincode)
        print(address)

        a,b,c = findcoordinates(address)
        print(a,b,c)

        # encode a given string
        encodedString = encryptMessage(flat_building)

        getWords = getFourWords(float(b),float(c))

        newList = getWords + " " + encodedString
        newList = newList.split(' ')

        print(newList)

        flat_Area = decryptMessage(encodedString.encode())
        print(flat_Area)

        pluscode = findpluscode(float(b),float(c))

        return render_template('GenerateCode.html', generated = GENERATED, global_address = a, latitude_generated = b, longitude_generated = c, plus_code = pluscode)

    GENERATED = False
    return render_template('GenerateCode.html', generated = GENERATED)


@app.route("/verify", methods=['GET', 'POST'])
def Verify():
    global VERIFIED

    if request.method == "POST":
        VERIFIED = True
        latitude = str(request.form['lat'])
        longitude = str(request.form['long'])
        # IDAC = str(request.form['IDAC'])
        globaladdress = findaddressusingcoordinates(latitude,longitude)
        pluscode = findpluscode(latitude,longitude)
        return render_template('VerifyCode.html', verified=VERIFIED, global_address=globaladdress, plus_code=pluscode, latitude_generated=latitude,longitude_generated=longitude)

    VERIFIED = False
    return render_template('VerifyCode.html', verified=VERIFIED)


if __name__ == "__main__":
    app.run(debug=True)