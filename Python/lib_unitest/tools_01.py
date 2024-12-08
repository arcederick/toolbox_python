#################################
#################################
# 1 - Teste Simples de Igualdade
# 2 - Teste de Exceção
# 3 - Teste de Igualdade Aproximada para Números de Ponto Flutuante
# 4 - Teste de Comportamento de Funções
# 5 - Teste de Classes
#################################
#################################
import unittest

# 1 - Teste Simples de Igualdade
class TesteIgualdade(unittest.TestCase):
    def test_igualdade(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()

# 2 - Teste de Exceção
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

class TesteExcecao(unittest.TestCase):
    def test_excecao(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()

# 3 - Teste de Igualdade Aproximada para Números de Ponto Flutuante
class TesteIgualdadeFlutuante(unittest.TestCase):
    def test_igualdade_flutuante(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, delta=0.0001)

if __name__ == '__main__':
    unittest.main()

# 4 - Teste de Comportamento de Funções
def dobrar(numero):
    return numero * 2

class TesteComportamento(unittest.TestCase):
    def test_dobrar(self):
        self.assertEqual(dobrar(5), 10)
        self.assertEqual(dobrar(0), 0)
        self.assertEqual(dobrar(-3), -6)

if __name__ == '__main__':
    unittest.main()

# 5 - Teste de Classes
class MinhaClasse:
    def __init__(self, x):
        self.x = x

    def multiplicar(self, y):
        return self.x * y

class TesteClasse(unittest.TestCase):
    def test_multiplicar(self):
        objeto = MinhaClasse(5)
        self.assertEqual(objeto.multiplicar(2), 10)
        self.assertEqual(objeto.multiplicar(0), 0)
        self.assertEqual(objeto.multiplicar(-3), -15)


# 6 - Teste de Comparação de Objetos
class TesteComparacaoObjetos(unittest.TestCase):
    def test_comparar_objetos(self):
        self.assertIs("teste", "teste")
        self.assertIsNot("teste", "diferente")

# 7 - Teste de Tamanho de Lista
class TesteTamanhoLista(unittest.TestCase):
    def test_tamanho_lista(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(len(lista), 5)

# 8 - Teste de Adição de Elementos em Lista
class TesteAdicionarLista(unittest.TestCase):
    def test_adicionar_elemento(self):
        lista = [1, 2, 3]
        lista.append(4)
        self.assertIn(4, lista)

# 9 - Teste de Excluir Elemento em Lista
class TesteExcluirLista(unittest.TestCase):
    def test_excluir_elemento(self):
        lista = [1, 2, 3, 4]
        lista.remove(3)
        self.assertNotIn(3, lista)

# 10 - Teste de Multiplicação de Números
class TesteMultiplicacao(unittest.TestCase):
    def test_multiplicacao(self):
        self.assertEqual(3 * 3, 9)

# 11 - Teste de Concorrência de Strings
class TesteConcorrenciaStrings(unittest.TestCase):
    def test_strings_iguais(self):
        self.assertTrue("abc" == "abc")

# 12 - Teste de Verificação de Tipo
class TesteVerificacaoTipo(unittest.TestCase):
    def test_tipo_inteiro(self):
        self.assertIsInstance(10, int)

# 13 - Teste de String Vazia
class TesteStringVazia(unittest.TestCase):
    def test_string_vazia(self):
        self.assertEqual(len(""), 0)

# 14 - Teste de Substring
class TesteSubstring(unittest.TestCase):
    def test_substring(self):
        self.assertIn("abc", "abcdef")

# 15 - Teste de Ordem de Listas
class TesteOrdemLista(unittest.TestCase):
    def test_ordem_lista(self):
        lista = [1, 2, 3]
        self.assertEqual(sorted(lista), [1, 2, 3])

# 16 - Teste de Concatenação de Strings
class TesteConcatenacao(unittest.TestCase):
    def test_concatenacao(self):
        resultado = "Hello " + "World"
        self.assertEqual(resultado, "Hello World")

# 17 - Teste de Criação de Dicionário
class TesteCriacaoDicionario(unittest.TestCase):
    def test_criar_dicionario(self):
        dicionario = {"chave1": "valor1", "chave2": "valor2"}
        self.assertEqual(dicionario["chave1"], "valor1")

# 18 - Teste de Elemento em Dicionário
class TesteElementoDicionario(unittest.TestCase):
    def test_elemento_dicionario(self):
        dicionario = {"chave1": "valor1"}
        self.assertIn("chave1", dicionario)

# 19 - Teste de Modificação de Dicionário
class TesteModificarDicionario(unittest.TestCase):
    def test_modificar_dicionario(self):
        dicionario = {"chave": "valor"}
        dicionario["chave"] = "novo_valor"
        self.assertEqual(dicionario["chave"], "novo_valor")

# 20 - Teste de Tamanho de Dicionário
class TesteTamanhoDicionario(unittest.TestCase):
    def test_tamanho_dicionario(self):
        dicionario = {"chave1": "valor1", "chave2": "valor2"}
        self.assertEqual(len(dicionario), 2)

# 21 - Teste de Comparação de Dicionários
class TesteCompararDicionarios(unittest.TestCase):
    def test_comparar_dicionarios(self):
        dicionario1 = {"chave": "valor"}
        dicionario2 = {"chave": "valor"}
        self.assertDictEqual(dicionario1, dicionario2)

# 22 - Teste de Exceção Personalizada
class ExcecaoPersonalizada(Exception):
    pass

def funcao_erro():
    raise ExcecaoPersonalizada("Erro customizado")

class TesteExcecaoPersonalizada(unittest.TestCase):
    def test_excecao_personalizada(self):
        with self.assertRaises(ExcecaoPersonalizada):
            funcao_erro()

# 23 - Teste de Lista Não Vazia
class TesteListaNaoVazia(unittest.TestCase):
    def test_lista_nao_vazia(self):
        lista = [1, 2, 3]
        self.assertGreater(len(lista), 0)

# 24 - Teste de Round em Números Flutuantes
class TesteArredondamento(unittest.TestCase):
    def test_arredondamento(self):
        self.assertEqual(round(3.14159, 2), 3.14)

# 25 - Teste de Concorrência de Set
class TesteConcorrenciaSet(unittest.TestCase):
    def test_set_igual(self):
        self.assertSetEqual({1, 2, 3}, {3, 2, 1})

# 26 - Teste de Contagem de Elementos em Set
class TesteContagemSet(unittest.TestCase):
    def test_contar_set(self):
        conjunto = {1, 2, 3}
        self.assertEqual(len(conjunto), 3)

# 27 - Teste de Lista em Ordem Crescente
class TesteListaOrdemCrescente(unittest.TestCase):
    def test_lista_ordem_crescente(self):
        lista = [1, 2, 3]
        self.assertTrue(all(x < y for x, y in zip(lista, lista[1:])))

# 28 - Teste de Indexação de Lista
class TesteIndexacaoLista(unittest.TestCase):
    def test_indexacao_lista(self):
        lista = [1, 2, 3]
        self.assertEqual(lista[1], 2)

# 29 - Teste de Primeira e Última Posição em Lista
class TestePosicaoLista(unittest.TestCase):
    def test_posicao_lista(self):
        lista = [1, 2, 3]
        self.assertEqual(lista[0], 1)
        self.assertEqual(lista[-1], 3)

# 30 - Teste de Tipo de Dados em Dicionário
class TesteTipoDicionario(unittest.TestCase):
    def test_tipo_dicionario(self):
        dicionario = {"chave": 1}
        self.assertIsInstance(dicionario["chave"], int)

if __name__ == '__main__':
    unittest.main()
