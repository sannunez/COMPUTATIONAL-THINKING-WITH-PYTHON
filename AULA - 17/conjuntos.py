# a = set() #conjunto vazio
# a.add(2) #adiciona elemento
# a.add(2) #não adiciona elementos iguais
# a.add(3)

# print(a)

a = {1,2,3,4,5}
b = {3,4,5,6,7,8}
print(a)
print(b)
# c = a - b --> remove os comuns
# c = a & b --> junta os comuns
# c = a | b --> junta os dois conjuntos não repete os comuns

n = int(input("Quantos números serão lidos? "))
tupla = ()
for i in range(n):
    x = int(input("Entre com um número: "))
    tupla = tupla + (x,)
print(tupla)