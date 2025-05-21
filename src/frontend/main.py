from tkinter import Label, Button, Frame, Tk, font
from interfaz_operaciones_combinadas import interfazOperacionesCombinadas
from interfaz_resta import interfaz_resta
from interfaz_inversa import interfaz_inversa
from interfaz_sumas import interfaz_suma
from interfaz_vectores import interfaz_vectores
from interfaz_multiplicacion import interfaz_multiplicacion

class CalculadoraAlgebra(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configurar_ventana()
        self.crear_interfaz()
        
    def configurar_ventana(self):
        self.master.title("Calculadora de Álgebra Lineal")
        self.master.geometry("1500x800")
        self.master.minsize(800, 600)
        self.master.resizable(False, False)
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
            'titulo': ("Segoe UI", 16, "bold"),
            'botones': ("Segoe UI", 11),
            'subtitulo': ("Segoe UI", 12)
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

        # Contenedor centrado para los botones
        contenedor_botones = Frame(self.panel_lateral, bg=self.colores['fondo_lateral'])
        contenedor_botones.grid(row=1, column=0, sticky="n")

        lbl_titulo = Label(self.panel_lateral, 
                           text="🧭 MENÚ",
                           bg=self.colores['fondo_lateral'],
                           fg="white",
                           font=self.fuentes['titulo'])
        lbl_titulo.grid(row=0, column=0, pady=30, padx=10)

        botones = [
            ("Sumar Matrices", self.mostrar_operaciones_suma),
            ("Restar Matrices", self.mostrar_operaciones_resta),
            ("Multiplicar Matrices", self.mostrar_multiplicacion),
            ("Inversa de Matriz", self.mostrar_operaciones_inversa),
            ("Operaciones Combinadas", self.mostrar_operaciones_combinadas),
            ("Vectores", self.mostrar_vectores)
        ]

        for i, (texto, comando) in enumerate(botones):
            btn = Button(contenedor_botones,
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
            btn.pack(pady=6, padx=10)

            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.colores['boton_hover']))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.colores['boton_normal']))

    def crear_area_principal(self):
        self.area_principal = Frame(self, bg=self.colores['fondo_principal'])
        self.area_principal.grid(row=0, column=1, sticky="nsew")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def mostrar_bienvenida(self):
        self.limpiar_area_principal()
        contenedor = Frame(self.area_principal, bg=self.colores['fondo_principal'])
        contenedor.place(relx=0.5, rely=0.4, anchor="center")

        Label(contenedor,
              text="Calculadora de Álgebra Lineal",
              bg=self.colores['fondo_principal'],
              fg=self.colores['titulo'],
              font=("Segoe UI", 20, "bold")
        ).grid(row=0, column=0, pady=10)

        Label(contenedor,
              text="Selecciona una opción del menú lateral para comenzar",
              bg=self.colores['fondo_principal'],
              fg="#495057",
              font=self.fuentes['subtitulo']
        ).grid(row=1, column=0, pady=5)

    def mostrar_suma(self):
        self.limpiar_area_principal()
        marco = Frame(self.area_principal, bg=self.colores['fondo_principal'])
        marco.pack(pady=30, padx=20, fill="both", expand=True)

        Label(marco,
              text="Suma de Matrices",
              bg=self.colores['fondo_principal'],
              fg=self.colores['titulo'],
              font=self.fuentes['titulo']
        ).pack(pady=10)

    def mostrar_placeholder(self):
        self.limpiar_area_principal()
        marco = Frame(self.area_principal, bg=self.colores['fondo_principal'])
        marco.place(relx=0.5, rely=0.5, anchor="center")

        Label(marco,
              text="🚧 Función en desarrollo",
              bg=self.colores['fondo_principal'],
              fg="#6c757d",
              font=self.fuentes['titulo']
        ).pack(pady=10)

        Label(marco,
              text="Próximamente disponible",
              bg=self.colores['fondo_principal'],
              fg="#adb5bd",
              font=self.fuentes['subtitulo']
        ).pack(pady=5)

    def limpiar_area_principal(self):
        for widget in self.area_principal.winfo_children():
            widget.destroy()

    #----------------------------------------------
    # Métodos para mostrar otras operaciones
    #----------------------------------------------
    def mostrar_operaciones_combinadas(self):
        self.limpiar_area_principal()
        interfazOperacionesCombinadas(self.area_principal, self.colores, self.fuentes)
 
    def mostrar_operaciones_resta(self):
        self.limpiar_area_principal()
        interfaz_resta(self.area_principal, self.colores, self.fuentes)

    def mostrar_operaciones_inversa(self):
        self.limpiar_area_principal()
        interfaz_inversa(self.area_principal, self.colores, self.fuentes)

    def mostrar_operaciones_suma(self):
        self.limpiar_area_principal()
        interfaz_suma(self.area_principal, self.colores, self.fuentes)

    def mostrar_vectores(self):
        self.limpiar_area_principal()
        interfaz_vectores(self.area_principal, self.colores, self.fuentes)

    def mostrar_multiplicacion(self):
        self.limpiar_area_principal()
        interfaz_multiplicacion(self.area_principal, self.colores, self.fuentes)


if __name__ == "__main__":
    root = Tk()
    app = CalculadoraAlgebra(root)
    app.mainloop()