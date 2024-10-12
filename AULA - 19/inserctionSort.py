lista = [10, 12, 41, 68, 95, 21]
# lista.sort()
# print(lista)
for i in range(len(lista)):
    aux = lista[i] #=21
    j = i-1

    while j >= 0 and lista[j] > aux:
        lista[j+1] = lista[j]
        j = j - 1 

    lista[j+1] = aux 
    print(lista)