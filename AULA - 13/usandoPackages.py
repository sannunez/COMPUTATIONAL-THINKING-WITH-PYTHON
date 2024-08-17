import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 3, 4, 5, 6]

plt.plot(x, y, marker = 'o', linestyle = 'dotted')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('Título do meu gráfico')
plt.grid(True)
plt.show()


def y(x):
    if x <= 2:
        return x
    elif x <= 3.5:
        return 2
    elif x < 5:
        return 3
    else:
        return x**2 - 10*x + 28