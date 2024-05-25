musica = '''O SAPO NAO LAVA O PE
NAO LAVA POR QUE NAO QUER
ELE MORA LA NA LAGOA
NAO LAVA O PE PORQUE NAO QUER 
MAS QUE CHULE'''

mus = list(musica)
texto_final = ""
vogal = "A"

for i in range(len(mus)):
    if mus[i] == 'A' or mus[i]== 'E' or mus[i] == 'I' or mus[i] == 'O' or mus[i]=='U':
        texto_final = texto_final + vogal
    else:
        texto_final = texto_final + mus[i]
print(texto_final)