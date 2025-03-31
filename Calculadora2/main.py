"""
Calculadora mejorada

Este programa permite al usuario ingresar dos operandos y seleccionar una operación
aritmética básica (suma, resta, multiplicación, división potenciacion, division entera, modulo).

Con soporte para múltiples operaciones,
validación de entrada y cancelación de operaciones.

Autor: Juherles Bravo -jjbravor@academia.usbbog.edu.co-
Fecha: 2025-03-31
"""
def obtener_operando(mensaje):
    """Solicita un operando al usuario y maneja errores de entrada."""
    while True:
        entrada = input(mensaje)
        if entrada == "":
            print("> Operación cancelada")
            return None
        try:
            return float(entrada)
        except ValueError:
            print("> Dato inválido, por favor ingrese un número válido.")

def realizar_operacion(operacion, a, b):
    """Realiza la operación matemática seleccionada."""
    if operacion == 1:
        return a + b, "suma"
    elif operacion == 2:
        return a - b, "resta"
    elif operacion == 3:
        return a * b, "multiplicación"
    elif operacion == 4:
        return a / b if b != 0 else "Error: División por cero", "división"
    elif operacion == 5:
        return a ** b, "potenciación"
    elif operacion == 6:
        return int(a) // int(b) if b != 0 else "Error: División por cero", "división entera"
    elif operacion == 7:
        return int(a) % int(b) if b != 0 else "Error: Módulo por cero", "módulo"

def main():
    """Función principal para manejar la calculadora interactiva."""
    while True:
        print("> Escriba 1 para suma,\n"
              ">         2 para resta,\n"
              ">         3 para multiplicación,\n"
              ">         4 para división,\n"
              ">         5 para potenciación,\n"
              ">         6 para división entera,\n"
              ">         7 para módulo,\n"
              ">         8 para salir.")
        try:
            operacion = int(input("< "))
            if operacion == 8:
                print("> Gracias!")
                break
            elif operacion not in range(1, 8):
                print("> Opción inválida, intente nuevamente.")
                continue
        except ValueError:
            print("> Entrada inválida, ingrese un número del 1 al 8.")
            continue

        a = obtener_operando("> Ingrese el operando A (vacío para cancelar):\n< ")
        if a is None:
            continue

        b = obtener_operando("> Ingrese el operando B (vacío para cancelar):\n< ")
        if b is None:
            continue

        resultado, nombre_operacion = realizar_operacion(operacion, a, b)
        print(f"> El resultado de la {nombre_operacion} es: {resultado}")

if __name__ == "__main__":
    main()