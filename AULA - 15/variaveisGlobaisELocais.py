def f1(a):
    print(a+x)

def f2(a):
    global x
    x = x + 1
    print(x+1)

x = 4
f1(3)
f2(3)
print(x)
