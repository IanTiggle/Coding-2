import requests


url = 'https://rickandmortyapi.com/api/character/1,2,3,4'
response = requests.get(url)
print(response)
print(response.json())

if response.status_code == 200:
    data= response.json()

    filtered_data = {
    
        "name": data[1],
        "status": data[1],
        "species": data[1], 
        "type": data[1],
    }
    print(filtered_data)
else:
    print("data not found")


