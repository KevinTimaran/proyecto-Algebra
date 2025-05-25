import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox, StringVar, OptionMenu
import os, sys

# === Asegurar ruta al backend ===
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)
if root_src_dir not in sys.path:
    sys.path.append(root_src_dir)

# === Intentar importar lógica ===
try:
    from backend.resolucionSistemas import (
        resolver_cramer,
        determinante_sarrus,
        matriz_de_cofactores
    )
except ImportError:
    def resolver_cramer(A, B): return "Error de importación"
    def determinante_sarrus(A): return "Error de importación"
    def matriz_de_cofactores(A): return "Error de importación"

def interfaz_sistemas(parent, colores, fuentes):
    frame = Frame(parent, bg=colores['fondo_principal'], width=760, height=700)
    frame.pack(padx=30, pady=30)
    frame.pack_propagate(False)

    Label(frame, text="Resolución de Sistemas Lineales",
          bg=colores['fondo_principal'], fg=colores['titulo'], font=fuentes['titulo']
    ).pack(pady=(0, 20))

    entrada_frame = Frame(frame, bg=colores['fondo_principal'])
    entrada_frame.pack()

    entries_A = []
    entries_B = []

    for i in range(3):
        fila = []
        for j in range(3):
            e = Entry(entrada_frame, width=5)
            e.grid(row=i, column=j, padx=5, pady=5)
            fila.append(e)
        entries_A.append(fila)

        e_b = Entry(entrada_frame, width=5)
        e_b.grid(row=i, column=4, padx=10)
        entries_B.append(e_b)

    # Selector de método
    metodo_var = StringVar()
    metodo_var.set("Cramer")
    opciones_metodos = ["Cramer", "Sarrus", "Cofactores"]
    menu = OptionMenu(frame, metodo_var, *opciones_metodos)
    menu.config(bg=colores['boton_normal'], fg=colores['texto_boton'], font=fuentes['botones'])
    menu.pack(pady=10)

    # Resultados
    resultado_frame = Frame(frame, bg=colores['fondo_principal'])
    resultado_frame.pack()

    def calcular():
        try:
            A = [[float(e.get()) for e in fila] for fila in entries_A]
            B = [float(e.get()) for e in entries_B]
        except ValueError:
            messagebox.showerror("Entrada inválida", "Todos los campos deben contener números.")
            return

        for widget in resultado_frame.winfo_children():
            widget.destroy()

        metodo = metodo_var.get()

        if metodo == "Cramer":
            resultado = resolver_cramer(A, B)
            if isinstance(resultado, str):
                Label(resultado_frame, text=resultado, fg="red", bg=colores['fondo_principal']).pack()
            else:
                Label(resultado_frame, text=f"Determinante de A: {resultado['det_A']}", bg=colores['fondo_principal']).pack()
                for i, x in enumerate(resultado['solucion'], 1):
                    Label(resultado_frame, text=f"x{i} = {x}", bg=colores['fondo_principal']).pack()

        elif metodo == "Sarrus":
            if len(A) == 3 and all(len(f) == 3 for f in A):
                det = determinante_sarrus(A)
                Label(resultado_frame, text=f"Determinante (Sarrus): {det}", bg=colores['fondo_principal']).pack()
            else:
                Label(resultado_frame, text="La matriz debe ser 3x3.", fg="red", bg=colores['fondo_principal']).pack()

        elif metodo == "Cofactores":
            if len(A) == 3 and all(len(f) == 3 for f in A):
                cofactores = matriz_de_cofactores(A)
                Label(resultado_frame, text="Matriz de Cofactores:", bg=colores['fondo_principal']).pack()
                for fila in cofactores:
                    Label(resultado_frame, text=str(fila), bg=colores['fondo_principal']).pack()
            else:
                Label(resultado_frame, text="La matriz debe ser 3x3.", fg="red", bg=colores['fondo_principal']).pack()

    Button(frame, text="Calcular", command=calcular,
           bg=colores['boton_normal'], fg=colores['texto_boton'],
           activebackground=colores['boton_hover'], relief="flat", font=fuentes['botones']
    ).pack(pady=15)

    return frame

# === Prueba local ===
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x720")
    root.title("Sistema de Ecuaciones - Multimétodo")
    colores = {
        'fondo_principal': "#f8f9fa",
        'boton_normal': "#495057",
        'boton_hover': "#343a40",
        'texto_boton': "#f8f9fa",
        'titulo': "#d62828"
    }
    fuentes = {
        'titulo': ("Segoe UI", 16, "bold"),
        'subtitulo': ("Segoe UI", 12),
        'botones': ("Segoe UI", 11)
    }
    interfaz_sistemas(root, colores, fuentes)
    root.mainloop()
