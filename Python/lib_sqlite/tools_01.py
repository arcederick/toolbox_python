#################################
#################################
# 1 - Criar uma Nova Tabela no Banco de Dados SQLite
# 2 - Inserir Dados em uma Tabela do Banco de Dados
# 3 - Selecionar Dados de uma Tabela do Banco de Dados
# 4 - Atualizar Dados em uma Tabela do Banco de Dados
# 5 - Excluir Dados de uma Tabela do Banco de Dados 
#################################
#################################
import sqlite3

# 1 - Criar uma Nova Tabela no Banco de Dados SQLite
class CriadorTabelaSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def criar_tabela(self):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                          (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')
        conexao.commit()
        conexao.close()

criador_tabela = CriadorTabelaSQLite('banco_dados.db')
criador_tabela.criar_tabela()

# 2 - Inserir Dados em uma Tabela do Banco de Dados
class InseridorDadosSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def inserir_dados(self, nome, idade):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
        conexao.commit()
        conexao.close()

inseridor_dados = InseridorDadosSQLite('banco_dados.db')
inseridor_dados.inserir_dados('Alice', 30)

# 3 - Selecionar Dados de uma Tabela do Banco de Dados
class SelecionadorDadosSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def selecionar_dados(self):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()
        conexao.close()
        return dados

selecionador_dados = SelecionadorDadosSQLite('banco_dados.db')
dados = selecionador_dados.selecionar_dados()
print("Dados da tabela:", dados)

# 4 - Atualizar Dados em uma Tabela do Banco de Dados
class AtualizadorDadosSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def atualizar_dados(self, id, novo_nome):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (novo_nome, id))
        conexao.commit()
        conexao.close()

atualizador_dados = AtualizadorDadosSQLite('banco_dados.db')
atualizador_dados.atualizar_dados(1, 'Bob')

# 5 - Excluir Dados de uma Tabela do Banco de Dados 
class ExcluidorDadosSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def excluir_dados(self, id):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        conexao.commit()
        conexao.close()

excluidor_dados = ExcluidorDadosSQLite('banco_dados.db')
excluidor_dados.excluir_dados(1)
