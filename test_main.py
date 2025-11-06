import unittest
# Importa as funções do seu arquivo principal
from main import somar, subtrair, multiplicar, dividir 

class TestCalculadora(unittest.TestCase):
    
    def test_somar(self):
        # Testa se 5 + 5 = 10
        self.assertEqual(somar(5, 5), 10)

    def test_subtrair(self):
        # Testa se 10 - 3 = 7
        self.assertEqual(subtrair(10, 3), 7)

    def test_multiplicar(self):
        # Testa se 4 * 3 = 12
        self.assertEqual(multiplicar(4, 3), 12)

    def test_dividir_sucesso(self):
        # Testa divisão normal
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_zero(self):
        # Testa a exceção para divisão por zero
        self.assertEqual(dividir(10, 0), "Erro: Divisão por zero")

if __name__ == '__main__':
    unittest.main()
