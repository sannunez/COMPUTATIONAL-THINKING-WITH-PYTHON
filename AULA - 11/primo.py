n = int(input("n: "))
i = 2
var = True
while i < n:
    if n % i == 0:
        var = False
        break 
    i = i+1


if var == True:
    print("é primo")
if var == False:
    print("não é primo")