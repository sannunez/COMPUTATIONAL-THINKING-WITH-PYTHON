arquivo = open("teste.txt", 'r')
# criará novo arquivo
arquivo2 = open("teste123.txt", 'w')

a = arquivo.readline()
b = arquivo.readline()
c = arquivo.readline()

# volta para o começo do arquivo
arquivo.seek(0,0)

# Escrever no arquivo
arquivo2.write('escrevendo...')

print(f'a={a}')
print(f'b={b}')
print(f'c={c}')

arquivo.close()