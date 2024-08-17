import funcoesByHelder1
import funcoesByHelder2

o = input('Digite +, -, *, / para a operação desejada: ')
val = []

while True:
    num = input('Digite o valor ou s para finalizar a operação')
    if num != 's':
        val.append(float(num))
    else:
        break

if o == '+':
    resultado = funcoesByHelder1.soma(*val)
elif o == '-':
    resultado = funcoesByHelder1.sub(*val)
elif o == '*':
    resultado = funcoesByHelder2.mult(*val)
elif o == '/':
    resultado = funcoesByHelder2.div(*val)
else:
    print('Operação Invalida')

print(f'O resultado da {o} é {resultado}')
