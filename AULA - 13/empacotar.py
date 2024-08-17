def soma(a, b):
    return a + b

l = [1, 2]
# asterisco desempacota uma lista
resultado = soma(*l) # > l[0], l[1]
print(resultado)