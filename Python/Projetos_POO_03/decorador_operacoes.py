# Decorador para registrar operações
def registrar_operacao(funcao):
    def wrapper(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        operacao = f"{funcao.__name__}({', '.join(map(str, args))}) = {resultado}"
        with open("registro_operacoes.txt", "a") as arquivo:
            arquivo.write(operacao + "\n")
        return resultado
    return wrapper

# Classe Calculadora
class Calculadora:
    def __init__(self):
        pass

    @registrar_operacao
    def somar(self, a, b):
        return a + b

    @registrar_operacao
    def subtrair(self, a, b):
        return a - b

    @registrar_operacao
    def multiplicar(self, a, b):
        return a * b

    @registrar_operacao
    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a / b

if __name__ == "__main__":
    calculadora = Calculadora()

    resultado_soma = calculadora.somar(5, 3)
    resultado_subtracao = calculadora.subtrair(10, 4)
    resultado_multiplicacao = calculadora.multiplicar(6, 7)
    resultado_divisao = calculadora.dividir(8, 2)

    print("Resultado da Soma:", resultado_soma)
    print("Resultado da Subtração:", resultado_subtracao)
    print("Resultado da Multiplicação:", resultado_multiplicacao)
    print("Resultado da Divisão:", resultado_divisao)

    # O registro de operações será salvo em "registro_operacoes.txt"