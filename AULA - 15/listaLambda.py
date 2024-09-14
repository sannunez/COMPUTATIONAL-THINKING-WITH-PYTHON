linha = 3
coluna = 2
# criação matriz usando função lambda recebendo input do usuário
matriz = lambda linha, coluna: [[int(input(";")) for i in range(coluna)] for i in range (linha)]
print(matriz(3,2))