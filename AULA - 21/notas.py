import pickle

arquivo1 = open('notas.txt', 'r')

arq = arquivo1.read()
b = arq.split('\n')

def media_alunos(d):
    c = d.split(' ')
    nome = c[0]
    media = 0

    for i in c[1: ]:
        media += int(i) / len(c[1: ])

    return nome, media

print(media_alunos(b[0]))

dicio = {}
for j in b:
    nome = (media_alunos(j)[0])
    media = (media_alunos(j)[1])
    dicio[nome] = media

print(dicio)

arquivo2 = open('notas.bin', 'wb')
pickle.dump(dicio, arquivo2)

arquivo1.close()
arquivo2.close()