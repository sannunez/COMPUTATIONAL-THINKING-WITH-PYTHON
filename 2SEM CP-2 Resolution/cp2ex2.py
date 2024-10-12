equipes = [('Equipe A', 85),('Equipe B', 90),('Equipe C', 80),('Equipe D', 95),('Equipe E', 88)]
print(equipes)

def organizaEquipe(equipes)
    for iterador in range(len(equipes) - 1, 0, -1):
        for i in range(iterador):
            if equipes[i][1] > equipes[i+1][1]:
                equipes[i], equipes[i+1] =  equipes[i+1], equipes[i]
print(equipes)