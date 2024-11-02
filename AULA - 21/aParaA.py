arquivo = open("aParaA.txt", 'r+')

texto = ''

while True:
    carac = arquivo.read(1)
    if carac == 'a':
        texto += 'A'
    else:
        texto += carac
    if carac == '':
        break

arquivo.seek(0,0)
arquivo.write(texto)
print(texto)
arquivo.close