import random

class JogoAdivinhacao:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0

    def adivinhar(self, numero):
        self.tentativas += 1

        if numero < self.numero_secreto:
            return "Tente um número maior."
        elif numero > self.numero_secreto:
            return "Tente um número menor."
        else:
            return f"Parabéns! Você acertou em {self.tentativas} tentativas."

jogo = JogoAdivinhacao()

print("Bem-vindo ao Jogo de Adivinhação de Números!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
        resultado = jogo.adivinhar(palpite)
        print(resultado)
        
        if resultado.startswith("Parabéns"):
            break
    except ValueError:
        print("Entrada inválida. Digite um número válido.")