
# rb = leitura binaria
# wb = escrita binaria
# r+b = leitura e escrita binaria

# import pickle traz a biblioteca que permite manipular arquivos binarios
# pickle.dump(objeto, arquivo) escreve no arquivo
# pickle.load(arquivo) lê o arquivo

import pickle 
arquivo = open('aula.bin', 'wb')

lista = [5, 10, 'olá', 10.5]

pickle.dump(lista, arquivo)