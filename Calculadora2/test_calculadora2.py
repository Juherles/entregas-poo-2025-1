"""
Test unitario para el programa de Calculadora2

Este test agrega validaciones para las nuevas operaciones y la gestión de errores.

Autor: Juherles Bravo
Fecha: 2025-02-27
"""
import unittest
from Calculadora2.main import realizar_operacion

class TestCalculadora2(unittest.TestCase):
    """Pruebas unitarias para la Calculadora2."""

    def test_division(self):
        """Verifica que la división de dos números sea correcta."""
        self.assertEqual(realizar_operacion(4, 10, 2), 5.0)
        self.assertEqual(realizar_operacion(4, 9, 3), 3.0)
        self.assertEqual(realizar_operacion(4, 7, 2), 3.5)
        self.assertEqual(realizar_operacion(4, 5, 0), "Error: División por cero")

if __name__ == "__main__":
    unittest.main()
