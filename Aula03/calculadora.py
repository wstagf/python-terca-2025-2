# o nosso professor pediu uma calculadora em python com 
# soma, subtracao, divisao, multiplicacao

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisao por zero"
    return a / b

def main():
    print("Calculadora Simples")
    print("Escolha a operacao:")
    print("1. Soma")
    print("2. Subtracao")
    print("3. Multiplicacao")
    print("4. Divisao")

    escolha = input("Digite a opcao (1/2/3/4): ")

    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    if escolha == '1':
        print(f"{num1} + {num2} = {soma(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtracao(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("Opcao invalida")

if __name__ == "__main__":
    main()