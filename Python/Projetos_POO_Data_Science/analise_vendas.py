import pandas as pd
import matplotlib.pyplot as plt

class SistemaAnaliseVendas:
    def __init__(self, arquivo_csv):
        self.df = pd.read_csv(arquivo_csv)

    def mostrar_estatisticas_vendas(self):
        # Exibe estatísticas básicas das vendas
        print("Estatísticas de Vendas:")
        print(self.df.describe())

    def visualizar_vendas_por_produto(self):
        # Gera um gráfico de barras das vendas por produto
        vendas_por_produto = self.df.groupby('Produto')['Valor'].sum()
        vendas_por_produto.plot(kind='bar', title='Vendas por Produto')
        plt.xlabel('Produto')
        plt.ylabel('Total de Vendas')
        plt.show()

    def analisar_tendencias_de_vendas(self):
        # Analisa tendências de vendas ao longo do tempo
        self.df['Data'] = pd.to_datetime(self.df['Data'])
        vendas_por_data = self.df.groupby('Data')['Valor'].sum()
        vendas_por_data.plot(title='Tendências de Vendas ao Longo do Tempo')
        plt.xlabel('Data')
        plt.ylabel('Total de Vendas')
        plt.show()

if __name__ == "__main__":
    # Crie uma instância do sistema de análise de vendas com um arquivo CSV de dados de vendas
    sistema_analise = SistemaAnaliseVendas('dados_de_vendas.csv')

    # Mostrar estatísticas de vendas
    sistema_analise.mostrar_estatisticas_vendas()

    # Visualizar vendas por produto
    sistema_analise.visualizar_vendas_por_produto()

    # Analisar tendências de vendas
    sistema_analise.analisar_tendencias_de_vendas()