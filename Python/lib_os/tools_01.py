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