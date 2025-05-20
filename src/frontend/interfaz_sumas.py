# src/frontend/interfaz_suma.py

from tkinter import Frame, Label

def interfaz_suma(parent, colores, fuentes):
    """
    Construye la interfaz gráfica para la operación de Suma de Matrices.

    Parámetros:
    - parent: Frame contenedor donde se colocará esta interfaz (usualmente self.area_principal).
    - colores: Diccionario de colores globales definidos en la interfaz principal.
    - fuentes: Diccionario de fuentes globales definidos en la interfaz principal.
    """

    # ✅ Este frame debe mantenerse (no modificar)
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # ✅ Este título principal debe mantenerse
    Label(
        frame,
        text="Suma de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    return frame  # Opcional: devolver el frame si se necesita manipular más tarde

class AppSumaMatrices:
    def __init__(self, root, colores, fuentes):
        self.root = root
        self.root.title("Calculadora de Suma de Matrices")
        self.colores = colores
        self.fuentes = fuentes

        self.crear_interfaz_inicial()

    def crear_interfaz_inicial(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        interfaz_suma(self.root, self.colores, self.fuentes)

        Label(self.root, text="Número de filas:").pack()
        self.entry_filas = Entry(self.root)
        self.entry_filas.pack()

        Label(self.root, text="Número de columnas:").pack()
        self.entry_columnas = Entry(self.root)
        self.entry_columnas.pack()

        Button(self.root, text="Siguiente", command=self.crear_entradas_matrices).pack(pady=10)

    def crear_entradas_matrices(self):
        try:
            self.filas = int(self.entry_filas.get())
            self.columnas = int(self.entry_columnas.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        interfaz_suma(self.root, self.colores, self.fuentes)

        Label(self.root, text="Matriz A").pack()
        self.matrizA_entries = self.crear_entradas(self.filas, self.columnas)

        Label(self.root, text="Matriz B").pack(pady=(10, 0))
        self.matrizB_entries = self.crear_entradas(self.filas, self.columnas)

        Button(self.root, text="Sumar", command=self.sumar_matrices_gui).pack(pady=10)

    def crear_entradas(self, filas, columnas):
        entradas = []
        for i in range(filas):
            fila = []
            fila_frame = Frame(self.root)
            fila_frame.pack()
            for j in range(columnas):
                e = Entry(fila_frame, width=5)
                e.pack(side="left", padx=2, pady=2)
                fila.append(e)
            entradas.append(fila)
        return entradas

    def sumar_matrices_gui(self):
        datosA = [[entry.get() for entry in fila] for fila in self.matrizA_entries]
        datosB = [[entry.get() for entry in fila] for fila in self.matrizB_entries]

        matrizA = crear_matriz(self.filas, self.columnas, datosA)
        if isinstance(matrizA, str):
            messagebox.showerror("Error", matrizA)
            return

        matrizB = crear_matriz(self.filas, self.columnas, datosB)
        if isinstance(matrizB, str):
            messagebox.showerror("Error", matrizB)
            return

        resultado = sumar_matrices(matrizA, matrizB)
        if isinstance(resultado, str):
            messagebox.showerror("Error", resultado)
            return

        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        ventana_resultado = tk.Toplevel(self.root)
        ventana_resultado.title("Resultado de la suma")

        Label(ventana_resultado, text="Resultado:").pack(pady=10)
        for fila in resultado:
            fila_texto = "   ".join(str(num) for num in fila)
            Label(ventana_resultado, text=fila_texto).pack()

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
    app = AppSumaMatrices(ventana, colores, fuentes)
    ventana.mainloop()
