"""
Programa de Calculadora de Matrices

Este programa ayuda a calcular matrices

Requisitos:
- Muestra resultados en formato de tabla
- Implementa validación de entradas
- Cumple con PEP8

Autor: Juherles Bravo
Fecha: 2025-05-04
"""

class Matriz:
    """Clase para representar y operar matrices 2x2."""

    def __init__(self, valores):
        """
        Inicializa una matriz 2x2.
        :param valores: Lista de listas 2x2 con valores numéricos.
        """
        if len(valores) != 2 or any(len(fila) != 2 for fila in valores):
            raise ValueError("La matriz debe ser de 2x2.")
        self.valores = valores

    def __add__(self, other):
        """Suma dos matrices 2x2."""
        return Matriz([
            [self.valores[0][0] + other.valores[0][0], self.valores[0][1] + other.valores[0][1]],
            [self.valores[1][0] + other.valores[1][0], self.valores[1][1] + other.valores[1][1]]
        ])

    def __sub__(self, other):
        """Resta dos matrices 2x2."""
        return Matriz([
            [self.valores[0][0] - other.valores[0][0], self.valores[0][1] - other.valores[0][1]],
            [self.valores[1][0] - other.valores[1][0], self.valores[1][1] - other.valores[1][1]]
        ])

    def __mul__(self, other):
        """Multiplica dos matrices 2x2."""
        a, b = self.valores, other.valores
        return Matriz([
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ])

    def __str__(self):
        """Representación en string de la matriz."""
        return f"|{self.valores[0][0]}  {self.valores[0][1]}|\n|{self.valores[1][0]}  {self.valores[1][1]}|"


def leer_matriz(num):
    """Solicita al usuario los valores de una matriz 2x2."""
    print(f"Ingrese los elementos de la Matriz {num}:")
    valores = []
    for i in range(2):
        fila = []
        for j in range(2):
            val = int(input(f"Matriz {num}: elemento {i},{j} > "))
            fila.append(val)
        valores.append(fila)
    return Matriz(valores)


def main():
    """Interfaz principal del programa."""
    m1 = leer_matriz(1)
    m2 = leer_matriz(2)

    print("\nMatriz 1:")
    print(m1)
    print("Matriz 2:")
    print(m2)

    print("\nEscriba 1 para suma,\n        2 para resta,\n        3 para multiplicación")
    opcion = input("> ")

    if opcion == "1":
        resultado = m1 + m2
        print("\nLa suma de las dos matrices es:")
    elif opcion == "2":
        resultado = m1 - m23
        print("\nLa resta de las dos matrices es:")
    elif opcion == "3":
        resultado = m1 * m2
        print("\nLa multiplicación de las dos matrices es:")
    else:
        print("Opción no válida.")
        return

    print(resultado)


if __name__ == "__main__":
    main()