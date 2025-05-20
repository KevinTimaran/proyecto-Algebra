# src/frontend/interfaz_suma.py

import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
import os, sys

# Agrega el path para importar del backend
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)
if root_src_dir not in sys.path:
    sys.path.insert(0, root_src_dir)

try:
    from backend.sumaMatrices import crear_matriz, sumar_matrices
except ImportError:
    def crear_matriz(*a): return "Error importando crear_matriz"
    def sumar_matrices(*a): return "Error importando sumar_matrices"

def interfaz_suma(parent, colores, fuentes):
    """Interfaz gráfica para la suma de matrices."""
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=True, padx=30, pady=30)

    Label(frame, text="Suma de Matrices",
          bg=colores['fondo_principal'],
          fg=colores['titulo'],
          font=fuentes['titulo']).pack(pady=(0, 20))

    Label(frame, text="Tamaño de las matrices:",
          bg=colores['fondo_principal'],
          fg="#333",
          font=fuentes['subtitulo']).pack()

    entrada_frame = Frame(frame, bg=colores['fondo_principal'])
    entrada_frame.pack(pady=10)

    Label(entrada_frame, text="Filas:", bg=colores['fondo_principal']).grid(row=0, column=0)
    entry_filas = Entry(entrada_frame, width=5)
    entry_filas.grid(row=0, column=1, padx=10)

    Label(entrada_frame, text="Columnas:", bg=colores['fondo_principal']).grid(row=0, column=2)
    entry_columnas = Entry(entrada_frame, width=5)
    entry_columnas.grid(row=0, column=3)

    def generar_entradas():
        try:
            filas = int(entry_filas.get())
            columnas = int(entry_columnas.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")
            return

        # Limpiar si ya había widgets anteriores
        for widget in resultado_frame.winfo_children():
            widget.destroy()

        Label(resultado_frame, text="Matriz A", bg=colores['fondo_principal'], font=fuentes['subtitulo']).grid(row=0, column=0, pady=5)
        Label(resultado_frame, text="Matriz B", bg=colores['fondo_principal'], font=fuentes['subtitulo']).grid(row=0, column=1, pady=5)

        matrizA = []
        matrizB = []

        for i in range(filas):
            fila_A = []
            fila_B = []

            frameA = Frame(resultado_frame)
            frameA.grid(row=i+1, column=0, padx=10, pady=2)

            frameB = Frame(resultado_frame)
            frameB.grid(row=i+1, column=1, padx=10, pady=2)

            for j in range(columnas):
                eA = Entry(frameA, width=5)
                eA.pack(side="left", padx=2)
                fila_A.append(eA)

                eB = Entry(frameB, width=5)
                eB.pack(side="left", padx=2)
                fila_B.append(eB)

            matrizA.append(fila_A)
            matrizB.append(fila_B)

        def calcular_suma():
            datosA = [[e.get() for e in fila] for fila in matrizA]
            datosB = [[e.get() for e in fila] for fila in matrizB]

            matriz_1 = crear_matriz(filas, columnas, datosA)
            if isinstance(matriz_1, str):
                messagebox.showerror("Error", matriz_1)
                return

            matriz_2 = crear_matriz(filas, columnas, datosB)
            if isinstance(matriz_2, str):
                messagebox.showerror("Error", matriz_2)
                return

            resultado = sumar_matrices(matriz_1, matriz_2)
            if isinstance(resultado, str):
                messagebox.showerror("Error", resultado)
                return

            # Mostrar resultado
            for widget in matriz_resultado_frame.winfo_children():
                widget.destroy()

            Label(matriz_resultado_frame, text="Resultado:", bg=colores['fondo_principal'], font=fuentes['subtitulo']).pack()
            for fila in resultado:
                fila_str = "   ".join(str(num) for num in fila)
                Label(matriz_resultado_frame, text=fila_str, font=("Courier", 11), bg=colores['fondo_principal']).pack()

        Button(resultado_frame, text="Calcular Suma",
               bg=colores['boton_normal'], fg=colores['texto_boton'],
               activebackground=colores['boton_hover'], relief="flat",
               font=fuentes['botones'], command=calcular_suma).grid(row=filas+1, column=0, columnspan=2, pady=20)

    Button(frame, text="Generar Matrices",
           bg=colores['boton_normal'], fg=colores['texto_boton'],
           activebackground=colores['boton_hover'], relief="flat",
           font=fuentes['botones'], command=generar_entradas).pack(pady=10)

    resultado_frame = Frame(frame, bg=colores['fondo_principal'])
    resultado_frame.pack(pady=10)

    matriz_resultado_frame = Frame(frame, bg=colores['fondo_principal'])
    matriz_resultado_frame.pack()

    return frame


# Para pruebas individuales
if __name__ == "__main__":
    colores = {
        'fondo_principal': "#f8f9fa",
        'boton_normal': "#495057",
        'boton_hover': "#343a40",
        'texto_boton': "#ffffff",
        'titulo': "#d62828"
    }

    fuentes = {
        'titulo': ("Segoe UI", 16, "bold"),
        'subtitulo': ("Segoe UI", 12),
        'botones': ("Segoe UI", 10)
    }

    root = tk.Tk()
    root.geometry("900x650")
    interfaz_suma(root, colores, fuentes)
    root.mainloop()
