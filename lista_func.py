#faça um programa que dado duas listas de mesmo tamanho
# retorne a soma elemento a elemento das listas

def somaLista(a, b):
    c=[]
    for elemento in len(a):
       c.append(a[elemento]+b[elemento])
    return c
             


soma = somaLista([1,2,3], [1,2,3])
print(soma)