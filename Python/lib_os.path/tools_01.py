#################################
#################################
# 1 - Verificar se um Caminho é um Diretório
# 2 - Verificar se um Caminho é um Arquivo
# 3 - Obter o Nome do Arquivo de um Caminho
# 4 - Obter o Diretório Pai de um Caminho
# 5 - Juntar Componentes de um Caminho
#################################
#################################
import os

# 1 - Verificar se um Caminho é um Diretório
class VerificadorDiretorio:
    def __init__(self, caminho):
        self.caminho = caminho

    def verificar_diretorio(self):
        return os.path.isdir(self.caminho)

caminho = "/path/to/directory"
verificador = VerificadorDiretorio(caminho)
print("O caminho", caminho, "é um diretório?", verificador.verificar_diretorio())

# 2 - Verificar se um Caminho é um Arquivo
class VerificadorArquivo:
    def __init__(self, caminho):
        self.caminho = caminho

    def verificar_arquivo(self):
        return os.path.isfile(self.caminho)

caminho = "/path/to/file.txt"
verificador = VerificadorArquivo(caminho)
print("O caminho", caminho, "é um arquivo?", verificador.verificar_arquivo())

# 3 - Obter o Nome do Arquivo de um Caminho
class ObterNomeArquivo:
    def __init__(self, caminho):
        self.caminho = caminho

    def obter_nome_arquivo(self):
        return os.path.basename(self.caminho)

caminho = "/path/to/file.txt"
obter_nome = ObterNomeArquivo(caminho)
print("Nome do arquivo:", obter_nome.obter_nome_arquivo())

# 4 - Obter o Diretório Pai de um Caminho
class ObterDiretorioPai:
    def __init__(self, caminho):
        self.caminho = caminho

    def obter_diretorio_pai(self):
        return os.path.dirname(self.caminho)

caminho = "/path/to/file.txt"
obter_diretorio = ObterDiretorioPai(caminho)
print("Diretório pai:", obter_diretorio.obter_diretorio_pai())

# 5 - Juntar Componentes de um Caminho
class JuntarCaminhos:
    def __init__(self, *componentes):
        self.componentes = componentes

    def juntar(self):
        return os.path.join(*self.componentes)

caminho1 = "/path/to"
caminho2 = "file.txt"
juntador = JuntarCaminhos(caminho1, caminho2)
print("Caminho completo:", juntador.juntar())
