n = int(input('Digite a qtde de elementos: '))
lista = []
for i in range(n):
    lista.append(float(input('Digite o elemento: ')))
print(lista)
print(sum(lista))
soma = sum(lista)
media = soma//n
print(media)