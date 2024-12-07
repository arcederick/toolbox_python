import pandas as pd
import matplotlib.pyplot as plt
import random

class Postagem:
    def __init__(self, autor, conteudo, data):
        self.autor = autor
        self.conteudo = conteudo
        self.data = data

class RedeSocial:
    def __init__(self):
        self.postagens = []

    def adicionar_postagem(self, postagem):
        self.postagens.append(postagem)

    def analisar_sentimentos(self):
        # Implemente a análise de sentimentos das postagens
        # Este é um exemplo simples
        sentimentos = ["Positivo", "Negativo", "Neutro"]
        resultados = [random.choice(sentimentos) for _ in range(len(self.postagens))]
        return resultados

    def plotar_histograma_sentimentos(self):
        sentimentos = self.analisar_sentimentos()
        plt.hist(sentimentos, bins=3)
        plt.xlabel('Sentimento')
        plt.ylabel('Quantidade')
        plt.title('Histograma de Sentimentos')
        plt.show()

if __name__ == "__main__":
    rede_social = RedeSocial()

    postagem1 = Postagem("Alice", "Estou tão animado para o feriado!", "2023-11-25")
    postagem2 = Postagem("Bob", "Dia chuvoso triste.", "2023-11-26")
    postagem3 = Postagem("Charlie", "Trabalhando duro!", "2023-11-27")

    rede_social.adicionar_postagem(postagem1)
    rede_social.adicionar_postagem(postagem2)
    rede_social.adicionar_postagem(postagem3)

    rede_social.plotar_histograma_sentimentos()