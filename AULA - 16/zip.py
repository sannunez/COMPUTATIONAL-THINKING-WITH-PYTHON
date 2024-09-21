nomes = ["Joao", 'Henrique', 'Julia']
idade = [10, 11, 12]
# criou um dicionario que atribui o primeiro como chave e atribui o segundo no primeiro como item
print(dict(zip(nomes,idade)))

#Exercício:
#{'Alice':[20, 'F]}, 'Beatriz': [18, F], 'Carlos': [19, 'M']}

cont = True
dictio = {}
while cont == True: 
    dictio[str(input('Digite o nome: '))] = [int(input('Adicionar idade:')), str(input('Adicionar gênero(M/F): '))]
    continuar = str(input('Digite "S" para adicionar novos usuários, "N" para terminar operações: '))
    if continuar == "N":
        cont = False
    
    else:
        continue
print(dictio)
