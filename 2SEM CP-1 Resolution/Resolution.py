def f(x):
    if x < - 2:
        return x**2 + 3*x -4
    elif x < 0:
        return 2*x + 5
    elif x < 4:
        return x**(1/2)
    elif x < 6:
        return x**3 - 3*x**2 - 10*x
    elif x < 8:
        return 3*x**2 - 4*x - 20
    else:
        return 10

def le_matriz(l, c):
    matriz = []
    for j in range(l):
        linha = []
        for i in range(c):
            linha.append(int(input(f'Matriz[{j}][{i}]: ')))
        matriz.append(linha)
    return matriz

def tam(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    return[linhas, colunas]

def subtracao(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0])
        c = []
        for j in range(len(a)):
            linha = []
            for i range(len(a[0])):
                linha.append(a[0][i] - b[0][i])
            c.append(linha)
    elif
        print("Matrizes de proporções diferentes!")
    return c

a = [
    [1,2,3],
    [5,8,10]
]

def transposta(a)

    trans = []
    for j in range(len(a[0])):
        linha = []
        for i in range(len(a)):
            linha.append(a[j][i])
        trans.append(linha)
    return trans