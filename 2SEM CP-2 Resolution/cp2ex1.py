lista_de_compras = 'biscoito', 'chocolate', 'farinha', 'ovo'
supermercado = {
    'amaciante': 4.99,
    'arroz': 10.90,
    'biscoito':1.69,
    'chocolate' 3.79,
    'farinha'
}

    def compras(lista_de_compras, supermercado):
    valor = 0
    tem = []
    ntem = []
    for i in lista_de_compras:
        if i in supermercado:
            valor += supermercado[i]
            tem.append(i)
        else:
            ntem.append(i)
    return valor,tem, ntem

    print(compras(lista_de_compras, supermercado))