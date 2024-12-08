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


# 6 - Cálculo da Idade em Anos a partir de uma Data de Nascimento
class CalculoIdade:
    def __init__(self, data_nascimento):
        self.data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
        self.data_atual = datetime.today()

    def calcular_idade(self):
        idade = self.data_atual.year - self.data_nascimento.year
        if self.data_atual.month < self.data_nascimento.month or (self.data_atual.month == self.data_nascimento.month and self.data_atual.day < self.data_nascimento.day):
            idade -= 1
        return idade

data_nascimento = "1990-05-15"
calculadora_idade = CalculoIdade(data_nascimento)
print("Idade de quem nasceu em", data_nascimento, "é:", calculadora_idade.calcular_idade(), "anos")

# 7 - Comparação entre Duas Datas
class CompararDatas:
    def __init__(self, data1, data2):
        self.data1 = datetime.strptime(data1, "%Y-%m-%d")
        self.data2 = datetime.strptime(data2, "%Y-%m-%d")

    def comparar(self):
        if self.data1 > self.data2:
            return "A primeira data é posterior à segunda."
        elif self.data1 < self.data2:
            return "A primeira data é anterior à segunda."
        else:
            return "As datas são iguais."

data1 = "2024-03-12"
data2 = "2024-03-15"
comparador = CompararDatas(data1, data2)
print(comparador.comparar())

# 8 - Obter Data e Hora Atual
class ObterDataHoraAtual:
    def __init__(self):
        self.data_hora_atual = datetime.now()

    def obter_data_hora(self):
        return self.data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

data_hora = ObterDataHoraAtual()
print("Data e Hora atual:", data_hora.obter_data_hora())

# 9 - Cálculo de Dias de um Mês Específico
class DiasDoMes:
    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes

    def dias_no_mes(self):
        proximo_mes = self.mes % 12 + 1
        ano_proximo_mes = self.ano + (self.mes // 12)
        primeiro_dia_proximo_mes = datetime(ano_proximo_mes, proximo_mes, 1)
        ultimo_dia_mes = primeiro_dia_proximo_mes - timedelta(days=1)
        return ultimo_dia_mes.day

ano = 2024
mes = 2
dias_mes = DiasDoMes(ano, mes)
print(f"Dias no mês {mes}/{ano}:", dias_mes.dias_no_mes())

# 10 - Cálculo de Data de Nascimento a partir de Idade
class CalcularDataNascimento:
    def __init__(self, idade):
        self.idade = idade
        self.data_atual = datetime.today()

    def calcular_data_nascimento(self):
        data_nascimento = self.data_atual.replace(year=self.data_atual.year - self.idade)
        return data_nascimento.strftime("%Y-%m-%d")

idade = 30
calculadora_data_nascimento = CalcularDataNascimento(idade)
print("Data de nascimento para quem tem", idade, "anos:", calculadora_data_nascimento.calcular_data_nascimento())

# 11 - Converter Data e Hora para Timestamp
class ConverterTimestamp:
    def __init__(self, data_hora):
        self.data_hora = datetime.strptime(data_hora, "%Y-%m-%d %H:%M:%S")

    def converter_timestamp(self):
        return int(self.data_hora.timestamp())

data_hora = "2024-03-12 15:30:00"
converter = ConverterTimestamp(data_hora)
print(f"Timestamp para {data_hora}:", converter.converter_timestamp())

# 12 - Converter Timestamp para Data e Hora
class ConverterDataHora:
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def converter_data_hora(self):
        return datetime.fromtimestamp(self.timestamp).strftime("%Y-%m-%d %H:%M:%S")

timestamp = 1683741600  # Exemplo de timestamp
converter_data_hora = ConverterDataHora(timestamp)
print(f"Data e Hora para o timestamp {timestamp}:", converter_data_hora.converter_data_hora())

# 13 - Adicionar Meses a uma Data
from dateutil.relativedelta import relativedelta

class AdicionarMeses:
    def __init__(self, data, meses):
        self.data = datetime.strptime(data, "%Y-%m-%d")
        self.meses = meses

    def adicionar_meses(self):
        nova_data = self.data + relativedelta(months=self.meses)
        return nova_data.strftime("%Y-%m-%d")

data = "2024-03-12"
meses_para_adicionar = 3
adicionador = AdicionarMeses(data, meses_para_adicionar)
print(f"Nova data após adicionar {meses_para_adicionar} meses:", adicionador.adicionar_meses())

# 14 - Obter o Último Dia do Ano Atual
class UltimoDiaAno:
    def __init__(self, ano):
        self.ano = ano

    def ultimo_dia(self):
        ultimo_dia = datetime(self.ano, 12, 31)
        return ultimo_dia.strftime("%Y-%m-%d")

ano = 2024
ultimo_dia = UltimoDiaAno(ano)
print("Último dia do ano", ano, ":", ultimo_dia.ultimo_dia())

# 15 - Contar a Quantidade de Semanas Entre Duas Datas
class ContarSemanasEntreDatas:
    def __init__(self, data_inicial, data_final):
        self.data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d")
        self.data_final = datetime.strptime(data_final, "%Y-%m-%d")

    def contar_semanas(self):
        diferenca = self.data_final - self.data_inicial
        return diferenca.days // 7

data_inicial = "2024-01-01"
data_final = "2024-03-01"
contagem_semanas = ContarSemanasEntreDatas(data_inicial, data_final)
print(f"Quantidade de semanas entre {data_inicial} e {data_final}:", contagem_semanas.contar_semanas())