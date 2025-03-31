"""
Test unitario para el programa de Calculadora1

Este test verifica que cada operación básica de suma se realiza correctamente.

Autor: Juherles Bravo
Fecha: 2025-02-27
"""
import unittest
from Calculadora1.main import suma

class TestCalculadora1(unittest.TestCase):
    """Pruebas unitarias para la función suma de la Calculadora1."""

    def test_suma(self):
        """Verifica que la suma de dos números sea correcta."""
        self.assertEqual(suma(1, 10), 11)  # 1 + 10 = 11
        self.assertEqual(suma(1, -3), -2)  # 1 + (-3) = -2
        self.assertEqual(suma(1, 0), 1)    # 1 + 0 = 1
        self.assertEqual(suma(1, 5.5), 6.5) # 1 + 5.5 = 6.5

if __name__ == "__main__":
    unittest.main()
