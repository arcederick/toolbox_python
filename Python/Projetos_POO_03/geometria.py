import math

class FormaGeometrica:
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

if __name__ == "__main__":
    retangulo = Retangulo(5, 10)
    circulo = Circulo(4)
    triangulo = Triangulo(6, 8)

    formas = [retangulo, circulo, triangulo]

    for forma in formas:
        nome = forma.__class__.__name__
        area = forma.calcular_area()
        print(f"Área do {nome}: {area}")