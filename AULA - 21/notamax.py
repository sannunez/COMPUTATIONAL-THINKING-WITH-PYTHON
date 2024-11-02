# jose 9 4 6 8 5
# pedro 5 8 3 9
# suzana 8 8 7 4 3 7 4 10 9
# gisela 10 8 10 5 6 10
# joao 8 7 5 6 9

arquivo = open('notamax.txt', 'r+')
carac = 0
notas = []

while True:
    carac = arquivo.read(1)
    if carac == " ":
        carac = arquivo.readline()
        notas.append(carac)
    if carac == '':
        break
    
print(notas)
    
