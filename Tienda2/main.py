"""
Programa de Inventario de Tienda

Este programa solicita al usuario ingresar productos con su nombre, precio, cantidad descripcion y clase.
Luego, muestra un resumen en formato de tabla.

Requisitos:
- Usa una clase `Producto`
- Solicita datos de productos
- Muestra resultados en formato de tabla
- Implementa validación de entradas
- Cumple con PEP8

Autor: Juherles Bravo <jjbravor@academia.usbbog.edu.co
Fecha: 2025-03-06
"""

class Producto:
    """Clase que representa un producto de la tienda."""

    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        """
        Inicializar el producto con sus atributos.

        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        :param descripcion: Descripción del producto.
        :param clasificacion: Clasificación del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def mostrar_producto(self):
        """
        Devuelve el producto formateado para el resumen.

        :return: Cadena con los datos del producto alineados.
        """
        return (
            f"|{self.nombre:<15}"
            f"|{str(self.cantidad) + ' unidades':<15}"
            f"|{str(self.precio) + ' pesos':<15}"
            f"|{self.descripcion[:20]:<20}"
            f"|{self.clasificacion:<15}|"
        )


def main():
    """
    Función principal para manejar el inventario.

    Permite ingresar productos, mostrarlos y calcular
    precios por clasificación.
    """
    productos = []
    total_clasificacion = {}

    print("> ¿Cuántos productos va a ingresar?")
    cantidad_productos = int(input("< "))

    for i in range(cantidad_productos):
        print(f"> Producto {i + 1}, ¿cuál es el nombre?")
        nombre = input("< ")

        print(f"> ¿Cuál es el precio de '{nombre}'?")
        precio = int(input("< "))

        print(f"> ¿Qué cantidad hay de '{nombre}'?")
        cantidad = int(input("< "))

        print(f"> Introduzca la descripción de '{nombre}':")
        descripcion = input("< ")

        print(f"> ¿Qué clasificación tiene '{nombre}'?")
        clasificacion = input("< ")

        producto = Producto(
            nombre, precio, cantidad, descripcion, clasificacion
        )
        productos.append(producto)

        if clasificacion in total_clasificacion:
            total_clasificacion[clasificacion] += precio
        else:
            total_clasificacion[clasificacion] = precio

    print("> Resumen:")
    print(
        "|Producto       |Cantidad       |Precio         |Descripción           |Clasificación   |"
    )
    for producto in productos:
        print(producto.mostrar_producto())

    print("\n> Precios por clasificación")
    print("|Clasificación   |Precio         |")
    for clasificacion, total in total_clasificacion.items():
        print(f"|{clasificacion:<16}|{str(total) + ' pesos':<15}|")


if __name__ == "__main__":
    main()
