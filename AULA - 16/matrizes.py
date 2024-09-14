a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# .copy copia a lista e não se altera caso a original seja alterada;
# lista1 = lista2 a lista esta sujeita as mesmas mudanças de sua semelhante
b = [i[:] for i in a]
print(a)
print(b)
print()
b[0][0] = 3
print(a)
print(b)
