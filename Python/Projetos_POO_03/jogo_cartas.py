import random

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self):
        naipes = ["Espadas", "Paus", "Copas", "Ouros"]
        valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "Ás"]
        self.cartas = [Carta(valor, naipe) for naipe in naipes for valor in valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            return None

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_carta(self, carta):
        self.mao.append(carta)

    def mostrar_mao(self):
        print(f"{self.nome}'s mão:")
        for carta in self.mao:
            print(carta)

# Exemplo de uso:
if __name__ == "__main__":
    baralho = Baralho()
    baralho.embaralhar()

    jogador1 = Jogador("Jogador 1")
    jogador2 = Jogador("Jogador 2")

    for _ in range(5):
        carta1 = baralho.distribuir_carta()
        carta2 = baralho.distribuir_carta()
        jogador1.receber_carta(carta1)
        jogador2.receber_carta(carta2)

    jogador1.mostrar_mao()
    jogador2.mostrar_mao()