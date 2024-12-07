#################################
#################################
# 1 - Cálculo da Diferença entre Duas Datas
# 2 - Adicionar ou Subtrair Dias de uma Data
# 3 - Exibição do Dia da Semana de uma Data
# 4 - Formatação de uma Data
# 5 - Verificação de Ano Bissexto
#################################
#################################

from datetime import datetime, timedelta

# 1 - Cálculo da Diferença entre Duas Datas
class CalculoDiferencaDatas:
    def __init__(self, data1, data2):
        self.data1 = datetime.strptime(data1, "%Y-%m-%d")
        self.data2 = datetime.strptime(data2, "%Y-%m-%d")

    def calcular_diferenca(self):
        diferenca = self.data2 - self.data1
        return diferenca.days

data_inicial = "2024-01-01"
data_final = "2024-03-01"
calculadora = CalculoDiferencaDatas(data_inicial, data_final)
print("Diferença entre as datas:", calculadora.calcular_diferenca(), "dias")

# 2 - Adicionar ou Subtrair Dias de uma Data
class OperacoesData:
    def __init__(self, data, dias):
        self.data = datetime.strptime(data, "%Y-%m-%d")
        self.dias = dias

    def adicionar_dias(self):
        nova_data = self.data + timedelta(days=self.dias)
        return nova_data.strftime("%Y-%m-%d")

data_atual = "2024-03-12"
dias_para_adicionar = 7
operacoes = OperacoesData(data_atual, dias_para_adicionar)
print("Nova data após adicionar", dias_para_adicionar, "dias:", operacoes.adicionar_dias())

# 3 - Exibição do Dia da Semana de uma Data
class DiaSemanaData:
    def __init__(self, data):
        self.data = datetime.strptime(data, "%Y-%m-%d")

    def obter_dia_semana(self):
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        return dias_semana[self.data.weekday()]

data = "2024-03-12"
dia_semana = DiaSemanaData(data)
print("Dia da semana para", data, ":", dia_semana.obter_dia_semana())

# 4 - Formatação de uma Data
class FormatacaoData:
    def __init__(self, data):
        self.data = datetime.strptime(data, "%Y-%m-%d")

    def formatar_data(self, formato):
        return self.data.strftime(formato)

data = "2024-03-12"
formatador = FormatacaoData(data)
print("Data formatada (DD/MM/AAAA):", formatador.formatar_data("%d/%m/%Y"))

# 5 - Verificação de Ano Bissexto
class VerificarAnoBissexto:
    def __init__(self, ano):
        self.ano = ano

    def eh_bissexto(self):
        return (self.ano % 4 == 0 and self.ano % 100 != 0) or (self.ano % 400 == 0)

ano = 2024
verificador = VerificarAnoBissexto(ano)
if verificador.eh_bissexto():
    print(ano, "é um ano bissexto")
else:
    print(ano, "não é um ano bissexto")
