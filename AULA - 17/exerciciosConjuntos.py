# Exercício: Escreva um programa que cmopare duas listas. Utilizando operações
# de conjuntos, imprima:

lista1 = [1,2,3,4,5,6]
lista2 = [4,5,6,7,8,9]

# 1) imprima os valores comuns às duas listas
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = conjunto1 & conjunto2
lista3 = list(conjunto3)
print(lista3)

# Os valores que só existem na primeira
valorUnico1 = conjunto1 - conjunto2
set(valorUnico1)
print(valorUnico1)

# Os valores que só existem na segunda
valorUnico2 = conjunto2 - conjunto1
print(valorUnico2)

# Uma lista com os elementos não repetidos das duas
valoresUnicos = (conjunto1 - conjunto2) | (conjunto2 - conjunto1)
valoresUnicos = list(valoresUnicos)
print(valoresUnicos)