#################################
#################################
# 1 - Listar Arquivos em Diretório
# 2 - Criar Diretório
# 3 - Renomear Arquivo
# 4 - Excluir Arquivo
# 5 - Verificar se um diretório Existe
#################################
#################################
import os


# 1 - Listar Arquivos em Diretório
class ListarArquivos:
    def __init__(self, diretorio):
        self.diretorio = diretorio

    def listar(self):
        arquivos = os.listdir(self.diretorio)
        for arquivo in arquivos:
            print(arquivo)

diretorio_atual = os.getcwd()
listador = ListarArquivos(diretorio_atual)
listador.listar()

# 2 - Criar Diretório
class CriarDiretorio:
    def __init__(self, nome):
        self.nome = nome

    def criar(self):
        os.makedirs(self.nome)
        print("Diretório", self.nome, "criado com sucesso.")

novo_diretorio = "meu_novo_diretorio"
criador = CriarDiretorio(novo_diretorio)
criador.criar()

# 3 - Renomear Arquivo
class RenomearArquivo:
    def __init__(self, nome_antigo, nome_novo):
        self.nome_antigo = nome_antigo
        self.nome_novo = nome_novo

    def renomear(self):
        os.rename(self.nome_antigo, self.nome_novo)
        print("Arquivo renomeado de", self.nome_antigo, "para", self.nome_novo)

arquivo_antigo = "arquivo_antigo.txt"
arquivo_novo = "arquivo_novo.txt"
renomeador = RenomearArquivo(arquivo_antigo, arquivo_novo)
renomeador.renomear()

# 4 - Excluir Arquivo
class ExcluirArquivo:
    def __init__(self, nome):
        self.nome = nome

    def excluir(self):
        os.remove(self.nome)
        print("Arquivo", self.nome, "excluído com sucesso.")

arquivo_a_excluir = "arquivo_a_excluir.txt"
excluidor = ExcluirArquivo(arquivo_a_excluir)
excluidor.excluir()

# 5 - Verificar se um diretório Existe
class VerificarDiretorio:
    def __init__(self, nome):
        self.nome = nome

    def verificar(self):
        if os.path.exists(self.nome):
            print("O diretório", self.nome, "existe.")
        else:
            print("O diretório", self.nome, "não existe.")

diretorio_verificar = "meu_diretorio"
verificador = VerificarDiretorio(diretorio_verificar)
verificador.verificar()

import os

# 6 - Obter o Caminho Absoluto de um Arquivo ou Diretório
class CaminhoAbsoluto:
    def __init__(self, caminho_relativo):
        self.caminho_relativo = caminho_relativo

    def obter(self):
        caminho_absoluto = os.path.abspath(self.caminho_relativo)
        print("Caminho absoluto:", caminho_absoluto)

caminho_relativo = "meu_diretorio/arquivo.txt"
caminho = CaminhoAbsoluto(caminho_relativo)
caminho.obter()

# 7 - Obter o Tamanho de um Arquivo
class TamanhoArquivo:
    def __init__(self, nome):
        self.nome = nome

    def obter(self):
        tamanho = os.path.getsize(self.nome)
        print(f"Tamanho do arquivo {self.nome}: {tamanho} bytes")

arquivo_tamanho = "arquivo_novo.txt"
tamanho_arquivo = TamanhoArquivo(arquivo_tamanho)
tamanho_arquivo.obter()

# 8 - Alterar o Diretório de Trabalho
class AlterarDiretorio:
    def __init__(self, novo_diretorio):
        self.novo_diretorio = novo_diretorio

    def alterar(self):
        os.chdir(self.novo_diretorio)
        print(f"Diretório de trabalho alterado para {self.novo_diretorio}")

diretorio_novo = "/caminho/do/diretorio"
alterador = AlterarDiretorio(diretorio_novo)
alterador.alterar()

# 9 - Criar um Arquivo Temporário
class CriarArquivoTemporario:
    def __init__(self, prefixo):
        self.prefixo = prefixo

    def criar(self):
        arquivo, caminho = os.mkstemp(prefix=self.prefixo)
        print(f"Arquivo temporário criado: {caminho}")
        os.close(arquivo)

prefixo_temporario = "temp_"
temporario = CriarArquivoTemporario(prefixo_temporario)
temporario.criar()

# 10 - Obter Informações de um Arquivo
class InformacoesArquivo:
    def __init__(self, nome):
        self.nome = nome

    def obter(self):
        info = os.stat(self.nome)
        print(f"Informações do arquivo {self.nome}: {info}")

arquivo_info = "arquivo_novo.txt"
info_arquivo = InformacoesArquivo(arquivo_info)
info_arquivo.obter()

# 11 - Listar Arquivos com um Padrão Específico (com glob)
import glob

class ListarArquivosPadrao:
    def __init__(self, padrao):
        self.padrao = padrao

    def listar(self):
        arquivos = glob.glob(self.padrao)
        print("Arquivos encontrados:", arquivos)

padrao = "*.txt"
listador_padrao = ListarArquivosPadrao(padrao)
listador_padrao.listar()

# 12 - Criar Arquivo com Permissões Específicas
class CriarArquivoComPermissao:
    def __init__(self, nome, permissoes):
        self.nome = nome
        self.permissoes = permissoes

    def criar(self):
        with open(self.nome, "w") as arquivo:
            pass
        os.chmod(self.nome, self.permissoes)
        print(f"Arquivo {self.nome} criado com permissões {oct(self.permissoes)}")

arquivo_com_permissao = "arquivo_com_permissao.txt"
permissoes = 0o755  # Permissões de leitura, escrita e execução para o dono, leitura e execução para outros
criar_com_permissao = CriarArquivoComPermissao(arquivo_com_permissao, permissoes)
criar_com_permissao.criar()

# 13 - Obter o Nome do Arquivo ou Diretório
class ObterNome:
    def __init__(self, caminho):
        self.caminho = caminho

    def obter(self):
        nome = os.path.basename(self.caminho)
        print(f"Nome do arquivo/diretório: {nome}")

caminho = "/meu_diretorio/arquivo.txt"
nome_obtido = ObterNome(caminho)
nome_obtido.obter()

# 14 - Obter o Diretório de um Arquivo
class ObterDiretorio:
    def __init__(self, caminho):
        self.caminho = caminho

    def obter(self):
        diretorio = os.path.dirname(self.caminho)
        print(f"Diretório do arquivo: {diretorio}")

caminho = "/meu_diretorio/arquivo.txt"
diretorio_obtido = ObterDiretorio(caminho)
diretorio_obtido.obter()

# 15 - Remover um Diretório Vazio
class RemoverDiretorioVazio:
    def __init__(self, nome):
        self.nome = nome

    def remover(self):
        os.rmdir(self.nome)
        print(f"Diretório {self.nome} removido com sucesso.")

diretorio_vazio = "meu_diretorio_vazio"
remover_diretorio_vazio = RemoverDiretorioVazio(diretorio_vazio)
remover_diretorio_vazio.remover()
