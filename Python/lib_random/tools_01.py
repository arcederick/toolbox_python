#################################
#################################
# 1 - Gerador de Senhas Aleatórias
# 2 - Embaralhar uma Lista
# 3 - Escolher um Elemento Aleatório de uma Lista
# 4 - Simulação de Lançamento de Dados
# 5 - Amostragem Aleatória de uma População
#################################
#################################
import random
import string

# 1 - Gerador de Senhas Aleatórias
class GeradorSenha:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def gerar_senha(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for i in range(self.tamanho))
        return senha

gerador = GeradorSenha(12)
print("Senha Aleatória:", gerador.gerar_senha())

# 2 - Embaralhar uma Lista
class EmbaralhadorLista:
    def __init__(self, lista):
        self.lista = lista

    def embaralhar(self):
        random.shuffle(self.lista)
        return self.lista

minha_lista = [1, 2, 3, 4, 5]
embaralhador = EmbaralhadorLista(minha_lista)
print("Lista Embaralhada:", embaralhador.embaralhar())

# 3 - Escolher um Elemento Aleatório de uma Lista
class EscolherElemento:
    def __init__(self, lista):
        self.lista = lista

    def escolher(self):
        return random.choice(self.lista)

opcoes = ['Maçã', 'Banana', 'Laranja', 'Morango']
escolhedor = EscolherElemento(opcoes)
print("Elemento Escolhido Aleatoriamente:", escolhedor.escolher())

# 4 - Simulação de Lançamento de Dados
class LancamentoDados:
    def __init__(self):
        pass

    def lancar_dado(self):
        return random.randint(1, 6)

lancador = LancamentoDados()
print("Resultado do lançamento do dado:", lancador.lancar_dado())

# 5 - Amostragem Aleatória de uma População
class AmostragemAleatoria:
    def __init__(self, populacao, tamanho_amostra):
        self.populacao = populacao
        self.tamanho_amostra = tamanho_amostra

    def amostra(self):
        return random.sample(self.populacao, self.tamanho_amostra)

populacao = range(1, 101)
tamanho_amostra = 10
amostrador = AmostragemAleatoria(populacao, tamanho_amostra)
print("Amostra Aleatória da População:", amostrador.amostra())
