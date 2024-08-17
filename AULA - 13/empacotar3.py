# Peça ao usuario para digitar a qtde de parametros que ele quer somar, os valores
# a serem somados e realize a soma

def soma(*params):
    x = 0
    adicao = 0
    for i in params:
        adicao = adicao + params[x]
        x = x + 1
    print(adicao)

qtd = int(input("Digite a qtde de valores que deseja somar: "))
valores = []
for i in range(qtd):
    valores.append(float(input("Digite o valor: ")))
print(soma(*valores))