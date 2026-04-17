import unittest


def somar_numeros (a,b):

    return a+b
 

class matematica(unittest.TestCase):

    def test_somar_numeros_correta(self):
        
        self.assertEqual(somar_numeros(2,2),5, "a soma deveria ser 5")


if __name__ == "__main__":
    unittest.main()