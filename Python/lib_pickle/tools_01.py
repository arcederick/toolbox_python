#################################
#################################
# 1 - Serialização de um Objeto para um Arquivo usando Pickle
# 2 - Desserialização de um Objeto de um Arquivo usando Pickle
# 3 - Serialização e Desserialização de Objetos Personalizados
# 4 - Serialização e Desserialização de Múltiplos Objetos
# 5 - Uso de Protocolo de Protocolo de Pickle Personalizado
#################################
#################################
import pickle

# 1 - Serialização de um Objeto para um Arquivo usando Pickle
class SerializadorPickle:
    def __init__(self, objeto, nome_arquivo):
        self.objeto = objeto
        self.nome_arquivo = nome_arquivo

    def serializar(self):
        with open(self.nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.objeto, arquivo)

meu_objeto = {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}
serializador = SerializadorPickle(meu_objeto, 'meu_objeto.pickle')
serializador.serializar()

# 2 - Desserialização de um Objeto de um Arquivo usando Pickle
class DesserializadorPickle:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def desserializar(self):
        with open(self.nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)

objeto = DesserializadorPickle('meu_objeto.pickle').desserializar()
print("Objeto desserializado:", objeto)

# 3 - Serialização e Desserialização de Objetos Personalizados
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade})'

# Serialização
pessoa = Pessoa('João', 25)
with open('pessoa.pickle', 'wb') as arquivo:
    pickle.dump(pessoa, arquivo)

# Desserialização
with open('pessoa.pickle', 'rb') as arquivo:
    pessoa_desserializada = pickle.load(arquivo)

print("Pessoa desserializada:", pessoa_desserializada)

# 4 - Serialização e Desserialização de Múltiplos Objetos
# Dados de exemplo
dados = {'nome': 'Maria', 'idade': 30}
lista = [1, 2, 3, 4, 5]

# Serialização de múltiplos objetos
with open('multiplos_objetos.pickle', 'wb') as arquivo:
    pickle.dump(dados, arquivo)
    pickle.dump(lista, arquivo)

# Desserialização de múltiplos objetos
with open('multiplos_objetos.pickle', 'rb') as arquivo:
    dados_desserializados = pickle.load(arquivo)
    lista_desserializada = pickle.load(arquivo)

print("Dados desserializados:", dados_desserializados)
print("Lista desserializada:", lista_desserializada)

# 5 - Uso de Protocolo Pickle Personalizado
class ObjetoPickleCustomizado:
    def __init__(self, dados):
        self.dados = dados

    def __getstate__(self):
        return self.dados

    def __setstate__(self, estado):
        self.__init__(estado)

objeto_original = ObjetoPickleCustomizado({'nome': 'Ana', 'idade': 35})

# Serialização
with open('objeto_custom.pickle', 'wb') as arquivo:
    pickle.dump(objeto_original, arquivo)

# Desserialização
with open('objeto_custom.pickle', 'rb') as arquivo:
    objeto_desserializado = pickle.load(arquivo)

print("Objeto desserializado:", objeto_desserializado)
