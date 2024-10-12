estoque_atual = {'camisa': 5, 'calça': 3, 'sapato':2}
novos_itens = {'camisa': 2, 'calça': 1, 'bone':4}

def atual_estoque(estoque_atual, novos_itens)
    for i in novos_itens.keyys():
        if i in estoque_atual:
            estoque_atual[i] += novos_itens[i]
        else:
            estoque_atual[i] = novos_itens
    return estoque_atual
