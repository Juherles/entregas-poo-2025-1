"""
Programa para un saludo GUI

Aplicación gráfica en Python con Tkinter que permite ingresar un nombre 
y muestra un saludo personalizado al hacer clic en un botón. Incluye también 
botón para salir del programa.

Autor: Juherles Bravo
Fecha: 2025-05-16
"""
import tkinter as tk
from tkinter import messagebox


class AplicacionSaludo:
    """
    Clase principal que crea una aplicación gráfica con Tkinter
    para ingresar un nombre y mostrar un saludo personalizado.
    """

    def __init__(self, master):
        """
        Inicializa la ventana principal y todos los widgets.
        :param master: Objeto Tk raíz de la aplicación.
        """
        self.master = master
        master.title("Saludo con Tkinter")
        master.geometry("300x200")
        master.configure(bg="#e6f2ff")

        # Label para indicar el dato a ingresar
        self.label_nombre = tk.Label(
            master, text="Ingresa tu nombre:",
            font=("Arial", 12), bg="#e6f2ff"
        )
        self.label_nombre.pack(pady=10)

        # Entry para ingresar el nombre
        self.entry_nombre = tk.Entry(master, font=("Arial", 12))
        self.entry_nombre.pack(pady=5)

        # Botón para realizar el saludo
        self.boton_saludo = tk.Button(
            master, text="Saludar",
            command=self.saludar,
            bg="#4CAF50", fg="white",
            font=("Arial", 12)
        )
        self.boton_saludo.pack(pady=10)

        # Botón para salir de la aplicación
        self.boton_salir = tk.Button(
            master, text="Salir",
            command=master.quit,
            bg="#f44336", fg="white",
            font=("Arial", 12)
        )
        self.boton_salir.pack(pady=5)

    def saludar(self):
        """
        Función que obtiene el nombre del Entry y muestra un saludo
        en una ventana de mensaje.
        """
        nombre = self.entry_nombre.get().strip()
        if nombre:
            messagebox.showinfo("Saludo", f"Hola {nombre}")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un nombre.")


# Punto de entrada del programa
if __name__ == "__main__":
    ventana = tk.Tk()                # Instancia de la ventana raíz
    app = AplicacionSaludo(ventana)  # Instancia de la aplicación
    ventana.mainloop()               # Ejecuta el loop principal
