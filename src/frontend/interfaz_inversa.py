# src/frontend/interfaz_inversa.py

import tkinter as tk
from tkinter import messagebox
import os, sys

# ===== Agrega el path al backend =====
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)

if root_src_dir not in sys.path:
    sys.path.insert(0, root_src_dir)

# ===== Importaciones del backend =====
try:
    from backend.calcularInversa import matriz_inversa_2x2, matriz_inversa_3x3
except ImportError as e:
    print("⚠️ Error de importación:", e)
    def matriz_inversa_2x2(*args, **kwargs):
        messagebox.showerror("Error", "No se pudo importar la función matriz_inversa_2x2.")
        return None
    def matriz_inversa_3x3(*args, **kwargs):
        messagebox.showerror("Error", "No se pudo importar la función matriz_inversa_3x3.")
        return None

# ===== Interfaz integrada a la aplicación principal =====
def interfaz_inversa(parent, colores, fuentes):
    """
    Crea la interfaz de usuario para calcular la inversa de matrices 2x2 o 3x3.
    Se adapta visualmente al estilo general del sistema.
    """
    frame = tk.Frame(parent, bg=colores['fondo_principal'])
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # 🏷️ Título
    tk.Label(
        frame, text="Cálculo de Inversa de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # 🔘 Selección del tamaño
    tk.Label(
        frame, text="Seleccione el tamaño de la matriz:",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['subtitulo']
    ).pack()

    opcion = tk.IntVar(value=2)
    radio_frame = tk.Frame(frame, bg=colores['fondo_principal'])
    radio_frame.pack(pady=5)
    tk.Radiobutton(radio_frame, text="2x2", variable=opcion, value=2,
                   bg=colores['fondo_principal'], font=fuentes['botones'],
                   command=lambda: crear_entradas(opcion.get())).pack(side="left", padx=10)
    tk.Radiobutton(radio_frame, text="3x3", variable=opcion, value=3,
                   bg=colores['fondo_principal'], font=fuentes['botones'],
                   command=lambda: crear_entradas(opcion.get())).pack(side="left", padx=10)

    # 📥 Entradas de matriz
    marco_entradas = tk.Frame(frame, bg=colores['fondo_principal'])
    marco_entradas.pack(pady=10)
    entradas = []

    def crear_entradas(n):
        # Limpia entradas anteriores
        for widget in marco_entradas.winfo_children():
            widget.destroy()
        entradas.clear()

        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(marco_entradas, width=6, font=fuentes['botones'])
                e.grid(row=i, column=j, padx=5, pady=5)
                fila.append(e)
            entradas.append(fila)

    crear_entradas(2)  # Tamaño por defecto

    # 🧮 Resultado
    resultado_var = tk.StringVar()
    resultado_label = tk.Label(frame, textvariable=resultado_var,
                               bg=colores['fondo_principal'],
                               fg="#000", font=("Courier", 12), justify="left")
    resultado_label.pack(pady=10)

    def calcular():
        try:
            matriz = [[float(e.get()) for e in fila] for fila in entradas]
            if len(matriz) == 2:
                inversa = matriz_inversa_2x2(matriz)
            elif len(matriz) == 3:
                inversa = matriz_inversa_3x3(matriz)
            else:
                resultado_var.set("Solo se permiten matrices 2x2 o 3x3.")
                return

            if isinstance(inversa, str):
                resultado_var.set(inversa)
            else:
                texto = "\n".join(["   ".join(f"{x:.2f}" for x in fila) for fila in inversa])
                resultado_var.set(f"Resultado:\n{texto}")

        except Exception as e:
            resultado_var.set("Error al procesar los datos.")
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    # 🚀 Botón de cálculo
    tk.Button(
        frame, text="Calcular Inversa",
        command=calcular,
        bg=colores['boton_normal'],
        fg=colores['texto_boton'],
        font=fuentes['botones'],
        activebackground=colores['boton_hover'],
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)

    return frame
