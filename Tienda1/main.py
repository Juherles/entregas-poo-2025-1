#!/usr/bin/env python3

"""
Programa de Inventario de Tienda

Este programa solicita al usuario ingresar tres productos con su nombre, precio y cantidad.
Luego, muestra un resumen en formato de tabla.

Requisitos:
- Usa una clase `Product`
- Solicita datos de 3 productos
- Muestra resultados en formato de tabla
- Implementa validación de entradas
- Cumple con PEP8

Autor: Juherles Bravo
Fecha: 2025-02-27
"""


class Product:
    """Clase para representar un producto en la tienda"""

    def __init__(self, name, price, quantity):
        """Inicializa un producto con nombre, precio y cantidad"""
        self.name = name
        self.price = price
        self.quantity = quantity

    def format_info(self):
        """Devuelve el producto formateado en una tabla"""
        return f"|{
            self.name:<10}|{
            self.quantity:<10} unidades |{
            self.price:<10} pesos |"


def get_product(index):
    """
    Pide al usuario los datos de un producto y valida la entrada.

    :param index: Número del producto (1, 2 o 3)
    :return: Un objeto Product con los datos ingresados
    """
    print(f"\nProducto {index}, ¿cuál es el nombre?")
    name = input("> ").strip()

    # Validar precio
    while True:
        try:
            price = int(
                input(
                    f"> ¿Cuál es el precio de '{name}'? (en COP)\n> "))
            if price < 0:
                raise ValueError
            break
        except ValueError:
            print("⚠️ Entrada inválida. Ingresa un número positivo.")

    # Validar cantidad
    while True:
        try:
            quantity = int(input(f"> ¿Qué cantidad hay de '{name}'?\n> "))
            if quantity < 0:
                raise ValueError
            break
        except ValueError:
            print("⚠️ Entrada inválida. Ingresa un número positivo.")

    return Product(name, price, quantity)


def run():
    """Función principal del programa"""
    products = []  # Lista para almacenar productos

    # Pedir datos de 3 productos
    for i in range(1, 4):
        product = get_product(i)
        products.append(product)

    # Mostrar resumen
    print("\nResumen:")
    print("|Producto  |Cantidad  |Precio      |")
    print("|----------|----------|------------|")
    for product in products:
        print(product.format_info())


# Punto de entrada del programa
if __name__ == "__main__":
    run()
