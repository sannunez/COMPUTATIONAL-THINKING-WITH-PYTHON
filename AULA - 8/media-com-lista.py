# Escreva um programa que aceite "n" notas e calcule a média de las, utilize listas.

add = input("Digite 'SIM' para iniciar o cálculo de médias: ").upper()
notas=[]
soma = 0
while add == "SIM":
    addNota = int(input("Digite o valor da nota: "))
    notas.append(addNota)
    soma = soma + addNota
    add = input("Digite 'SIM' para continuar adicionando notas: ").upper()

media = soma/len(notas)
print(f"A média das notas é: {media}")
