from matrizes import *

c = 2
l = 3

# 
matriz = []
for j in range(l):
    linha = []
    for i in range(c):
        linha.append(c * j + i + 1)
        # x = x + 1
    matriz.append(linha)
# print(matriz)

printMatriz(matriz)