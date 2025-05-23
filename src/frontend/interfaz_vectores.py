from tkinter import Frame, Label, Entry, Button
from tkinter.ttk import Combobox, Style
import tkinter as tk
import tkinter.messagebox as messagebox
import os, sys

# Ajuste de rutas
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)

if root_src_dir not in sys.path:
    sys.path.insert(0, root_src_dir)

# Importación del backend
from backend.vectores import suma_vectores, resta_vectores, producto_punto, producto_cruz, angulo_entre_vectores, modulo_vector as magnitud_vector, multiplicar_por_escalar as multiplicacion_por_escalar



def interfaz_vectores(parent, colores, fuentes):
    """
    Carga la interfaz de operaciones con vectores en el área principal.

    Esta función será invocada desde la ventana principal al presionar el botón "Vectores".

    Parámetros:
    - parent: Frame contenedor (usualmente self.area_principal)
    - colores: Diccionario global de colores
    - fuentes: Diccionario global de fuentes
    """

    # Frame principal que ocupa toda el área de trabajo
    frame = Frame(parent, bg=colores['fondo_principal'], width=1200, height=750)
    frame.pack(padx=30, pady=30)
    frame.pack_propagate(False)  # Mantiene el tamaño definido, no se ajusta al contenido

    # Subdivisión: Área de control (superior)
    frame_top = Frame(frame, bg=colores['fondo_principal'], height=240)
    frame_top.pack(fill="x")
    frame_top.pack_propagate(False)

    #  Subdivisión: Área de operaciones y resultados (inferior)
    frame_operaciones = Frame(frame, bg="#f1f3f5", bd=2, relief="groove")
    frame_operaciones.pack(fill="both", expand=True, pady=(15, 0), padx=5)

    #  Título principal
    Label(
        frame_top,
        text="Operaciones con Vectores",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 10))

    #  Instrucción
    Label(
        frame_top,
        text="Selecciona una operación del menú desplegable para comenzar:",
        bg=colores['fondo_principal'],
        fg="#495057",
        font=fuentes['subtitulo']
    ).pack()

    #  Estilo visual para ComboBox
    style = Style()
    style.theme_use("clam")
    style.configure("TCombobox",
                    fieldbackground="white",
                    background="lightgray",
                    padding=5,
                    font=fuentes['botones'])

    #  Menú desplegable
    opciones = [
        "Suma", "Resta", "Multiplicación por escalar",
        "Producto punto", "Producto cruz", "Magnitud", "Ángulo entre vectores"
    ]
    cmb_opciones = Combobox(frame_top, values=opciones, state="readonly", style="TCombobox", width=30)
    cmb_opciones.pack(pady=10)
    cmb_opciones.current(0)

    #  Botón para procesar la operación
    Button(
        frame_top,
        text="Seleccionar operación",
        bg=colores['boton_normal'],
        fg=colores['texto_boton'],
        font=fuentes['botones'],
        activebackground=colores['boton_hover'],
        relief="flat",
        cursor="hand2",
        command=lambda: evaluar_opcion(cmb_opciones.get())
    ).pack(pady=5)

    #  Selector de operaciones
    def evaluar_opcion(seleccion):
        # Limpiar el área de operaciones antes de cargar algo nuevo
        for widget in frame_operaciones.winfo_children():
            widget.destroy()

        if seleccion == "Suma":
            frame_suma()
        elif seleccion == "Resta":
            frame_resta()
        elif seleccion == "Multiplicación por escalar":
            frame_multiplicacion()
        elif seleccion == "Producto punto":
            frame_producto()
        elif seleccion == "Producto cruz":
            frame_producto_cruz()
        elif seleccion == "Magnitud":
            frame_magnitud()
        elif seleccion == "Ángulo entre vectores":
            frame_angulo()

   
   
    def frame_suma():
        # Limpiar contenido anterior
        for widget in frame_operaciones.winfo_children():
            widget.destroy()

        # Dividir en dos columnas: izquierda (inputs) y derecha (gráfico)
        panel_izquierdo = Frame(frame_operaciones, bg="#f1f3f5", width=380)
        panel_derecho = Frame(frame_operaciones, bg="#f1f3f5", width=380)
        panel_izquierdo.pack(side="left", fill="both", expand=True, padx=10)
        panel_derecho.pack(side="right", fill="both", expand=True, padx=10)

        # 🎯 Entrada de vectores en panel izquierdo
        Label(panel_izquierdo, text="Suma de Vectores A + B",
            bg="#f1f3f5", fg="#212529", font=fuentes['subtitulo']).pack(pady=(5, 10))

        Label(panel_izquierdo, text="Vector A (ej: 3,4):", bg="#f1f3f5", font=fuentes['botones']).pack(anchor="w", padx=5)
        entry_A = Entry(panel_izquierdo, width=35)
        entry_A.insert(0, "3,4")
        entry_A.pack(pady=5)

        Label(panel_izquierdo, text="Vector B (ej: 1,2):", bg="#f1f3f5", font=fuentes['botones']).pack(anchor="w", padx=5)
        entry_B = Entry(panel_izquierdo, width=35)
        entry_B.insert(0, "1,2")
        entry_B.pack(pady=5)

        resultado_var = tk.StringVar()
        Label(panel_izquierdo, textvariable=resultado_var, bg="#f1f3f5", fg="black", font=fuentes['botones']).pack(pady=10)

        # 📦 Frame para la gráfica
        frame_grafica = Frame(panel_derecho, bg="#f1f3f5")
        frame_grafica.pack(fill="both", expand=True)

        def calcular_suma():
            for widget in frame_grafica.winfo_children():
                widget.destroy()

            texto_A = entry_A.get()
            texto_B = entry_B.get()

            try:
                A = [float(x.strip()) for x in texto_A.replace(',', ' ').split()]
                B = [float(x.strip()) for x in texto_B.replace(',', ' ').split()]
            except ValueError:
                resultado_var.set("Error: Los vectores deben contener solo números.")
                return

            if len(A) != len(B):
                resultado_var.set("Error: Los vectores deben tener la misma dimensión.")
                return

            from backend.vectores import suma_vectores
            from backend.graficas_vectores import graficar_vectores_en_2d

            resultado = suma_vectores(A, B)
            if isinstance(resultado, str):
                resultado_var.set(resultado)
            else:
                resultado_var.set(f"Resultado: {resultado}")
                graficar_vectores_en_2d(
                    canvas_parent=frame_grafica,
                    vectores=[A, B, resultado],
                    colores=["#007bff", "#28a745", "#dc3545"],
                    labels=["A", "B", "A + B"],
                    titulo="Suma de Vectores"
                )

        Button(panel_izquierdo, text="Calcular Suma",
            command=calcular_suma,
            bg=colores['boton_normal'],
            fg=colores['texto_boton'],
            activebackground=colores['boton_hover'],
            font=fuentes['botones'],
            relief="flat",
            cursor="hand2").pack(pady=5)






    def frame_resta():
         #  Limpiar contenido previo
        for widget in frame_operaciones.winfo_children():
            widget.destroy()

        #  Título
        Label(frame_operaciones, text="Suma de Vectores",
            bg="#f1f3f5", fg=colores['titulo'], font=fuentes['subtitulo']
        ).pack(pady=(10, 5))

        # Entrada: Vector A
        Label(frame_operaciones, text="Vector A (separa por comas):",
            bg="#f1f3f5", fg="#212529", font=fuentes['botones']
        ).pack(anchor="w", padx=10)
        entry_A = Entry(frame_operaciones, width=50)
        entry_A.pack(pady=5)

        # Entrada: Vector B
        Label(frame_operaciones, text="Vector B (separa por comas):",
            bg="#f1f3f5", fg="#212529", font=fuentes['botones']
        ).pack(anchor="w", padx=10)
        entry_B = Entry(frame_operaciones, width=50)
        entry_B.pack(pady=5)

        # Resultado
        resultado_var = tk.StringVar()
        Label(frame_operaciones, textvariable=resultado_var,
            bg="#f1f3f5", fg="#000", font=fuentes['botones']
        ).pack(pady=(10, 5))

        # Función para ejecutar la suma usando el backend
        def calcular():
            vector_a_str = entry_A.get()
            vector_b_str = entry_B.get()

            vector_a = vector_a_str.split(',')
            vector_b = vector_b_str.split(',')

            resultado = resta_vectores(vector_a, vector_b)

            if isinstance(resultado, str):  # Es un error del backend
                resultado_var.set(f"⚠️ {resultado}")
            else:
                resultado_var.set(f"Resultado: {resultado}")

        # Botón calcular
        Button(
            frame_operaciones,
            text="Calcular suma",
            bg=colores['boton_normal'],
            fg=colores['texto_boton'],
            font=fuentes['botones'],
            activebackground=colores['boton_hover'],
            relief="flat",
            cursor="hand2",
            command=calcular
        ).pack(pady=10)

    def frame_multiplicacion():
        # Limpiar contenido anterior del área de operaciones
        for widget in frame_operaciones.winfo_children():
            widget.destroy()

        # Título dentro del área de operaciones
        Label(frame_operaciones, text="Multiplicación por escalar",
            bg=frame_operaciones["bg"], fg="#343a40", font=fuentes['subtitulo']
        ).pack(pady=(10, 10))

        # Entrada para el vector
        Label(frame_operaciones, text="Vector (separado por comas):",
            bg=frame_operaciones["bg"], fg="#212529", font=fuentes['botones']
        ).pack(anchor="w", padx=10)
        entry_vector = Entry(frame_operaciones, width=40)
        entry_vector.pack(pady=(0, 10))

        # Entrada para el escalar
        Label(frame_operaciones, text="Escalar:",
            bg=frame_operaciones["bg"], fg="#212529", font=fuentes['botones']
        ).pack(anchor="w", padx=10)
        entry_escalar = Entry(frame_operaciones, width=10)
        entry_escalar.pack(pady=(0, 10))

        # Área de resultado
        resultado_var = tk.StringVar()
        Label(frame_operaciones, textvariable=resultado_var,
            bg=frame_operaciones["bg"], fg="#000", font=fuentes['botones'],
            justify="left", anchor="w", wraplength=700
        ).pack(pady=10, padx=10)

        # Botón de calcular
        def calcular():
            from backend.vectores import validar_vector, multiplicar_por_escalar

            vector_raw = entry_vector.get()
            escalar_raw = entry_escalar.get()

            vector = vector_raw.replace(" ", "").split(",")
            escalar = escalar_raw.strip()

            resultado = multiplicar_por_escalar(vector, escalar)

            if isinstance(resultado, str):
                messagebox.showerror("Error", resultado)
            else:
                resultado_var.set(f"Resultado:\n{resultado}")

        Button(frame_operaciones, text="Calcular",
            bg=colores['boton_normal'], fg=colores['texto_boton'],
            font=fuentes['botones'], activebackground=colores['boton_hover'],
            relief="flat", cursor="hand2", command=calcular
        ).pack(pady=10)


    def frame_producto():
        # Limpiar el área de operaciones antes de mostrar esta
        for widget in frame_operaciones.winfo_children():
            widget.destroy()

        # Título del submódulo
        tk.Label(
            frame_operaciones,
            text="Producto Punto entre dos vectores",
            bg=frame_operaciones['bg'],
            fg=colores['titulo'],
            font=fuentes['subtitulo']
        ).pack(pady=(0, 10))

        # Entradas de vectores
        frame_inputs = tk.Frame(frame_operaciones, bg=frame_operaciones['bg'])
        frame_inputs.pack(pady=10)

        tk.Label(frame_inputs, text="Vector A:", bg=frame_operaciones['bg'], font=fuentes['botones']).grid(row=0, column=0, sticky="e", padx=5)
        entry_a = tk.Entry(frame_inputs, width=40)
        entry_a.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_inputs, text="Vector B:", bg=frame_operaciones['bg'], font=fuentes['botones']).grid(row=1, column=0, sticky="e", padx=5)
        entry_b = tk.Entry(frame_inputs, width=40)
        entry_b.grid(row=1, column=1, padx=5, pady=5)

        # Resultado
        resultado_var = tk.StringVar()
        tk.Label(frame_operaciones, textvariable=resultado_var, bg=frame_operaciones['bg'], font=fuentes['botones'], fg="#333").pack(pady=10)

        # Botón de cálculo
        def calcular():
            from backend.vectores import producto_punto
            try:
                vec_a = entry_a.get().replace(" ", "").split(",")
                vec_b = entry_b.get().replace(" ", "").split(",")
                resultado = producto_punto(vec_a, vec_b)
                resultado_var.set(f"Resultado: {resultado}")
            except Exception as e:
                resultado_var.set(f"Error: {e}")

        tk.Button(
            frame_operaciones,
            text="Calcular Producto Punto",
            command=calcular,
            bg=colores['boton_normal'],
            fg=colores['texto_boton'],
            activebackground=colores['boton_hover'],
            relief="flat",
            font=fuentes['botones'],
            cursor="hand2"
        ).pack(pady=5)


    def frame_producto_cruz():
        # Limpiar área de operaciones
        for widget in frame_operaciones.winfo_children():
            widget.destroy()

        # Título
        tk.Label(
            frame_operaciones,
            text="Producto Cruz entre Vectores 3D",
            bg=frame_operaciones['bg'],
            fg=colores['titulo'],
            font=fuentes['subtitulo']
        ).pack(pady=(0, 10))

        # Entradas
        frame_inputs = tk.Frame(frame_operaciones, bg=frame_operaciones['bg'])
        frame_inputs.pack(pady=10)

        tk.Label(frame_inputs, text="Vector A (3 elementos):", bg=frame_operaciones['bg'], font=fuentes['botones']).grid(row=0, column=0, sticky="e", padx=5)
        entry_a = tk.Entry(frame_inputs, width=30)
        entry_a.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_inputs, text="Vector B (3 elementos):", bg=frame_operaciones['bg'], font=fuentes['botones']).grid(row=1, column=0, sticky="e", padx=5)
        entry_b = tk.Entry(frame_inputs, width=30)
        entry_b.grid(row=1, column=1, padx=5, pady=5)

        # Resultado
        resultado_var = tk.StringVar()
        tk.Label(frame_operaciones, textvariable=resultado_var, bg=frame_operaciones['bg'], font=fuentes['botones'], fg="#333").pack(pady=10)

        # Botón calcular
        def calcular():
            from backend.vectores import producto_cruz
            try:
                vec_a = entry_a.get().replace(" ", "").split(",")
                vec_b = entry_b.get().replace(" ", "").split(",")
                resultado = producto_cruz(vec_a, vec_b)
                if isinstance(resultado, str):
                    resultado_var.set(f"Error: {resultado}")
                else:
                    resultado_var.set(f"Resultado: [{', '.join(map(str, resultado))}]")
            except Exception as e:
                resultado_var.set(f"Error: {e}")

        tk.Button(
            frame_operaciones,
            text="Calcular Producto Cruz",
            command=calcular,
            bg=colores['boton_normal'],
            fg=colores['texto_boton'],
            activebackground=colores['boton_hover'],
            relief="flat",
            font=fuentes['botones'],
            cursor="hand2"
        ).pack(pady=5)


    def frame_magnitud():
        # Limpiar contenido anterior del frame de operaciones
        for widget in frame_operaciones.winfo_children():
            widget.destroy()

        # Título
        tk.Label(
            frame_operaciones,
            text="Magnitud de un Vector",
            bg=frame_operaciones['bg'],
            fg=colores['titulo'],
            font=fuentes['subtitulo']
        ).pack(pady=(0, 15))

        # Entrada
        input_frame = tk.Frame(frame_operaciones, bg=frame_operaciones['bg'])
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Vector:", bg=frame_operaciones['bg'], font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_vector = tk.Entry(input_frame, width=35)
        entry_vector.grid(row=0, column=1, padx=5)

        # Resultado
        resultado_var = tk.StringVar()
        tk.Label(frame_operaciones, textvariable=resultado_var, bg=frame_operaciones['bg'], font=fuentes['botones'], fg="#333").pack(pady=15)

        # Botón
        def calcular_magnitud():
            from backend.vectores import modulo_vector
            try:
                valores = entry_vector.get().replace(" ", "").split(",")
                resultado = modulo_vector(valores)
                if isinstance(resultado, str):
                    resultado_var.set(f"Error: {resultado}")
                else:
                    resultado_var.set(f"Magnitud: {resultado}")
            except Exception as e:
                resultado_var.set(f"Error inesperado: {e}")

        tk.Button(
            frame_operaciones,
            text="Calcular Magnitud",
            command=calcular_magnitud,
            bg=colores['boton_normal'],
            fg=colores['texto_boton'],
            activebackground=colores['boton_hover'],
            relief="flat",
            font=fuentes['botones'],
            cursor="hand2"
        ).pack()


    def frame_angulo():
        # Limpiar contenido previo
        for widget in frame_operaciones.winfo_children():
            widget.destroy()

        # Título
        tk.Label(
            frame_operaciones,
            text="Ángulo entre dos vectores",
            bg=frame_operaciones['bg'],
            fg=colores['titulo'],
            font=fuentes['subtitulo']
        ).pack(pady=(0, 15))

        # Entradas
        input_frame = tk.Frame(frame_operaciones, bg=frame_operaciones['bg'])
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Vector A:", bg=frame_operaciones['bg'], font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_a = tk.Entry(input_frame, width=35)
        entry_a.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Vector B:", bg=frame_operaciones['bg'], font=fuentes['botones']).grid(row=1, column=0, padx=5, sticky="e")
        entry_b = tk.Entry(input_frame, width=35)
        entry_b.grid(row=1, column=1, padx=5)

        # Resultado
        resultado_var = tk.StringVar()
        tk.Label(frame_operaciones, textvariable=resultado_var, bg=frame_operaciones['bg'], font=fuentes['botones'], fg="#333").pack(pady=15)

        # Botón de cálculo
        def calcular_angulo():
            from backend.vectores import angulo_entre_vectores
            try:
                vector_a = entry_a.get().replace(" ", "").split(",")
                vector_b = entry_b.get().replace(" ", "").split(",")

                resultado = angulo_entre_vectores(vector_a, vector_b)
                if isinstance(resultado, str):
                    resultado_var.set(f"Error: {resultado}")
                else:
                    resultado_var.set(f"Ángulo: {resultado}°")
            except Exception as e:
                resultado_var.set(f"Error inesperado: {e}")

        tk.Button(
            frame_operaciones,
            text="Calcular Ángulo",
            command=calcular_angulo,
            bg=colores['boton_normal'],
            fg=colores['texto_boton'],
            activebackground=colores['boton_hover'],
            relief="flat",
            font=fuentes['botones'],
            cursor="hand2"
        ).pack()


    # Devolver el frame si se requiere manipular desde afuera
    return frame


# === Bloque de prueba ===
if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    root.title("Prueba Interfaz Vectores")
    root.geometry("1280x700")
    colores = {
        'fondo_principal': "#edf2f4",
        'fondo_lateral': "#2b2d42",
        'titulo': "#ef233c",
        'boton_normal': "#8d99ae",
        'boton_hover': "#6c757d",
        'texto_boton': "white"
    }
    fuentes = {
        'titulo': ("Arial", 16, "bold"),
        'subtitulo': ("Arial", 12),
        'botones': ("Arial", 11)
    }

    interfaz_vectores(root, colores, fuentes)
    root.mainloop()