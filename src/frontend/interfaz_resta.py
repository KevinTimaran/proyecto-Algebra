import tkinter as tk
from tkinter import Frame, Label, messagebox
from restarMatrices import restarMatrices  


def interfaz_resta(parent, colores, fuentes):
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=False, padx=20, pady=10)

    Label(
        frame,
        text="Resta de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 10))

    return frame


class AppRestaMatrices:
    def __init__(self, root, colores, fuentes):
        self.root = root
        self.root.title("Calculadora de Resta de Matrices")
        self.colores = colores
        self.fuentes = fuentes

        self.crear_interfaz_inicial()

    def crear_interfaz_inicial(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        interfaz_resta(self.root, self.colores, self.fuentes)

        self.label_filas = tk.Label(self.root, text="Número de filas:")
        self.label_filas.pack()
        self.entry_filas = tk.Entry(self.root)
        self.entry_filas.pack()

        self.label_columnas = tk.Label(self.root, text="Número de columnas:")
        self.label_columnas.pack()
        self.entry_columnas = tk.Entry(self.root)
        self.entry_columnas.pack()

        self.boton_siguiente = tk.Button(self.root, text="Siguiente", command=self.crear_entradas_matrices)
        self.boton_siguiente.pack(pady=10)

    def crear_entradas_matrices(self):
        try:
            self.filas = int(self.entry_filas.get())
            self.columnas = int(self.entry_columnas.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        interfaz_resta(self.root, self.colores, self.fuentes)

        # Título matriz 1
        tk.Label(self.root, text="Matriz 1").pack()

        self.matriz1_entries = []
        for i in range(self.filas):
            fila_frame = tk.Frame(self.root)
            fila_frame.pack()
            fila = []
            for j in range(self.columnas):
                e = tk.Entry(fila_frame, width=5)
                e.pack(side="left", padx=2)
                fila.append(e)
            self.matriz1_entries.append(fila)

        # Título matriz 2
        tk.Label(self.root, text="Matriz 2").pack(pady=(10, 0))

        self.matriz2_entries = []
        for i in range(self.filas):
            fila_frame = tk.Frame(self.root)
            fila_frame.pack()
            fila = []
            for j in range(self.columnas):
                e = tk.Entry(fila_frame, width=5)
                e.pack(side="left", padx=2)
                fila.append(e)
            self.matriz2_entries.append(fila)

        self.boton_restar = tk.Button(self.root, text="Restar", command=self.restar_matrices_gui)
        self.boton_restar.pack(pady=10)

    def restar_matrices_gui(self):
        try:
            matriz1 = [[int(self.matriz1_entries[i][j].get()) for j in range(self.columnas)] for i in range(self.filas)]
            matriz2 = [[int(self.matriz2_entries[i][j].get()) for j in range(self.columnas)] for i in range(self.filas)]
        except ValueError:
            messagebox.showerror("Error", "Todos los campos deben tener números enteros.")
            return

        resultado = restarMatrices(matriz1, matriz2)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        ventana_resultado = tk.Toplevel(self.root)
        ventana_resultado.title("Resultado de la resta")

        tk.Label(ventana_resultado, text="Resultado:").pack(pady=10)
        for fila in resultado:
            fila_texto = "   ".join(str(num) for num in fila)
            tk.Label(ventana_resultado, text=fila_texto).pack()


# --- Ejecutar la aplicación ---
if __name__ == "__main__":
    colores = {
        'fondo_principal': '#f0f0f0',
        'titulo': '#333366'
    }

    fuentes = {
        'titulo': ('Helvetica', 16, 'bold')
    }

    ventana = tk.Tk()
    app = AppRestaMatrices(ventana, colores, fuentes)
    ventana.mainloop()
