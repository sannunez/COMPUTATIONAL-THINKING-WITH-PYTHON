n = int(input("Digite o número de linhas: "))
arvore = "*"
espaco = " " * n
if n > 0:
    while n > 0:
        espaco = " " * (n - 1)
        print(f"{espaco + arvore}")
        arvore = arvore + "**"
        n = n - 1
        
# b = 3
# for i in range(b):
#     print(f"{'*'*(2*i+1):{2*n-1}s}")
        