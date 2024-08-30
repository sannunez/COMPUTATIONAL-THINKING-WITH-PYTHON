c = int(input("qtdeI?")) 
l = int(input("qtdeJ?"))

def criaMatriz(c, l):
    matriz = []
    for j in range(l):
        linha = []
        for i in range(c):
            linha.append(int(input(':')))
        matriz.append(linha)
    print(matriz)

criaMatriz(c, l)