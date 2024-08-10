notas = [1, 2, 3.1, 'Maria', True, [1, 2]]

for i in notas:
        print(f"{i} é {type(i)}")

# [:] --> faz uma cópia da lista
lista = notas[:]

notas[0] = 180
print(lista)
print(notas)


print(lista[-1])
print(notas[-1][0])

lista.append(3)
print(lista)

lista.remove(3)
print(lista)