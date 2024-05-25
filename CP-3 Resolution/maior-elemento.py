def maior_elemento(a, b, c):
    if a>b and a > c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    
print(maior_elemento(2, 4, 10))


# def maior_elemento(a, b, c):
#     lista = [a, b, c]
#     return max(lista)

# print(maior_elemento(2, 22, 22))