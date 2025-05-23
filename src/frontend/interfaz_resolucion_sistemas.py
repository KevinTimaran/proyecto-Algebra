import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
import os, sys

# === Asegurar ruta al backend ===
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)
if root_src_dir not in sys.path:
    sys.path.append(root_src_dir)

# === Intentar importar lógica de Cramer ===
try:
    from backend.resolucionSistemas import resolver_cramer
except ImportError:
    def resolver_cramer(A, B):
        messagebox.showerror("Error", "No se pudo importar la función 'resolver_cramer'.")
        return None

def interfaz_sistemas(parent, colores, fuentes):
    frame = Frame(parent, bg=colores['fondo_principal'], width=760, height=660)
    frame.pack(padx=30, pady=30)
    frame.pack_propagate(False)

    Label(frame, text="Resolución de Sistemas (Método de Cramer)",
          bg=colores['fondo_principal'], fg=colores['titulo'], font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # 🧮 Entrada de matrices
    entrada_frame = Frame(frame, bg=colores['fondo_principal'])
    entrada_frame.pack(pady=10)

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

    # Resultado
    resultado_frame = Frame(frame, bg=colores['fondo_principal'])
    resultado_frame.pack(pady=10)

    def calcular():
        try:
            A = [[float(e.get()) for e in fila] for fila in entries_A]
            B = [float(e.get()) for e in entries_B]
        except ValueError:
            messagebox.showerror("Entrada inválida", "Todos los campos deben contener números.")
            return

        resultado = resolver_cramer(A, B)

        for widget in resultado_frame.winfo_children():
            widget.destroy()

        if isinstance(resultado, str):
            Label(resultado_frame, text=resultado, fg="red",
                  bg=colores['fondo_principal'], font=fuentes['subtitulo']).pack()
        else:
            Label(resultado_frame, text=f"Determinante de A: {resultado['det_A']}",
                  bg=colores['fondo_principal'], font=fuentes['subtitulo']).pack(pady=5)

            for i, x in enumerate(resultado['solucion'], 1):
                Label(resultado_frame, text=f"x{i} = {x}",
                      bg=colores['fondo_principal'], font=fuentes['botones']).pack()

    Button(frame, text="Resolver con Cramer", command=calcular,
           bg=colores['boton_normal'], fg=colores['texto_boton'],
           activebackground=colores['boton_hover'], relief="flat", font=fuentes['botones']
    ).pack(pady=15)

    return frame

# === Prueba local ===
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x650")
    root.title("Sistema de Ecuaciones - Método de Cramer")
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
