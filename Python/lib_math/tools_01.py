#################################
#################################
# 1 - Cálculo do Fatorial usando math.factorial()
# 2 - Cálculo do Seno usando math.sin()
# 3 - Cálculo da Raiz Quadrada usando math.sqrt()
# 4 - Cálculo do Logaritmo Natural usando math.log()
# 5 - Cálculo da Constante Pi usando math.pi
#################################
#################################
import math


# 1 - Cálculo do Fatorial usando math.factorial()
class CalculadoraFatorial:
    def __init__(self, numero):
        self.numero = numero

    def calcular_fatorial(self):
        return math.factorial(self.numero)

calculadora = CalculadoraFatorial(5)
print("Fatorial de", calculadora.numero, "é:", calculadora.calcular_fatorial())

# 2 - Cálculo do Seno usando math.sin()
class CalculadoraSeno:
    def __init__(self, angulo):
        self.angulo = angulo

    def calcular_seno(self):
        return math.sin(math.radians(self.angulo))

calculadora = CalculadoraSeno(45)
print("Seno de", calculadora.angulo, "graus é:", calculadora.calcular_seno())

# 3 - Cálculo da Raiz Quadrada usando math.sqrt()
class CalculadoraRaizQuadrada:
    def __init__(self, numero):
        self.numero = numero

    def calcular_raiz_quadrada(self):
        return math.sqrt(self.numero)

calculadora = CalculadoraRaizQuadrada(25)
print("Raiz quadrada de", calculadora.numero, "é:", calculadora.calcular_raiz_quadrada())

# 4 - Cálculo do Logaritmo Natural usando math.log()
class CalculadoraLogaritmoNatural:
    def __init__(self, numero):
        self.numero = numero

    def calcular_logaritmo_natural(self):
        return math.log(self.numero)

calculadora = CalculadoraLogaritmoNatural(10)
print("Logaritmo natural de", calculadora.numero, "é:", calculadora.calcular_logaritmo_natural())

# 5 - Cálculo da Constante Pi usando math.pi
class CalculadoraPi:
    def __init__(self):
        pass

    def obter_valor_pi(self):
        return math.pi

calculadora = CalculadoraPi()
print("O valor de Pi é:", calculadora.obter_valor_pi())
