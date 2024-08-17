# Diferentes métodos para resolução de uma mesma questão
# Soma de todos os itens dentro de uma lista

# Metodo 1
def soma(*params):
    adicao = sum(params)
    print(adicao)

soma(1, 2, 3)

# Metodo 2
def soma2(*params):
    x = 0
    adicao = 0
    for i in params:
        adicao = adicao + params[x]
        x = x + 1
    print(adicao)

soma2(1, 2, 3, 5, 8)

# Metodo 3
l = [1, 10, 20, 45]
res = 0
for i in l:
    res = res + i
print(res)

# Peça ao usuario para digitar a qtde de parametros que ele quer somar, os valores
# a serem somados e realize a soma

qtd = int(input("Digite quantos parâmetros você quer somar: "))
x = qtd
somatorio = 0
while 0 < x <= qtd:
    valor = float(input("Digite o valor: "))
    somatorio = somatorio + valor
    x = x - 1
print(somatorio)


