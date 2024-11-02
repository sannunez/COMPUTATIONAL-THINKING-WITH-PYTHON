import pickle

arquivo = open('aula.bin', 'rb')
a = pickle.load(arquivo)

print(a)