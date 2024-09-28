# Tuplas são objetos imutaveis, que uma vez criados não
# não podem ser mudadas, são imutaveis.  E estar entre parenteses
# não é necessário
tupla = 1, 2, 3, 4
# tupla[0] = 3 --> ERRO POIS NÃO É POSSÍVEL ALTERA-LA

tupla2 = 5, 6, 7, 8

print(tupla[2])

# tuplas somam
print(tupla + tupla2)

# for percorre tupla
for i in tupla:
    print(i)

# x = 1, x = 2, x = 3
x, y, z = 1, 2, 3

a, b = input('Digite alguma coisa: ').split()
print(a, b)

lista = ['san', 'nunez', 1.7, True]
for i, j in enumerate(lista):
    print(f'index: {i} e valor {j}')

