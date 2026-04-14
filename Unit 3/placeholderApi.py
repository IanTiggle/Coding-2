import requests



#url = 'https://bored-api.appbrewery.com/random'
#myobj = { "title": "foo", "body": "bar", "userId": 1 }

#response = requests.get(url)


#print(response.text)

#url = 'https://bored-api.appbrewery.com/filter?type=cooking'
#myobj = { "title": "foo", "body": "bar", "userId": 1 }

#response = requests.get(url)


#print(response.text)
def pokedex():
    search = input("would you like to search pokemon, ")
    while search == "y":
        pokename = input("please enter a pokemon name, ")
        url = f'https://pokeapi.co/api/v2/pokemon/{pokename}'
        response = requests.get(url)




        if response.status_code == 200:
            data= response.json()

            filtered_data = {
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"], 
                "types": data["types"],
                "abilities": [ability["ability"]["name"] for ability in data["abilities"]]
            }
            print(filtered_data)
            search = input("would you like to find another pokemon?  ")

        else:
            print("data not found")
            print(response.status_code)
pokedex()