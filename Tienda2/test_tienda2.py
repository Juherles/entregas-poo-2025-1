import unittest
from main import Producto


class TestProducto(unittest.TestCase):
    """Test para la clase Producto."""

    def test_creacion_producto(self):
        """Verifica que el producto se cree con los atributos correctos."""
        producto = Producto(
            "pan", 2000, 10, "pan tajado marca bimbo", "alimentación"
        )
        self.assertEqual(producto.nombre, "pan")
        self.assertEqual(producto.precio, 2000)
        self.assertEqual(producto.cantidad, 10)
        self.assertEqual(producto.descripcion, "pan tajado marca bimbo")
        self.assertEqual(producto.clasificacion, "alimentación")

    def test_mostrar_producto(self):
        """Verifica que mostrar_producto devuelva el formato esperado."""
        producto = Producto(
            "pan", 2000, 10, "pan tajado marca bimbo", "alimentación"
        )
        esperado = (
            "|pan            "
            "|10 unidades    "
            "|2000 pesos     "
            "|pan tajado marca bim"
            "|alimentación   |"
        )
        self.assertEqual(producto.mostrar_producto(), esperado)


if __name__ == "__main__":
    unittest.main()
