import unittest
from main import Mascota, Perro, Gato


class TestMascotas(unittest.TestCase):
    """Pruebas unitarias para la gestión de mascotas."""

    def test_creacion_mascota(self):
        """Verifica la creación de una mascota genérica."""
        mascota = Mascota("Max", 4, "Pastor Alemán")
        self.assertEqual(mascota.nombre, "Max")
        self.assertEqual(mascota.edad, 4)
        self.assertEqual(mascota.raza, "Pastor Alemán")

    def test_creacion_perro(self):
        """Verifica la creación de un perro con el atributo 'clase'."""
        perro = Perro("Motas", 2, "Labrador")
        self.assertEqual(perro.nombre, "Motas")
        self.assertEqual(perro.edad, 2)
        self.assertEqual(perro.raza, "Labrador")
        self.assertEqual(perro.clase, "Perro")

    def test_creacion_gato(self):
        """Verifica la creación de un gato con el atributo 'clase'."""
        gato = Gato("Whiskers", 3, "Siamés")
        self.assertEqual(gato.nombre, "Whiskers")
        self.assertEqual(gato.edad, 3)
        self.assertEqual(gato.raza, "Siamés")
        self.assertEqual(gato.clase, "Gato")


if __name__ == "__main__":
    unittest.main()