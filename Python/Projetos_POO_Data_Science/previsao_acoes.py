import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class Acao:
    def __init__(self, nome):
        self.nome = nome
        self.dados = pd.DataFrame()

    def adicionar_dados(self, data, preco):
        self.dados = self.dados.append({'Data': data, 'Preco': preco}, ignore_index=True)

class SistemaPrevisaoAcoes:
    def __init__(self):
        self.acoes = {}

    def adicionar_acao(self, nome_acao):
        self.acoes[nome_acao] = Acao(nome_acao)

    def prever_valor_acao(self, nome_acao):
        acao = self.acoes.get(nome_acao)
        if acao:
            X = acao.dados[['Data']].values
            y = acao.dados['Preco'].values
            modelo = LinearRegression()
            modelo.fit(X, y)
            previsao = modelo.predict([[X[-1] + pd.Timedelta(days=1)]])[0]
            return previsao
        else:
            return None

    def plotar_grafico_acao(self, nome_acao):
        acao = self.acoes.get(nome_acao)
        if acao:
            plt.plot(acao.dados['Data'], acao.dados['Preco'], label=nome_acao)
            plt.xlabel('Data')
            plt.ylabel('Preço')
            plt.title(f'Histórico de Preços de {nome_acao}')
            plt.legend()
            plt.show()
        else:
            print("Ação não encontrada.")

if __name__ == "__main__":
    sistema_previsao = SistemaPrevisaoAcoes()

    sistema_previsao.adicionar_acao("AAPL")
    sistema_previsao.adicionar_acao("GOOGL")

    sistema_previsao.acoes["AAPL"].adicionar_dados("2023-01-01", 150.0)
    sistema_previsao.acoes["AAPL"].adicionar_dados("2023-01-02", 155.0)
    sistema_previsao.acoes["AAPL"].adicionar_dados("2023-01-03", 160.0)
    sistema_previsao.acoes["GOOGL"].adicionar_dados("2023-01-01", 2700.0)
    sistema_previsao.acoes["GOOGL"].adicionar_dados("2023-01-02", 2750.0)
    sistema_previsao.acoes["GOOGL"].adicionar_dados("2023-01-03", 2800.0)

    previsao = sistema_previsao.prever_valor_acao("AAPL")
    print(f"Previsão de preço para AAPL: ${previsao:.2f}")

    sistema_previsao.plotar_grafico_acao("AAPL")