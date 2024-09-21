import requests

# url = 'https://viacep.com.br/ws/37044150/json/'

# # PUXANDO JSON DO VIACEP
# r = requests.get(url)
# cep = r.json()
# print(type(cep))
# print(cep['bairro'])

#faça um exercicio que o usuario vai digitar o cep dele para entrega e o programa ira escrever em tela a rua, bairro, e  cidade da entrega

# def correio(endereco):
#     url = f'https://viacep.com.br/ws/{endereco}/json/'
#     r = requests.get(url)
#     cep = r.json()

#     return f'''
#     Rua:{cep['logradouro']}
#     Bairro:{cep['bairro']}
#     Cidade:{cep['localidade']}
#     '''

# print(correio('37044150'))

url = f'https://apis.codante.io/olympic-games/countries'
país = 'China'
r = requests.get(url)
info = r.json()
# print(info['data'])
for i in info['data']:
    if i['name'] == pais:
        print(i['gold_medals'])
        print(i['silver_medals'])
        print(i['bronze_medals'])
       