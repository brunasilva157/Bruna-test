import unittest

class TestCicloDeVida(unittest.TestCase):

    def setUp(self):
        # Executado ANTES de cada teste
        print("\n[setUp] Preparando o ambiente")

    def test_um(self):
        print("Executando teste 01.")

    def test_dois(self):
        print("Executando teste 02.")

    def test_tres(self):
        print("Executando teste 03.")

    def tearDown(self):
        # Executado DEPOIS de cada teste
        print("[tearDown] Limpando")

if __name__ == "__main__":
    unittest.main()