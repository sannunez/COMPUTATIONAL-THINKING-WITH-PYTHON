# SEM MATCH CASE
dia = 6
if dia == 1:
    print("domingo")
elif dia == 2:
    print("segunda")
elif dia == 3:
    print("terça")
elif dia == 4:
    print("quarta")
elif dia == 5:
    print("quinta")
elif dia == 6:
    print("sexta")
elif dia == 7:
    print("sabado")

# COM MATCH CASE
day = 15

match day:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabado")
    case _:
        print("dia invalido")