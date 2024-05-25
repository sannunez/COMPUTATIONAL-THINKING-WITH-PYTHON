def fat(n):
    fat = 1
    for i in range (1, n+1):
        fat = fat * i
    return fat

print(fat(10))
