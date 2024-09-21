lista_compras = 'biscoito', 'chocolate', 'farinha', 'arroz', 'uranio', 'cafe'

supermercado = {
    'amaciante':4.99,
    'arroz': 10.90,
    'biscoito': 1.69,
    'cafe' : 6.98,
    'chocolate' : 3.79,
    'farinha' : 2.99
}

def compras(lista_compras):
    valor = 0
    for i in lista_compras:
        if i in supermercado:
            valor = valor + supermercado[i]
        else:
            pass
    return valor

print(compras(lista_compras))