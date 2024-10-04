# # Exercícios
# 1.	Escreva uma função que receba uma lista de strings como argumento e retorne um dicionário onde
# as chaves sejam as palavras e os valores sejam o número de vezes que essas palavras aparecem na lista.
# Exemplo de entrada:
# palavras = ["casa", "carro", "casa", "bicicleta", "carro", "carro", "bicicleta"]
# Exemplo de saída:
# {"casa": 2, "carro": 3, "bicicleta": 2}

# palavras = ["casa", "carro", "casa", "bicicleta", "carro", "carro", "bicicleta"]
# dict = {}

# for i in palavras:

palavras = ["casa", "carro", "casa", "bicicleta", "carro", "carro", "bicicleta"]
dicio = {}
def palavras(list):
    for i in palavras:
        if i in dicio:
            dicio[i] = dicio[i] + 1
        else:
            dicio[i] = 1
    return(dicio)





# 2.	Dada a tupla pessoas = (("João", 19), ("Maria", 21), ("Pedro", 20), ("Ana", 18)),
#  escreva uma função que receba uma tupla semelhante a pessoas e retorne uma nova tupla 
# contendo apenas as pessoas que são maiores de idade (idade ≥ 18).

pessoas = (("João", 19), ("Maria", 21), ("Pedro", 20), ("Ana", 18), ("Pedro", 12))
print(pessoas[0][1])
def maiorDeDezoito(tuple):
    lista = list(tuple)
    pessoasLista = []
    for i in lista:
        if i[1] >=18 :
            pessoasLista.append(i)
    return pessoasLista

print(maiorDeDezoito(pessoas))   

# 3.	Implemente uma função que receba uma lista de números inteiros e
#  ordene essa lista utilizando o algoritmo de Bubble Sort.

bubbleLista = [12, 7, 3, 2, 15]

def bubbleSort(lista):
    for iteracao in range(len(lista) - 1, 0, -1):
        for  i in range(iteracao):
            if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista
print(bubbleSort(bubbleLista))

# 4.	Escreva uma função que receba uma lista de tuplas, onde cada tupla contém dois números inteiros. 
# A função deve retornar uma lista contendo a soma de cada par de números nas tuplas.
# Exemplo de entrada:
# pares = [(1, 2), (3, 4), (5, 6)]
# Exemplo de saída:
# [3, 7, 11]
pares = [(1, 2), (3, 4), (5, 6)]

def somaDePares(lista):
    listupla = []
    for i in pares:
        listupla.append(i[0] + i[1])
    return listupla

print(somaDePares(pares))


# 5.	Escreva uma função que receba uma lista de nomes de alunos e uma lista correspondente de notas. 
# A função deve retornar um dicionário onde as chaves são os nomes dos alunos e os valores são suas respectivas notas.
# Exemplo de entrada:
# alunos = ["Ana", "Bruno", "Carlos", "Diana"]
# notas = [85, 90, 78, 92]
# Exemplo de saída:
# {"Ana": 85, "Bruno": 90, "Carlos": 78, "Diana": 92}
alunos = ["Ana", "Bruno", "Carlos", "Diana"]
notas = [85, 90, 78, 92]

def teste(lista1, lista2):
    school = []
    if len(lista1) != len(lista2):
        print("ERRO: listas de tamanhos diferentes!")
    else:
        school = dict(zip(lista1, lista2))
    return school

print(teste(alunos, notas))

# 6.	Imagine que você tem um dicionário que armazena o saldo de várias contas bancárias. 
# Escreva uma função que receba o dicionário de contas 
# e um segundo dicionário contendo valores a serem creditados ou debitados das respectivas contas. 
# A função deve atualizar o saldo das contas existentes e criar novas entradas para contas que ainda não existem.
# Exemplo de entrada:
# saldos = {"Conta A": 1000, "Conta B": 1500}
# movimentacoes = {"Conta A": -200, "Conta C": 500}
# Exemplo de saída:
# {"Conta A": 800, "Conta B": 1500, "Conta C": 500}

saldos = {"Conta A": 1000, "Conta B": 1500}
movimentacoes = {"Conta A": -200, "Conta C": 500}

for i in movimentacoes:
    if not i in saldos:
        saldos[i] = movimentacoes[i]
    else:
        saldos[i] = saldos[i] + movimentacoes[i]
    print(saldos) 


# 7.	Escreva uma função que receba uma lista de palavras e ordene-a em ordem alfabética utilizando o algoritmo Bubble Sort.
# Exemplo de entrada:
# palavras = ["banana", "maçã", "laranja", "uva", "abacaxi"]
# Exemplo de saída:
# ["abacaxi", "banana", "laranja", "maçã", "uva"]

frutas = ["banana", "maçã", "laranja", "uva", "abacaxi"]

def bubbleFrutas(lista):
    for iteracao in range(len(lista) - 1, 0, -1):
        for  i in range(iteracao):
            if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista
print(bubbleFrutas(frutas))
print(sorted(frutas))

# 8.	Escreva uma função que receba um dicionário com o nome de produtos e seus respectivos preços, e um valor limite. A função deve retornar um novo dicionário contendo apenas os produtos cujo preço seja maior que o limite fornecido.
# Exemplo de entrada:
# produtos = {"banana": 2.50, "maçã": 3.20, "laranja": 1.80}
# limite = 2.00
# Exemplo de saída:
# {"banana": 2.50, "maçã": 3.20}

# 9.	Sabe-se que uma molécula de RNA mensageiro é utilizada como base para sintetizar proteínas, no processo denominado de tradução. Cada trinca de bases de RNA mensageiro está relacionada com um aminoácido. Combinando vários aminoácidos, temos uma proteína. Com base na tabela (simplificada) de trincas de RNA abaixo, crie uma função que receba uma string representando uma molécula de RNA mensageiro válida, segundo essa tabela, e retorne a cadeia de aminoácidos que representam a proteína correspondente.
# Trinca de RNA	Nome do Aminoácido
# UUU	Phe
# CUU	Leu
# UUA	Leu
# AAG	Lisina
# UCU	Ser
# UAU	Tyr
# CAA	Gln 


# Exemplo: traducao_rnaM(“UUUUUAUCU”) retorna “Phe-Leu-Ser”


