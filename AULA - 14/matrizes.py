obj = [
    [3, 7, 1],
    [0, 9, 2],
    [2, 1, 1]
]
def printMatriz(obj):
    for j in obj:
        for i in j:
            print (f"{i:.1f}", end= '')
        print()
# def printMatrizBonitinha(a):

printMatriz(obj)