a = [7,3,4,6,5,2]
print(a)

for iteracao in range (len(a) -1, 0, -1):
    for i in range (iteracao    ):
        if a[i] > a[i + 1]:
            aux = a[i]
            a[i] = a[i +1]
            a[i+1] = aux
    print(a)