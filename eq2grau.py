#Façam uma função que retorne as raízes de uma #equação de segundo grau:
#equação de segundo de grau:
# ax² + bx + c = 0
#Em que os parametros de entrada da função são: a,b,c

def raiz(a, b, c):
    delta = b**2 -4*a*c
    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)
    
    return x1, x2
print(raiz(2, -3, 1))