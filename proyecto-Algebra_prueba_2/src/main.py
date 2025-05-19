# src/main.py
from tkinter import Label, Button, Frame, Tk, font # tkinter.font no se usa directamente, pero es bueno tenerlo si se usa.

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Importar la interfaz específica de manera estándar
try:
    from frontend.interfaz_operaciones_combinadas import InterfazOperacionesCombinadas
except ImportError as e:
    print(f"ERROR EN MAIN.PY AL IMPORTAR: {e}") # Mensaje de depuración
    print("CAUSA POSIBLE: Verifique el terminal para errores DENTRO de 'interfaz_operaciones_combinadas.py' o sus propias importaciones (ej. del backend).")
    print("Asegúrese de que 'interfaz_operaciones_combinadas.py' esté en 'src/frontend/'.")
    print("Asegúrese de que existan archivos __init__.py vacíos en 'src/', 'src/frontend/' y 'src/backend/'.")
    print("Ejecute desde 'proyecto-Algebra/' con: python src/main.py")
    InterfazOperacionesCombinadas = None 


class CalculadoraAlgebra(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configurar_ventana()
        self.crear_interfaz()
        
    def configurar_ventana(self):
        self.master.title("Calculadora de Álgebra Lineal")
        self.master.geometry("1000x700")
        self.master.minsize(800, 600)
        self.master.resizable(True, True)
        self.master.configure(bg='white')

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid(sticky="nsew")

    def crear_interfaz(self):
        self.colores = {
            'fondo_lateral': "#2b2d42",
            'fondo_principal': "#f8f9fa",
            'boton_normal': "#495057",
            'boton_hover': "#343a40",
            'texto_boton': "#f8f9fa",
            'titulo': "#d62828" 
        }
        self.fuentes = {
            'titulo_menu': ("Segoe UI", 16, "bold"), 
            'botones': ("Segoe UI", 11),
            'subtitulo_bienvenida': ("Segoe UI", 12), 
            'titulo_area_principal': ("Segoe UI", 18, "bold") 
        }
        self.crear_panel_lateral()
        self.crear_area_principal()
        self.mostrar_bienvenida()

    def crear_panel_lateral(self):
        self.panel_lateral = Frame(self, width=220, bg=self.colores['fondo_lateral'])
        self.panel_lateral.grid(row=0, column=0, sticky="ns")
        self.panel_lateral.grid_propagate(False)
        self.panel_lateral.grid_rowconfigure(0, weight=0) 
        self.panel_lateral.grid_rowconfigure(1, weight=1) 

        contenedor_botones_outer = Frame(self.panel_lateral, bg=self.colores['fondo_lateral'])
        contenedor_botones_outer.grid(row=1, column=0, sticky="nsew") 
        contenedor_botones_outer.grid_rowconfigure(0, weight=1)
        contenedor_botones_outer.grid_rowconfigure(2, weight=1)
        contenedor_botones_outer.grid_columnconfigure(0, weight=1)
        contenedor_botones_outer.grid_columnconfigure(2, weight=1)
        contenedor_botones_inner = Frame(contenedor_botones_outer, bg=self.colores['fondo_lateral'])
        contenedor_botones_inner.grid(row=1, column=1, sticky="n")

        lbl_titulo_menu = Label(self.panel_lateral, 
                           text="🧭 MENÚ",
                           bg=self.colores['fondo_lateral'],
                           fg="white",
                           font=self.fuentes['titulo_menu'])
        lbl_titulo_menu.grid(row=0, column=0, pady=(30,15), padx=10, sticky="ew") 

        botones = [
            ("Sumar Matrices", self.mostrar_suma),
            ("Restar Matrices", self.mostrar_placeholder), 
            ("Multiplicar Matrices", self.mostrar_placeholder), 
            ("Inversa de Matriz", self.mostrar_placeholder), 
            ("Operaciones Combinadas", self.mostrar_operaciones_combinadas), 
            ("Vectores", self.mostrar_placeholder) 
        ]
        for i, (texto, comando) in enumerate(botones):
            btn = Button(contenedor_botones_inner, 
                         text=texto,
                         command=comando,
                         bg=self.colores['boton_normal'],
                         fg=self.colores['texto_boton'],
                         font=self.fuentes['botones'],
                         relief="flat",
                         padx=10,
                         pady=10,
                         width=20, 
                         cursor="hand2")
            btn.pack(pady=6, padx=10, fill='x') 
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.colores['boton_hover']))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.colores['boton_normal']))

    def crear_area_principal(self):
        self.area_principal = Frame(self, bg=self.colores['fondo_principal'])
        self.area_principal.grid(row=0, column=1, sticky="nsew")
        self.grid_columnconfigure(1, weight=1) 
        self.grid_rowconfigure(0, weight=1)    

    def limpiar_area_principal(self):
        for widget in self.area_principal.winfo_children():
            widget.destroy()

    def mostrar_bienvenida(self):
        self.limpiar_area_principal()
        contenedor = Frame(self.area_principal, bg=self.colores['fondo_principal'])
        contenedor.place(relx=0.5, rely=0.4, anchor="center")
        Label(contenedor, text="Calculadora de Álgebra Lineal", bg=self.colores['fondo_principal'], fg=self.colores['titulo'], font=("Segoe UI", 24, "bold") ).grid(row=0, column=0, pady=10)
        Label(contenedor, text="Selecciona una opción del menú lateral para comenzar", bg=self.colores['fondo_principal'], fg="#495057", font=self.fuentes['subtitulo_bienvenida']).grid(row=1, column=0, pady=5)

    def mostrar_suma(self):
        self.limpiar_area_principal()
        marco = Frame(self.area_principal, bg=self.colores['fondo_principal'])
        marco.pack(pady=30, padx=20, fill="both", expand=True)
        Label(marco, text="Suma de Matrices", bg=self.colores['fondo_principal'], fg=self.colores['titulo'], font=self.fuentes['titulo_area_principal']).pack(pady=10)

    def mostrar_operaciones_combinadas(self):
        self.limpiar_area_principal()
        if InterfazOperacionesCombinadas:
            # Instanciar la interfaz, pasándole el frame del área principal como master.
            # La propia clase InterfazOperacionesCombinadas (si hereda de Frame/ttk.Frame)
            # se encargará de dibujarse usando .pack() o .grid() en su __init__.
            app_combinada = InterfazOperacionesCombinadas(self.area_principal)
        else:
            Label(self.area_principal,
                  text="Error: Interfaz de Operaciones Combinadas no pudo ser cargada.\nRevise la consola para más detalles.",
                  bg=self.colores['fondo_principal'], fg="red", font=self.fuentes['subtitulo_bienvenida'],
                  justify="left"
                  ).pack(pady=20, padx=20)

    def mostrar_placeholder(self): 
        self.limpiar_area_principal()
        marco = Frame(self.area_principal, bg=self.colores['fondo_principal'])
        marco.place(relx=0.5, rely=0.5, anchor="center")
        Label(marco, text="🚧 Función en desarrollo", bg=self.colores['fondo_principal'], fg="#6c757d", font=self.fuentes['titulo_area_principal']).pack(pady=10)
        Label(marco, text="Próximamente disponible", bg=self.colores['fondo_principal'], fg="#adb5bd", font=self.fuentes['subtitulo_bienvenida']).pack(pady=5)

if __name__ == "__main__":
    root = Tk()
    app = CalculadoraAlgebra(root)
    root.mainloop()
