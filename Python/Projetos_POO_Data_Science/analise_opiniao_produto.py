import pandas as pd
from textblob import TextBlob

class AvaliacaoProduto:
    def __init__(self, produto, opiniao):
        self.produto = produto
        self.opiniao = opiniao

class SistemaAnaliseOpinioes:
    def __init__(self):
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def analisar_sentimentos(self):
        sentimentos = []
        for avaliacao in self.avaliacoes:
            analise = TextBlob(avaliacao.opiniao)
            polaridade = analise.sentiment.polarity
            if polaridade > 0:
                sentimento = "Positivo"
            elif polaridade < 0:
                sentimento = "Negativo"
            else:
                sentimento = "Neutro"
            sentimentos.append(sentimento)
        return sentimentos

    def contar_sentimentos(self):
        sentimentos = self.analisar_sentimentos()
        contagem = {
            "Positivo": sentimentos.count("Positivo"),
            "Negativo": sentimentos.count("Negativo"),
            "Neutro": sentimentos.count("Neutro"),
        }
        return contagem

if __name__ == "__main__":
    sistema_analise = SistemaAnaliseOpinioes()

    avaliacao1 = AvaliacaoProduto("Celular", "Ótimo produto, estou muito satisfeito!")
    avaliacao2 = AvaliacaoProduto("Laptop", "A bateria não dura muito, estou insatisfeito.")
    avaliacao3 = AvaliacaoProduto("Fones de Ouvido", "Som de alta qualidade, estou impressionado.")

    sistema_analise.adicionar_avaliacao(avaliacao1)
    sistema_analise.adicionar_avaliacao(avaliacao2)
    sistema_analise.adicionar_avaliacao(avaliacao3)

    contagem_sentimentos = sistema_analise.contar_sentimentos()
    print("Contagem de Sentimentos:")
    for sentimento, contagem in contagem_sentimentos.items():
        print(f"{sentimento}: {contagem} avaliações")