# src/frontend/interfaz_operaciones_combinadas.py

import tkinter as tk
from tkinter import ttk, messagebox
import os, sys

# ===== Agrega el path para importar backend si es necesario =====
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)

if root_src_dir not in sys.path:
    sys.path.insert(0, root_src_dir)

# ===== Intenta importar desde el backend =====
try:
    from backend.matricesOperacionesCombinadas import operacion_combinada, es_matriz_valida
except ImportError as e:
    print("⚠️ Error de importación:", e)
    def operacion_combinada(*args, **kwargs):
        messagebox.showerror("Error", "No se pudo importar la función operacion_combinada.")
        return None
    def es_matriz_valida(_):
        return False, "Error: No se pudo validar la matriz."

# ===== INTERFAZ COMPATIBLE CON ESTILO GLOBAL DE LA APP PRINCIPAL =====
def interfazOperacionesCombinadas(parent, colores, fuentes):
    """
    Módulo gráfico reutilizable para la operación combinada αA + βB
    Parámetros:
    - parent: frame contenedor (área principal)
    - colores: diccionario de colores compartido
    - fuentes: diccionario de fuentes compartido
    """
    # 🧱 Contenedor base
    frame = tk.Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # 🏷️ Título
    tk.Label(frame, text="Operación Combinada αA + βB",
             bg=colores['fondo_principal'], fg=colores['titulo'],
             font=fuentes['titulo']).pack(pady=(0, 20))

    # 🧮 Instrucciones
    tk.Label(frame, text="Ingresa dos matrices (usando ; para filas y , o espacio para columnas)",
             bg=colores['fondo_principal'], fg="#495057",
             font=fuentes['subtitulo']).pack(pady=(0, 15))

    # 📥 Entradas
    def etiqueta(texto):
        return tk.Label(frame, text=texto, bg=colores['fondo_principal'],
                        fg="#212529", font=fuentes['botones'])

    etiqueta("Matriz A:").pack(anchor="w", padx=5)
    entry_A = tk.Entry(frame, width=50)
    entry_A.insert(0, "1,2;3,4")
    entry_A.pack(pady=(0, 10))

    etiqueta("Escalar α:").pack(anchor="w", padx=5)
    entry_alpha = tk.Entry(frame, width=10)
    entry_alpha.insert(0, "1")
    entry_alpha.pack(pady=(0, 10))

    etiqueta("Matriz B:").pack(anchor="w", padx=5)
    entry_B = tk.Entry(frame, width=50)
    entry_B.insert(0, "5,6;7,8")
    entry_B.pack(pady=(0, 10))

    etiqueta("Escalar β:").pack(anchor="w", padx=5)
    entry_beta = tk.Entry(frame, width=10)
    entry_beta.insert(0, "1")
    entry_beta.pack(pady=(0, 20))

    # 📤 Resultado
    resultado_var = tk.StringVar()
    resultado_label = tk.Label(frame, textvariable=resultado_var,
                               bg=colores['fondo_principal'], fg="#000",
                               font=fuentes['botones'], justify="left", anchor="w")
    resultado_label.pack(pady=(10, 5), anchor="w")

    # 🧠 Funciones internas
    def parsear_matriz(cadena):
        try:
            matriz = []
            filas = cadena.strip().split(';')
            num_columnas = -1
            for fila_raw in filas:
                fila_str = fila_raw.strip().replace(',', ' ')
                elementos = [float(x) for x in fila_str.split()]
                if num_columnas == -1:
                    num_columnas = len(elementos)
                elif len(elementos) != num_columnas:
                    return None, "Filas con diferentes columnas."
                matriz.append(elementos)
            valida, msg = es_matriz_valida(matriz)
            if not valida: return None, msg
            return matriz, None
        except ValueError:
            return None, "Hay valores no numéricos."

    def parsear_escalar(txt):
        try: return float(txt)
        except ValueError: return None

    def calcular():
        A, errA = parsear_matriz(entry_A.get())
        B, errB = parsear_matriz(entry_B.get())
        alpha = parsear_escalar(entry_alpha.get())
        beta = parsear_escalar(entry_beta.get())

        if errA:
            messagebox.showerror("Error en A", errA)
            resultado_var.set(errA)
            return
        if errB:
            messagebox.showerror("Error en B", errB)
            resultado_var.set(errB)
            return
        if alpha is None:
            messagebox.showerror("Escalar α inválido", "Debe ser numérico.")
            return
        if beta is None:
            messagebox.showerror("Escalar β inválido", "Debe ser numérico.")
            return

        resultado = operacion_combinada(alpha, A, beta, B)
        if resultado is None:
            resultado_var.set("Error durante el cálculo.")
            return

        # Formatear salida
        if not resultado:
            resultado_var.set("Resultado vacío.")
        else:
            resultado_formateado = "\n".join(
                ["  ".join(f"{num:.2f}" for num in fila) for fila in resultado]
            )
            resultado_var.set(f"Resultado:\n{resultado_formateado}")

    # 🚀 Botón
    tk.Button(frame, text="Calcular αA + βB",
              bg=colores['boton_normal'], fg=colores['texto_boton'],
              font=fuentes['botones'], relief="flat",
              activebackground=colores['boton_hover'],
              cursor="hand2",
              command=calcular).pack(pady=10)

    return frame  # Retornamos el frame si se desea manipular más tarde
