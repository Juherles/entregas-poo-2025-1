import unittest
from Calcmat import Matriz  # <- Asegúrate de que el nombre del archivo es correcto

class TestMatriz(unittest.TestCase):
    def test_suma(self):
        m1 = Matriz([[1, 2], [3, 4]])
        m2 = Matriz([[5, 6], [7, 8]])
        resultado = m1 + m2
        self.assertEqual(resultado.valores, [[6, 8], [10, 12]])

if __name__ == "__main__":
    unittest.main()
