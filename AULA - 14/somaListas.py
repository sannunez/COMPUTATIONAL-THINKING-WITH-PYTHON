lista1 = [4, 8, 3, 45, 2]
lista2 = [9, 7, 2,  3, 5]
# x = 0 
# a = 0
# somaEMulti = 0
# while x < len(lista1):
#     somaEMulti = somaEMulti + ((lista1[a])*(lista2[a]))
#     a = a + 1
#     x = x + 1
# print(somaEMulti)

def listasFunc(v, w):
    x = 0
    a = 0
    somaEMulti = 0
    if len(v) != len(w):
        return None
    else:
        while x < len(v):
            somaEMulti = somaEMulti + ((v[a])*(w[a]))
            print(f"i = {v[a]} * {w[a]} = {(v[a])*(w[a])}")
            a = a + 1
            x = x + 1
    print(somaEMulti)

listasFunc(lista1, lista2)