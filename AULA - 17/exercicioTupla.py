# CRIE UMA FORMA DE ADICIONAR ITENS E REMOVER ITENS DE UMA TUPLA
tuplaOriginal = 1, 2, 3
a = input(":")
a = tuple([a])

tuplaOriginal += a
print(tuplaOriginal)


tupla1 = (1,2,3,4,5)
rem = 4
tupla1 = list(tupla1)

for i, j in enumerate(tupla1):
    if j == rem:
        tupla1.pop(i)
print(tuple(tupla1))