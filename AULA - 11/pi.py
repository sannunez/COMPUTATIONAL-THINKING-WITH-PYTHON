# n=0
# pi = 0
# while n<=100:
#     ha = 2*(3**0.5)*((-1)**n)/(3**n*(2*n+1))
#     n = n + 1
#     pi = pi + ha
# print(pi)

# SENo
def fat(n):
    fat = 1
    for i in range (1, n+1):
        fat = fat * i
    return fat

def pi(loop):
    sum = 0
    for n in range(loop):
        sum = sum + 2*3**(0.5)*(-1)**n/(3**n*(2*n+1))
    return sum

print(pi(100))

def sin(x, loop):
    sum = 0
    for n in range(loop):
        sum += (-1)**n*x**(2*n+1) / fat(2*n+1)
    return sum

def cos(x, loop):
    sum = 0
    for n in range(loop):
        sum += (-1)**n*x**(2*n) / fat(2*n)
    return sum

def tan(x, loop):
    return sin(x , loop) / cos(x, loop)

print(tan(pi(50)/4, 50))
