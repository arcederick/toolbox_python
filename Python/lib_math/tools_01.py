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

# 6 - Cálculo do Cosseno usando math.cos()
class CalculadoraCosseno:
    def __init__(self, angulo):
        self.angulo = angulo

    def calcular_cosseno(self):
        return math.cos(math.radians(self.angulo))

calculadora = CalculadoraCosseno(45)
print("Cosseno de", calculadora.angulo, "graus é:", calculadora.calcular_cosseno())

# 7 - Cálculo da Tangente usando math.tan()
class CalculadoraTangente:
    def __init__(self, angulo):
        self.angulo = angulo

    def calcular_tangente(self):
        return math.tan(math.radians(self.angulo))

calculadora = CalculadoraTangente(45)
print("Tangente de", calculadora.angulo, "graus é:", calculadora.calcular_tangente())

# 8 - Cálculo da Exponencial usando math.exp()
class CalculadoraExponencial:
    def __init__(self, numero):
        self.numero = numero

    def calcular_exponencial(self):
        return math.exp(self.numero)

calculadora = CalculadoraExponencial(2)
print("Exponencial de", calculadora.numero, "é:", calculadora.calcular_exponencial())

# 9 - Cálculo da Função Fatorial de um Número com math.factorial()
class CalculadoraFatorialGrande:
    def __init__(self, numero):
        self.numero = numero

    def calcular_fatorial_grande(self):
        return math.factorial(self.numero)

calculadora = CalculadoraFatorialGrande(10)
print("Fatorial de", calculadora.numero, "é:", calculadora.calcular_fatorial_grande())

# 10 - Cálculo do Valor Absoluto com math.fabs()
class CalculadoraValorAbsoluto:
    def __init__(self, numero):
        self.numero = numero

    def calcular_absoluto(self):
        return math.fabs(self.numero)

calculadora = CalculadoraValorAbsoluto(-7.25)
print("Valor absoluto de", calculadora.numero, "é:", calculadora.calcular_absoluto())

# 11 - Cálculo do Máximo entre dois valores com math.fmax()
class CalculadoraMaximo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular_maximo(self):
        return math.fmax(self.a, self.b)

calculadora = CalculadoraMaximo(5, 10)
print("Máximo entre", calculadora.a, "e", calculadora.b, "é:", calculadora.calcular_maximo())

# 12 - Cálculo do Mínimo entre dois valores com math.fmin()
class CalculadoraMinimo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular_minimo(self):
        return math.fmin(self.a, self.b)

calculadora = CalculadoraMinimo(5, 10)
print("Mínimo entre", calculadora.a, "e", calculadora.b, "é:", calculadora.calcular_minimo())

# 13 - Cálculo de Potência com math.pow()
class CalculadoraPotencia:
    def __init__(self, base, expoente):
        self.base = base
        self.expoente = expoente

    def calcular_potencia(self):
        return math.pow(self.base, self.expoente)

calculadora = CalculadoraPotencia(2, 3)
print(f"{calculadora.base} elevado a {calculadora.expoente} é:", calculadora.calcular_potencia())

# 14 - Cálculo do Arco Seno (inverso do Seno) com math.asin()
class CalculadoraArcoSeno:
    def __init__(self, valor):
        self.valor = valor

    def calcular_arco_seno(self):
        return math.degrees(math.asin(self.valor))

calculadora = CalculadoraArcoSeno(0.5)
print("Arco seno de", calculadora.valor, "é:", calculadora.calcular_arco_seno(), "graus")

# 15 - Cálculo do Arco Cosseno (inverso do Cosseno) com math.acos()
class CalculadoraArcoCosseno:
    def __init__(self, valor):
        self.valor = valor

    def calcular_arco_cosseno(self):
        return math.degrees(math.acos(self.valor))

calculadora = CalculadoraArcoCosseno(0.5)
print("Arco cosseno de", calculadora.valor, "é:", calculadora.calcular_arco_cosseno(), "graus")