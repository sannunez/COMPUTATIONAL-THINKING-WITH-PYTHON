lista = [1,2,3,50,100]
aux = 50
def busca(lista, aux):
    for i in range(len(lista)):
        if lista[i] == aux:
            return i
    return -1