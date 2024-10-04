dict = {}

dict[input("Digite a chave:")] = input("Digite os valores desta chave: ")
print(dict) 

dict['casa'] = 'teste'
print(dict)

dict.pop('casa')
print(dict)