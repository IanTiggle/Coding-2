import requests

# Coordinates for New York City (Look up philly lat/long)
lat = 39.96
lon = 75.22

# no "apikey"
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

print (data)