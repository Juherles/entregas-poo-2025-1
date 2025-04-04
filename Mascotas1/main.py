"""
Programa de registro de mascotas en una veterinaria

Este programa nos permite ingresar los datos basicos de una mascota como
clase, edad, nombre, raza y registra automaticamente la fecha en la que
se registraron los datos.

Autor: Juherles Bravo
Fecha: 2025-02-27
"""
from datetime import datetime


class Mascota:
    """Clase base para representar una mascota."""

    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

    def obtener_info(self):
        """Devuelve la información de la mascota en formato de tabla."""
        return [self.clase,
                self.nombre,
                f"{self.edad} años",
                self.raza,
                self.fecha_ingreso]


class Perro(Mascota):
    """Clase que representa un perro, hereda de Mascota."""

    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
        self.clase = "Perro"


class Gato(Mascota):
    """Clase que representa un gato, hereda de Mascota."""

    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
        self.clase = "Gato"


def ingresar_mascotas():
    """Función para ingresar mascotas desde la consola."""
    mascotas = []
    cantidad = int(input("¿Cuántas mascotas va a ingresar?\n> "))

    for i in range(1, cantidad + 1):
        tipo = input(
            f"Mascota {i}, ¿qué clase es (P)erro o (G)ato?\n> ").strip().lower()
        nombre = input(
            f"¿Cuál es el nombre del {
                'Perro' if tipo == 'p' else 'Gato'}?\n> ").strip()
        edad = int(input(f"¿Qué edad tiene '{nombre}'?\n> "))
        raza = input(f"¿De qué raza es '{nombre}'?\n> ").strip()

        if tipo == 'p':
            mascota = Perro(nombre, edad, raza)
        elif tipo == 'g':
            mascota = Gato(nombre, edad, raza)
        else:
            print("Entrada no válida. Intente de nuevo.")
            continue

        mascotas.append(mascota)

    return mascotas


def mostrar_resumen(mascotas):
    """Muestra el resumen de mascotas en formato de tabla."""
    print("\nResumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    print("|------|---------|------|-------------|--------------------------|")
    for mascota in mascotas:
        print(
            f"|{
                mascota.obtener_info()[0]:<6} |{
                mascota.obtener_info()[1]:<8} |{
                mascota.obtener_info()[2]:<6} |{
                    mascota.obtener_info()[3]:<12} |{
                        mascota.obtener_info()[4]}|")


if __name__ == "__main__":
    mascotas_registradas = ingresar_mascotas()
    mostrar_resumen(mascotas_registradas)
