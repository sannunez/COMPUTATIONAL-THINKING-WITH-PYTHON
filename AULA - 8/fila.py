# a = input("Digite SIM para adicionar elementos a fila: ").upper()
# fila = []

# while a == "SIM":
#     elemento = input("Nome: ")
#     fila.append(elemento)
#     a = input("Digite SIM para adicionar elementos a fila: ").upper()
# for elemento in fila:
#     próximo = fila.pop()
#     print()
#     print()
#     print(f"Proximo da fila: {próximo}")
#     print()
#     print(fila)
#     print()
#     a = input("Digite SIM para adicionar elementos a fila: ").upper()
# print(f"Proximo da fila: {próximo}")

fila= []
while True:
    acao = input("Digite A para adicionar na fila ou R para remover da fila: ").upper()
    if acao == "A":
        nome = input("Digite o nome da pessoa: ")
        fila.append(nome)
    elif acao == "R":
        rem = fila.pop(0)
        print(f"{rem} foi atendido!")
        print(f"O tamanho da fila é de {len(fila)} pessoas. ").upper()

    else:
        print("Comando inválido!")

    print(fila)
    enc = input("Deseja encerrar a fila? (S para encerrrar): ").upper()
    if enc=="S":
        break
print(fila)