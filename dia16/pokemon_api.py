import requests

pokemon = str(input(" digite o pokemon"))
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

req = requests.get(url)

pokemon =req.json()

print(f"id é {pokemon['id']} e o tipo dele é {pokemon['types'][0]['type']['name']} ")



