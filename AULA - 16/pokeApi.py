# OBJETIVO: chamar o id e o tipo do pokemon

import requests

pokemon = input("Digite o pokemon desejado: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

r = requests.get(url)
# print(r)
# print(r.text)
# print(r.json())

armazenaPokemon = r.json()
print(armazenaPokemon['id'])
print(armazenaPokemon['types'][0]['type']['name'])


# TRANSFORMAR EM FUNÇÃO:
def poke(pokemon):
        url = f'"https://pokeapi.co/api/v2/pokemon/{pokemon}'
        r = reqiests.get(url)
        var = r.json