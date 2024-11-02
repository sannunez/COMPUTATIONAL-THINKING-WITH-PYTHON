arquivo = open('notamaxhelder.txt', 'r')

arq = arquivo.read()
b = arq.split('\n')

def nome_notas(d):
    c = d.split(' ')
    nome = c[0]
    maior = 0
    menor = 10

    # c[1:] analisa a lista a partir do elemento 1
    for i in c[1:]:
        if int(i) > maior:
            maior = int(i)
        if int(i) < menor:
            menor = int(i)
    return nome, maior, menor

for j in b:
    print(nome_notas(j))

arquivo.close()