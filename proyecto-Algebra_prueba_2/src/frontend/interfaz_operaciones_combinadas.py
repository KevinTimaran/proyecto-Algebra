# src/frontend/interfaz_operaciones_combinadas.py
import tkinter as tk
from tkinter import ttk, messagebox

# Intenta importar las funciones necesarias del backend.
try:
    from backend.matricesOperacionesCombinadas import operacion_combinada, es_matriz_valida
except ImportError as e_interno:
    print(f"DEBUG: Error AL IMPORTAR DENTRO DE interfaz_operaciones_combinadas.py: {e_interno}")
    print("DEBUG: Asegúrate que 'src/backend/matricesOperacionesCombinadas.py' existe y no tiene errores.")
    print("DEBUG: Y que 'src/backend/__init__.py' existe.")
    def operacion_combinada(alpha, A, beta, B):
        messagebox.showerror("Error Crítico de Importación", "No se pudo cargar la lógica del backend (operacion_combinada).")
        return None
    def es_matriz_valida(matriz):
        return False, "Error crítico: no se pudo cargar la lógica del backend (es_matriz_valida)."

class InterfazOperacionesCombinadas(ttk.Frame): 
    def __init__(self, master): 
        super().__init__(master, padding="10 10 10 10")
        self.master = master 
        self.pack(fill=tk.BOTH, expand=True) 

        style = ttk.Style(self) 
        style.configure("TLabel", padding=5, font=('Arial', 10))
        style.configure("TEntry", padding=5, font=('Arial', 10))
        style.configure("TButton", padding=5, font=('Arial', 10))
        style.configure("Resultado.TLabel", font=('Arial', 10, 'bold'))
        
        ttk.Label(self, text="Operación Combinada αA + βB", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0,10))

        # --- Etiqueta Modificada ---
        ttk.Label(self, text="Matriz A (filas con ; elementos con , o espacio):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_A_str = ttk.Entry(self, width=40)
        self.entry_A_str.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        self.entry_A_str.insert(0, "1,2;3,4") 

        ttk.Label(self, text="Escalar α:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_alpha_str = ttk.Entry(self, width=10)
        self.entry_alpha_str.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        self.entry_alpha_str.insert(0, "1") 

        # --- Etiqueta Modificada para Matriz B también (para consistencia) ---
        ttk.Label(self, text="Matriz B (filas con ; elementos con , o espacio):").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_B_str = ttk.Entry(self, width=40)
        self.entry_B_str.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)
        self.entry_B_str.insert(0, "5,6;7,8") 

        ttk.Label(self, text="Escalar β:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_beta_str = ttk.Entry(self, width=10)
        self.entry_beta_str.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        self.entry_beta_str.insert(0, "1") 

        self.calculate_button = ttk.Button(self, text="Calcular αA + βB", command=self.calcular)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="Resultado:").grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
        self.result_text = tk.StringVar()
        self.result_label = ttk.Label(self, textvariable=self.result_text, style="Resultado.TLabel", wraplength=550)
        self.result_label.grid(row=7, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)
        
        self.columnconfigure(1, weight=1)

    def parse_matrix_string(self, matrix_str):
        matriz = []
        if not matrix_str.strip():
            return [], "La cadena de la matriz está vacía."
        
        filas_str = matrix_str.split(';')
        num_cols = -1

        for i, fila_str_raw in enumerate(filas_str):
            fila_str = fila_str_raw.strip()
            elementos_str = fila_str.replace(',', ' ').split()
            
            if not elementos_str and not fila_str: 
                if len(filas_str) == 1: 
                     return None, "La cadena de la matriz está vacía o es inválida."
                matriz.append([]) 
                if i == 0: num_cols = 0
                elif num_cols != 0 : 
                    return None, f"Error: Fila {i+1} está vacía pero filas anteriores no lo estaban."
                continue
            elif not elementos_str and fila_str: 
                return None, f"Error: Fila {i+1} contiene solo espacios o caracteres no numéricos."

            fila_actual = []
            try:
                for elem_str in elementos_str:
                    fila_actual.append(float(elem_str)) 
            except ValueError:
                return None, f"Error: Elemento no numérico '{elem_str}' en la fila {i+1}."
            
            if i == 0:
                num_cols = len(fila_actual)
            elif len(fila_actual) != num_cols :
                 return None, f"Error: Fila {i+1} tiene {len(fila_actual)} columnas, se esperaban {num_cols}."
            
            matriz.append(fila_actual)
        
        es_valida, mensaje_val = es_matriz_valida(matriz) 
        if not es_valida:
            return None, f"Error de validación interna: {mensaje_val}"
            
        return matriz, None

    def parse_scalar_string(self, scalar_str):
        try:
            return float(scalar_str)
        except ValueError:
            return None

    def calcular(self):
        A_str = self.entry_A_str.get()
        B_str = self.entry_B_str.get()
        alpha_str = self.entry_alpha_str.get()
        beta_str = self.entry_beta_str.get()

        A, error_A = self.parse_matrix_string(A_str)
        if error_A:
            messagebox.showerror("Error en Matriz A", error_A)
            self.result_text.set(f"Error en A: {error_A}")
            return

        B, error_B = self.parse_matrix_string(B_str)
        if error_B:
            messagebox.showerror("Error en Matriz B", error_B)
            self.result_text.set(f"Error en B: {error_B}")
            return

        alpha = self.parse_scalar_string(alpha_str)
        if alpha is None:
            messagebox.showerror("Error en Escalar α", "El escalar α debe ser un número.")
            self.result_text.set("Error: α debe ser numérico.")
            return

        beta = self.parse_scalar_string(beta_str)
        if beta is None:
            messagebox.showerror("Error en Escalar β", "El escalar β debe ser un número.")
            self.result_text.set("Error: β debe ser numérico.")
            return

        resultado_matriz = operacion_combinada(alpha, A, beta, B)

        if resultado_matriz is not None:
            if not resultado_matriz: 
                resultado_str = "Matriz vacía []"
            elif not resultado_matriz[0] and len(resultado_matriz) == 1: 
                resultado_str = "Matriz [[]]"
            else:
                resultado_str = "\n".join(["  ".join(map(str, fila)) for fila in resultado_matriz])
            self.result_text.set(resultado_str)
        else:
            self.result_text.set("Error durante el cálculo. Verifique la consola y los datos de entrada.")

if __name__ == '__main__':
    import sys
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__)) 
    project_root_src_dir = os.path.dirname(current_dir) 
    
    if project_root_src_dir not in sys.path:
       sys.path.insert(0, project_root_src_dir)
    
    root_test = tk.Tk()
    root_test.title("Test Interfaz Operaciones Combinadas")
    root_test.geometry("600x500")
    app_test = InterfazOperacionesCombinadas(root_test)
    root_test.mainloop()
