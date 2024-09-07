a = [
    [0,0,0],
    [0,1,1],
    [2,3,4]
]


qtdeZeros = []
difZero = []
for l in range(len(a)):
    for c in a[l]:
        if c == 0:
            qtdeZeros.append(0)
        else:
            difZero.append(1)


print(qtdeZeros)
print(difZero)

if len(qtdeZeros) > len(difZero):
    print("Matriz Esparsa")
elif len(qtdeZeros) <= len(difZero):
    print("Matriz Comum")


   
        