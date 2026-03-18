# api = Application Programming Interface

# are methods (funtions) that allow computer programs to share
# data between each other over the internet/ a network

import requests
# modules are files of code (objects with methods and parameters)
# with prewritten code to help us program

countryData = requests.get("https://restcountries.com/v3.1/all?fields=name,capital").json()

# JSON - JavaScript Object Notation
# this a object structured for computers and peopleto easily read
# and sort data

print(countryData.json())

southAmericaCountry = requests.get("https://restcountries.com/v3.1/region/south%20america?fields=name,capital").json()
print(southAmericaCountry)