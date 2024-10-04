lista = [7, 5, 10, 6, 8]

for iteracao in range(len(lista)-1,0,-1):
    for i in range(iteracao):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
        else:
            print(i)

print(lista)

# def bubbleSort(lista):
#     for iteracao in range(len(lista)-1, 0, -1):
#         for i in range(iteracao):
#             if lista[i] > lista[i+1]:
#                 lista[i], lista[i+1] = lista[i+1], lista[i]
#     return lista

# print(bubbleSort(lista))