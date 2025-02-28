"""
Test unitario para el programa de Inventario de Tienda

Este archivo verifica que:
- La clase Product almacena los datos correctamente.
- La función `format_info` devuelve el formato esperado.
- Se manejan correctamente valores negativos y entradas inválidas.

Autor: Juherles
Fecha: 2025-02-27
"""

import unittest
from main import Product


class TestProduct(unittest.TestCase):
    """Clase de pruebas para la clase Product"""

    def test_product_creation(self):
        """Prueba la creación de un producto"""
        product = Product("pan", 2000, 10)
        self.assertEqual(product.name, "pan")
        self.assertEqual(product.price, 2000)
        self.assertEqual(product.quantity, 10)

    def test_format_info(self):
        """Prueba el formato de salida de un producto"""
        product = Product("leche", 5000, 15)
        expected_output = "|leche     |15        unidades |5000       pesos |"
        self.assertEqual(product.format_info(), expected_output)

    def test_negative_price(self):
        """Prueba que un precio negativo no sea válido"""
        with self.assertRaises(ValueError):
            Product("huevo", -500, 200)

    def test_negative_quantity(self):
        """Prueba que una cantidad negativa no sea válida"""
        with self.assertRaises(ValueError):
            Product("arroz", 1000, -5)


# Punto de entrada para ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
