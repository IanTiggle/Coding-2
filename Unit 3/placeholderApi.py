import requests



#url = 'https://bored-api.appbrewery.com/random'
#myobj = { "title": "foo", "body": "bar", "userId": 1 }

#response = requests.get(url)


#print(response.text)

#url = 'https://bored-api.appbrewery.com/filter?type=cooking'
#myobj = { "title": "foo", "body": "bar", "userId": 1 }

#response = requests.get(url)


#print(response.text)


url = 'https://pokeapi.co/api/v2/berry-firmness/2/'
myobj = { "title": "foo", "body": "bar", "userId": 1 }

response = requests.get(url)


print(response.text)