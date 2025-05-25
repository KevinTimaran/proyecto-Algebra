import tkinter as tk
from tkinter import messagebox, StringVar, ttk
import os, sys

# === Asegurar ruta al backend ===
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)
if root_src_dir not in sys.path:
    sys.path.append(root_src_dir)

# === Importar funciones del backend ===
try:
    from backend.resolucionSistemas import resolver_cramer, determinante_sarrus, matriz_de_cofactores
except ImportError:
    def resolver_cramer(A, B): return "Error de importación"
    def determinante_sarrus(A): return "Error de importación"
    def matriz_de_cofactores(A): return "Error de importación"

def interfaz_sistemas_general(parent, colores, fuentes):
    frame = tk.Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(frame, text="Resolución de Sistemas Lineales (n x n)",
             bg=colores['fondo_principal'], fg=colores['titulo'],
             font=fuentes['titulo']).pack(pady=10)

    top_frame = tk.Frame(frame, bg=colores['fondo_principal'])
    top_frame.pack()

    # Selección de método
    metodo_var = StringVar(value="Cramer")
    ttk.Label(top_frame, text="Método:", background=colores['fondo_principal']).pack(side="left", padx=5)
    metodo_menu = ttk.Combobox(top_frame, textvariable=metodo_var, values=["Cramer", "Sarrus", "Cofactores"], state="readonly", width=15)
    metodo_menu.pack(side="left", padx=5)

    # Tamaño del sistema
    tk.Label(top_frame, text="Tamaño n:", bg=colores['fondo_principal']).pack(side="left", padx=5)
    entry_n = tk.Entry(top_frame, width=4)
    entry_n.insert(0, "3")
    entry_n.pack(side="left", padx=5)

    # Área para entradas dinámicas
    entradas_frame = tk.Frame(frame, bg=colores['fondo_principal'])
    entradas_frame.pack(pady=10)

    resultado_var = tk.StringVar()
    tk.Label(frame, textvariable=resultado_var, bg=colores['fondo_principal'],
             fg="#000", font=fuentes['botones'], justify="left").pack(pady=10)

    def construir_formulario():
        for widget in entradas_frame.winfo_children():
            widget.destroy()

        try:
            n = int(entry_n.get())
            if n <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "n debe ser un número entero positivo.")
            return

        tk.Label(entradas_frame, text="Coeficientes de la matriz A:", bg=colores['fondo_principal'], font=fuentes['botones']).grid(row=0, column=0, columnspan=n)
        entries_A = []
        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(entradas_frame, width=5)
                e.grid(row=i + 1, column=j, padx=2, pady=2)
                fila.append(e)
            entries_A.append(fila)

        tk.Label(entradas_frame, text="Términos independientes (B):", bg=colores['fondo_principal'], font=fuentes['botones']).grid(row=0, column=n + 1)
        entries_B = []
        for i in range(n):
            e = tk.Entry(entradas_frame, width=5)
            e.grid(row=i + 1, column=n + 1, padx=5)
            entries_B.append(e)

        def leer_matriz(entries):
            try:
                return [[float(e.get()) for e in fila] for fila in entries], None
            except ValueError:
                return None, "Todos los valores en la matriz deben ser numéricos."

        def leer_vector(entries):
            try:
                return [float(e.get()) for e in entries], None
            except ValueError:
                return None, "Todos los valores en el vector deben ser numéricos."

        def calcular():
            A, errA = leer_matriz(entries_A)
            B, errB = leer_vector(entries_B)
            metodo = metodo_var.get()

            for widget in entradas_frame.winfo_children():
                widget.update()

            if errA:
                messagebox.showerror("Error en matriz A", errA)
                return
            if errB:
                messagebox.showerror("Error en vector B", errB)
                return

            if len(A) != len(A[0]):
                messagebox.showerror("Error", "La matriz A debe ser cuadrada.")
                return
            if len(B) != len(A):
                messagebox.showerror("Error", "El vector B debe tener la misma cantidad de filas que A.")
                return

            resultado_var.set("")  # limpiar

            if metodo == "Cramer":
                resultado = resolver_cramer(A, B)
                if isinstance(resultado, str):
                    resultado_var.set(resultado)
                else:
                    texto = f"Determinante |A|: {resultado['det_A']}\n"
                    texto += "\n".join([f"x{i + 1} = {val}" for i, val in enumerate(resultado['solucion'])])
                    resultado_var.set(texto)

            elif metodo == "Sarrus":
                if len(A) != 3:
                    messagebox.showwarning("Método no válido", "Sarrus solo se aplica a sistemas 3x3.")
                    return
                det = determinante_sarrus(A)
                resultado_var.set(f"Determinante por Sarrus: {det}")

            elif metodo == "Cofactores":
                if len(A) != 3:
                    messagebox.showwarning("Método no válido", "Cofactores solo se aplica a matrices 3x3.")
                    return
                cof = matriz_de_cofactores(A)
                texto = "Matriz de Cofactores:\n" + "\n".join(str(fila) for fila in cof)
                resultado_var.set(texto)

        tk.Button(entradas_frame, text="Calcular",
                  bg=colores['boton_normal'], fg=colores['texto_boton'],
                  font=fuentes['botones'], relief="flat",
                  activebackground=colores['boton_hover'],
                  cursor="hand2", command=calcular).grid(row=n + 2, columnspan=n + 2, pady=10)

    # Reconstruir formulario al cambiar método o tamaño
    metodo_menu.bind("<<ComboboxSelected>>", lambda e: construir_formulario())
    entry_n.bind("<Return>", lambda e: construir_formulario())
    construir_formulario()

    return frame
