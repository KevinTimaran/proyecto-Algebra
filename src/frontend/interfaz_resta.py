import tkinter as tk
from tkinter import Frame, Label, messagebox
from backend.restarMatrices import restarMatrices
import os, sys

# === PATH DINÁMICO PARA IMPORTACIONES ===
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)

def interfaz_resta(parent, colores, fuentes):
    """
    Interfaz gráfica para la resta de matrices. 
    Este Frame se inyecta dentro del área principal.
    """
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    Label(
        frame,
        text="Resta de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # 🧱 Contenedor para todas las entradas
    contenido = Frame(frame, bg=colores['fondo_principal'])
    contenido.pack()

    # ========== ENTRADAS DE DIMENSIONES ==========
    Label(contenido, text="Filas:", bg=colores['fondo_principal'], font=fuentes['botones']).grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_filas = tk.Entry(contenido, width=5)
    entry_filas.grid(row=0, column=1, padx=5, pady=5)

    Label(contenido, text="Columnas:", bg=colores['fondo_principal'], font=fuentes['botones']).grid(row=0, column=2, padx=5, pady=5, sticky="e")
    entry_columnas = tk.Entry(contenido, width=5)
    entry_columnas.grid(row=0, column=3, padx=5, pady=5)

    # ========== FUNCIONES INTERNAS ==========

    def crear_entradas():
        try:
            filas = int(entry_filas.get())
            columnas = int(entry_columnas.get())
        except ValueError:
            messagebox.showerror("Error", "Filas y columnas deben ser números enteros.")
            return

        # Limpiar área de entradas previas si las hay
        for widget in frame.pack_slaves():
            if widget != contenido:
                widget.destroy()

        # Reagregar el título si se eliminó
        Label(
            frame,
            text="Resta de Matrices",
            bg=colores['fondo_principal'],
            fg=colores['titulo'],
            font=fuentes['titulo']
        ).pack(pady=(0, 20))

        matrices_frame = Frame(frame, bg=colores['fondo_principal'])
        matrices_frame.pack(pady=10)

        # ===== MATRIZ A =====
        matrizA_frame = Frame(matrices_frame, bg=colores['fondo_principal'])
        matrizA_frame.grid(row=0, column=0, padx=20)
        Label(matrizA_frame, text="Matriz A", bg=colores['fondo_principal'], font=fuentes['subtitulo']).pack()
        entradas_A = []
        for i in range(filas):
            fila = []
            fila_frame = Frame(matrizA_frame)
            fila_frame.pack()
            for j in range(columnas):
                e = tk.Entry(fila_frame, width=5)
                e.pack(side="left", padx=2, pady=2)
                fila.append(e)
            entradas_A.append(fila)

        # ===== MATRIZ B =====
        matrizB_frame = Frame(matrices_frame, bg=colores['fondo_principal'])
        matrizB_frame.grid(row=0, column=1, padx=20)
        Label(matrizB_frame, text="Matriz B", bg=colores['fondo_principal'], font=fuentes['subtitulo']).pack()
        entradas_B = []
        for i in range(filas):
            fila = []
            fila_frame = Frame(matrizB_frame)
            fila_frame.pack()
            for j in range(columnas):
                e = tk.Entry(fila_frame, width=5)
                e.pack(side="left", padx=2, pady=2)
                fila.append(e)
            entradas_B.append(fila)

        # ===== BOTÓN CALCULAR =====
        def calcular_resta():
            try:
                A = [[int(entradas_A[i][j].get()) for j in range(columnas)] for i in range(filas)]
                B = [[int(entradas_B[i][j].get()) for j in range(columnas)] for i in range(filas)]
            except ValueError:
                messagebox.showerror("Error", "Todos los campos deben tener números.")
                return

            resultado = restarMatrices(A, B)
            mostrar_resultado(resultado)

        tk.Button(frame, text="Calcular Resta", command=calcular_resta,
                  bg=colores['boton_normal'], fg=colores['texto_boton'],
                  activebackground=colores['boton_hover'],
                  relief="flat", font=fuentes['botones']).pack(pady=15)

        # ===== RESULTADO =====
        resultado_frame = Frame(frame, bg=colores['fondo_principal'])
        resultado_frame.pack()

        def mostrar_resultado(matriz):
            # Limpiar resultados anteriores
            for widget in resultado_frame.winfo_children():
                widget.destroy()
            Label(resultado_frame, text="Resultado:", bg=colores['fondo_principal'], font=fuentes['subtitulo']).pack()
            for fila in matriz:
                fila_texto = "   ".join(str(num) for num in fila)
                Label(resultado_frame, text=fila_texto, bg=colores['fondo_principal'], font=fuentes['botones']).pack()

    # ===== BOTÓN PARA CREAR ENTRADAS =====
    tk.Button(contenido, text="Siguiente", command=crear_entradas,
              bg=colores['boton_normal'], fg=colores['texto_boton'],
              activebackground=colores['boton_hover'],
              relief="flat", font=fuentes['botones']).grid(row=0, column=4, padx=10)

    return frame
