#################################
#################################
# 1 - Leitura de um Arquivo JSON
# 2 - Escrita em um Arquivo JSON
# 3 - Conversão de Dicionário para String JSON
# 4 - Conversão de String JSON para Dicionário
# 5 - Manipulação de Dados Aninhados em JSON
#################################
#################################
import json


# 1 - Leitura de um Arquivo JSON
class LeitorJSON:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def ler_arquivo_json(self):
        with open(self.nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados

leitor = LeitorJSON('dados.json')
dados = leitor.ler_arquivo_json()
print("Dados lidos do arquivo JSON:", dados)

# 2 - Escrita em um Arquivo JSON
class EscritorJSON:
    def __init__(self, nome_arquivo, dados):
        self.nome_arquivo = nome_arquivo
        self.dados = dados

    def escrever_arquivo_json(self):
        with open(self.nome_arquivo, 'w') as arquivo:
            json.dump(self.dados, arquivo, indent=4)

dados = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
escritor = EscritorJSON('dados.json', dados)
escritor.escrever_arquivo_json()

# 3 - Conversão de Dicionário para String JSON
class ConversorDictParaJSON:
    def __init__(self, dicionario):
        self.dicionario = dicionario

    def converter_para_json(self):
        return json.dumps(self.dicionario)

dados = {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'}
conversor = ConversorDictParaJSON(dados)
json_string = conversor.converter_para_json()
print("Dicionário convertido para JSON:", json_string)

# 4 - Conversão de String JSON para Dicionário
class ConversorJSONParaDict:
    def __init__(self, json_string):
        self.json_string = json_string

    def converter_para_dict(self):
        return json.loads(self.json_string)

json_string = '{"nome": "Pedro", "idade": 35, "cidade": "Belo Horizonte"}'
conversor = ConversorJSONParaDict(json_string)
dados = conversor.converter_para_dict()
print("String JSON convertida para dicionário:", dados)

# 5 - Manipulação de Dados Aninhados em JSON
class ManipuladorDadosAninhados:
    def __init__(self, dados):
        self.dados = dados

    def obter_valor(self, chave):
        try:
            return json.dumps(self.dados[chave])
        except KeyError:
            return f'A chave "{chave}" não existe nos dados.'

dados = {'pessoa': {'nome': 'Ana', 'idade': 28}}
manipulador = ManipuladorDadosAninhados(dados)
print("Valor da chave 'nome':", manipulador.obter_valor('nome'))
print("Valor da chave 'email':", manipulador.obter_valor('email'))
