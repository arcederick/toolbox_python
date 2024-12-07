import math

class CalculadoraCientifica:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            return "Erro: divisão por zero"
        return a / b

    def potencia(self, base, expoente):
        return base ** expoente

    def raiz_quadrada(self, numero):
        if numero < 0:
            return "Erro: não é possível calcular a raiz quadrada de um número negativo"
        return math.sqrt(numero)

calculadora = CalculadoraCientifica()

while True:
    print("Calculadora Científica")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Sair")

    escolha = input("Escolha uma operação (1-7): ")

    if escolha == "1":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = calculadora.soma(a, b)
        print(f"Resultado: {resultado}")
    elif escolha == "2":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = calculadora.subtracao(a, b)
        print(f"Resultado: {resultado}")
    elif escolha == "3":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = calculadora.multiplicacao(a, b)
        print(f"Resultado: {resultado}")
    elif escolha == "4":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = calculadora.divisao(a, b)
        print(f"Resultado: {resultado}")
    elif escolha == "5":
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        resultado = calculadora.potencia(base, expoente)
        print(f"Resultado: {resultado}")
    elif escolha == "6":
        numero = float(input("Digite o número para calcular a raiz quadrada: "))
        resultado = calculadora.raiz_quadrada(numero)
        print(f"Resultado: {resultado}")
    elif escolha == "7":
        break
    else:
        print("Opção inválida. Tente novamente.")