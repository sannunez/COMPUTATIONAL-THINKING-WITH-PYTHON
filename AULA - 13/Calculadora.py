import funcCalcMultiEDiv
import funcCalcSomaESub

def calculadora():
    while True:
        operacao = str(input('''Que tipo de operação você deseja fazer?
                        Envie: 
                        "+" para Soma
                        "-" para Subtração
                        "*" para Multiplicação
                        "/" para Divisão
                        Escreva aqui: '''))
        if operacao == "+":
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            print(funcCalcSomaESub.soma(a, b))
            break
        elif operacao == "-":
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            print(funcCalcSomaESub.sub(a, b))
            break
        elif operacao == "*":
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            print(funcCalcMultiEDiv.multi(a, b))
            break
        elif operacao == "/":
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            print(funcCalcMultiEDiv.div(a, b))
            break
        else:
            print("Digite um operador valido!")


calculadora()