def numAmigo(a,b):
    n=1
    soma1=0
    while a>n:    
        if (a%n)==0:
            soma1 = soma1 + n
            n = n + 1
        else:
            n = n+1
    print(soma1)
    m=1
    soma2 = 0
    while b>m:    
        if (b%m)==0:
            soma2 = soma2 + m
            m = m + 1
        else:
            m = m + 1
    print(soma2)
    if soma1 == b and soma2==a:
        return(True)
    else:
        return(False)
    

print(numAmigo(220,284))