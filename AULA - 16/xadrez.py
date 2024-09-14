import matplotlib.pyplot as plt

# linha = 8
# coluna = 8

# xadrez = [[[255*((i+j)%2),255*((i+j)%2),255*((i+j)%2)]for i in range(coluna)] for j in range(linha)]
# plt.imshow(xadrez)
# plt.axis('off')
# plt.show()
# print(xadrez)

linha = 8
coluna = 8
cond = True
matriz = []
for j in range (linha):
    linha = []
    for i in range(coluna):
        cor = []
        for k in range(3):
            if cond:
                elemento = 0
            else:
                elemento = 255
            cor.append(elemento)
        cond = not cond
        linha.append(cor)
    cond = not cond
    matriz.append(linha)
print(matriz)

plt.imshow(matriz)
plt.axis('off')
plt.show()