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

if __name__ == '__main__':
    unittest.main()
