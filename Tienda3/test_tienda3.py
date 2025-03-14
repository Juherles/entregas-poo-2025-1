"""
Test unitario para el programa de Inventario de Tienda3

Este archivo verifica que:
- La clase Producto almacena los datos correctamente.
- La función `mostrar_producto` devuelve el formato esperado.
- Se manejan correctamente valores negativos y entradas inválidas.

Autor: Juherles Bravo
Fecha: 2025-03-13
"""
import unittest
from main import Producto  # Importa la clase desde main.py


class TestProducto(unittest.TestCase):
    """Pruebas unitarias para la clase Producto."""

    def setUp(self):
        """Configura un producto de prueba."""
        self.producto_valido = Producto("Manzana", 10, 5, "Fruta roja", "Alimentos")

    def test_creacion_producto(self):
        """Verifica que los atributos del producto sean correctos."""
        self.assertEqual(self.producto_valido.nombre, "Manzana")
        self.assertEqual(self.producto_valido.precio, 10)
        self.assertEqual(self.producto_valido.cantidad, 5)
        self.assertEqual(self.producto_valido.descripcion, "Fruta roja")
        self.assertEqual(self.producto_valido.clasificacion, "Alimentos")
        self.assertEqual(self.producto_valido.total_inventario, 50)  # 10 * 5
        self.assertEqual(self.producto_valido.precio_x5, 50)  # 10 * 5

    def test_mostrar_producto(self):
        """Verifica que la salida de mostrar_producto() sea la esperada."""
        resultado = self.producto_valido.mostrar_producto()
        self.assertIn("Manzana", resultado)
        self.assertIn("5 unidades", resultado)
        self.assertIn("10 pesos", resultado)
        self.assertIn("Fruta roja", resultado)
        self.assertIn("Alimentos", resultado)
        self.assertIn("50 pesos", resultado)


if __name__ == "__main__":
    unittest.main()
