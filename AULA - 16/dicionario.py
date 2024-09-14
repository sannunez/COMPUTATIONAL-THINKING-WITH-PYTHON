dicA = {
    'Nome': 'Helder',
    'Idade': 33
}

dicB = {
    'Propriedade':'Janela',
    'Ar': True
}


print(dic.values())
print(dic.keys())
print(dic.items())
print(dic.pop('Carro')) #remove
print(dic)

for i in dic.values():
    print(i)

dicA.update(dicB)
print(dicA)
print(dicB)
