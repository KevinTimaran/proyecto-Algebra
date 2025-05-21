import tkinter as tk
from tkinter import Frame, Label, Entry, Button, messagebox
import os, sys

# Configuración de rutas para importar el backend
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)
if root_src_dir not in sys.path:
    sys.path.append(root_src_dir)

# Importar backend (con manejo de errores)
try:
    from backend.multiplicacionMatrices import multiplicar_matrices
    from backend.sumaMatrices import crear_matriz
    backend_ok = True
except ImportError as e:
    print(f"⚠️ Error al importar backend: {e}")
    backend_ok = False
    def multiplicar_matrices(A, B):
        messagebox.showerror("Error", "Backend no disponible. Verifica los imports.")
        return None

def crear_matriz(filas, columnas, datos):
    """Valida y construye una matriz a partir de strings."""
    try:
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = datos[i][j].strip()
                if not valor:
                    return f"Error: Celda vacía en ({i+1},{j+1})"
                fila.append(float(valor))
            matriz.append(fila)
        return matriz
    except ValueError:
        return "Error: Ingresa solo números válidos."
    except IndexError:
        return "Error: Dimensiones incorrectas."

def interfaz_multiplicacion(parent, colores, fuentes):
    # Frame principal
    frame = Frame(parent, bg=colores['fondo_principal'], width=760, height=660)
    frame.pack(padx=30, pady=30)
    frame.pack_propagate(False)

    Label(frame, text="Multiplicación de Matrices (A × B)", 
          bg=colores['fondo_principal'], fg=colores['titulo'],
          font=fuentes['titulo']).pack(pady=(0, 20))

    # Frame para dimensiones
    frame_dim = Frame(frame, bg=colores['fondo_principal'])
    frame_dim.pack()

    def crear_input(label_text, row, col):
        Label(frame_dim, text=label_text, bg=colores['fondo_principal'], 
              font=fuentes['botones']).grid(row=row, column=col, padx=5, pady=2, sticky="e")
        e = Entry(frame_dim, width=5)
        e.grid(row=row, column=col+1, padx=5, pady=2)
        return e

    Label(frame_dim, text="Dimensiones:", bg=colores['fondo_principal'], 
          font=fuentes['subtitulo']).grid(row=0, column=0, columnspan=4, pady=5)
    entry_filas_A = crear_input("Filas A:", 1, 0)
    entry_cols_A  = crear_input("Columnas A:", 2, 0)
    entry_filas_B = crear_input("Filas B:", 1, 2)
    entry_cols_B  = crear_input("Columnas B:", 2, 2)

    # Frames para matrices y resultado
    frame_entradas = Frame(frame, bg=colores['fondo_principal'])
    frame_entradas.pack(pady=10)
    frame_resultado = Frame(frame, bg=colores['fondo_principal'])
    frame_resultado.pack(pady=10)

    def generar_campos():
        try:
            fa, ca = int(entry_filas_A.get()), int(entry_cols_A.get())
            fb, cb = int(entry_filas_B.get()), int(entry_cols_B.get())

            if ca != fb:
                messagebox.showerror("Error", "Columnas A debe ser igual a Filas B")
                return
            if not all(1 <= x <= 7 for x in [fa, ca, fb, cb]):
                messagebox.showwarning("Límite", "Máximo permitido: 7x7")
                return

        except ValueError:
            messagebox.showerror("Error", "Ingresa números enteros válidos")
            return

        # Limpiar frames anteriores
        for widget in frame_entradas.winfo_children(): widget.destroy()
        for widget in frame_resultado.winfo_children(): widget.destroy()

        # Crear etiquetas de matrices
        Label(frame_entradas, text="Matriz A", bg=colores['fondo_principal'], 
              font=fuentes['subtitulo']).grid(row=0, column=0, columnspan=ca, padx=10)
        Label(frame_entradas, text="Matriz B", bg=colores['fondo_principal'], 
              font=fuentes['subtitulo']).grid(row=0, column=ca+1, columnspan=cb, padx=10)

        entries_A = []
        for i in range(fa):
            fila_A = []
            for j in range(ca):
                e = Entry(frame_entradas, width=5)
                e.grid(row=i+1, column=j, padx=2, pady=2)
                fila_A.append(e)
            entries_A.append(fila_A)

        # Frame interno para Matriz B
        frame_B = Frame(frame_entradas, bg=colores['fondo_principal'])
        frame_B.grid(row=1, column=ca+1, rowspan=fa, padx=10)
        entries_B = []
        for i in range(fb):
            fila_B = []
            for j in range(cb):
                e = Entry(frame_B, width=5)
                e.grid(row=i, column=j, padx=2, pady=2)
                fila_B.append(e)
            entries_B.append(fila_B)

        def calcular():
            # Obtener datos y validar
            datos_A = [[e.get() for e in fila] for fila in entries_A]
            datos_B = [[e.get() for e in fila] for fila in entries_B]

            A = crear_matriz(fa, ca, datos_A)
            if isinstance(A, str):
                messagebox.showerror("Error en A", A)
                return

            B = crear_matriz(fb, cb, datos_B)
            if isinstance(B, str):
                messagebox.showerror("Error en B", B)
                return

            # Multiplicar y mostrar resultado
            resultado = multiplicar_matrices(A, B)
            if resultado is None: return

            for widget in frame_resultado.winfo_children(): widget.destroy()
            Label(frame_resultado, text="Resultado A × B:", 
                  bg=colores['fondo_principal'], font=fuentes['subtitulo']).pack(pady=5)
            
            for fila in resultado:
                texto = "  ".join(f"{x:.2f}" for x in fila)
                Label(frame_resultado, text=texto, font=("Courier", 11), 
                      bg=colores['fondo_principal']).pack()

        Button(frame_entradas, text="Calcular", command=calcular,
               bg=colores['boton_normal'], fg=colores['texto_boton'],
               font=fuentes['botones']).grid(row=fa+2, column=0, columnspan=ca+cb+1, pady=10)

    Button(frame, text="Generar Matrices", command=generar_campos,
           bg=colores['boton_normal'], fg=colores['texto_boton'],
           font=fuentes['botones']).pack(pady=10)

    return frame

# Ejemplo de uso
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Multiplicador de Matrices")
    root.geometry("900x700")
    
    colores = {
        'fondo_principal': "#f0f8ff",
        'titulo': "#2e86c1",
        'boton_normal': "#3498db",
        'texto_boton': "white"
    }
    
    fuentes = {
        'titulo': ("Arial", 16, "bold"),
        'subtitulo': ("Arial", 12),
        'botones': ("Arial", 10)
    }
    
    interfaz_multiplicacion(root, colores, fuentes)
    root.mainloop()