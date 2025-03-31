"""
Calculadora Sencilla

Este programa permite al usuario ingresar dos operandos y seleccionar una operación
aritmética básica (suma, resta, multiplicación o división).

Autor: Juherles Bravo -jjbravor@academia.usbbog.edu.co-
Fecha: 2025-03-31
"""

def suma(a, b):
    """Retorna la suma de dos números."""
    return a + b

def resta(a, b):
    """Retorna la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Retorna la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Retorna la división de dos números. Si b es 0, muestra un error."""
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def main():
    """Función principal para manejar la calculadora."""
    print("> Ingrese el operando A:")
    operando_a = float(input("< "))
    
    print("> Ingrese el operando B:")
    operando_b = float(input("< "))
    
    print("> Cual operación se va a realizar?")
    print("> Escriba 1 para suma,")
    print(">         2 para resta,")
    print(">         3 para multiplicación,")
    print(">       y 4 para división.")
    
    opcion = input("< ")
    
    if opcion == "1":
        resultado = suma(operando_a, operando_b)
    elif opcion == "2":
        resultado = resta(operando_a, operando_b)
    elif opcion == "3":
        resultado = multiplicacion(operando_a, operando_b)
    elif opcion == "4":
        resultado = division(operando_a, operando_b)
    else:
        print("> Opcion no válida.")
        return
    
    print(f"> El resultado es: {resultado}")

if __name__ == "__main__":
    main()
