import requests
import pprint

#url = 'https://pokeapi.co/api/v2/pokemon/{}/{}/'.format(name, move)

url = 'https://pokeapi.co/api/v2/pokemon/'
params = {'name': '', 'move': ''}

pokemon_ID = ['2', '6', '7', '8', '5', '3']

for pokemon in pokemon_ID:
   response = requests.get(url, params=params)

   if response.status_code == 200:
       print(response.text)

   else:
       data = response.json()

       for result in data['results']:
           pprint.pprint(result['\nname'])
           pprint.pprint(result.get(['move']))

#   with open('pokemon.txt', 'w+') as pokemon_file:
#       pokemon_file.write(result['name'])
#       pokemon_file.write('\n')
#       pokemon_file.write(result.get(['move']))
