# qtd = 100000
# pi = 0

# for i in range(qtd):
#     termo = (-1)**i/(2*i+1)
#     pi = pi + termo
# print(pi*4)


# l = 3
# c = 2
# matriz = []
# x = 1

# for i in range(l):
#     linha = []
#     for j in range(c):
#         linha.append(x)
#         x = x + 1       
#     matriz.append(linha)
# print(matriz)

# for column in matriz:
#     for i in column:
#         print(f"{i:.1f}", end=' ')
#     print()



# A = [[1, 2], [3, 4]]
# B = [list(linha) for linha in A]
# B[0][0] = 0
# print(A)
# # [[1, 2], [3, 4]]
# print(B)
# # [[0, 2], [3, 4]]



matriz = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]

]

for j in matriz:
    for i in j:
        if (float(i) % 2) == 0:
            print(f"{i} ", end=" ")
    print()


