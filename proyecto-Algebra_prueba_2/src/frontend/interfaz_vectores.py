from tkinter import Frame, Label, Button, Entry

def interfaz_vectores(parent, colores, fuentes):
    """
    Construye la interfaz gráfica para las operaciones con vectores.
    
    Esta función será llamada desde la ventana principal al presionar el botón "Vectores".

    Parámetros:
    - parent: Frame donde se insertará esta sección (normalmente self.area_principal)
    - colores: Diccionario de colores definidos en la interfaz principal
    - fuentes: Diccionario de fuentes tipográficas definidas en la interfaz principal
    """

    # 🧱 Crear un contenedor (Frame) dentro del área principal (parent)
    # Este frame contendrá todos los elementos de la interfaz de vectores
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    # 🏷️ Título principal de la sección
    # Le dice al usuario que está en el apartado de vectores
    Label(
        frame,
        text="Operaciones con Vectores",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # ℹ️ Instrucción o mensaje temporal de guía
    # Este mensaje puede ser borrado una vez se agregue contenido real
    Label(
        frame,
        text="(Aquí puedes construir tu interfaz para suma, producto, magnitud, etc.)",
        bg=colores['fondo_principal'],
        fg="#495057",
        font=fuentes['subtitulo']
    ).pack(pady=(0, 10))

    # --------------------
    # 📥 Entrada: Vector A
    # --------------------

    # Etiqueta para campo de entrada de Vector A
    Label(
        frame,
        text="Vector A (separado por comas):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    # Campo de entrada para Vector A
    entry_vector_a = Entry(frame, width=40)
    entry_vector_a.pack(pady=(0, 10))

    # --------------------
    # 📥 Entrada: Vector B
    # --------------------

    # Etiqueta para campo de entrada de Vector B
    Label(
        frame,
        text="Vector B (separado por comas):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    # Campo de entrada para Vector B
    entry_vector_b = Entry(frame, width=40)
    entry_vector_b.pack(pady=(0, 20))

    # -----------------------------
    # 🚀 Botón de acción de ejemplo
    # -----------------------------

    # Botón para simular una acción (por ejemplo: suma)
    # Este botón aún no realiza ninguna operación, solo está de ejemplo
    Button(
        frame,
        text="Calcular Suma",  # Aquí tu compañero puede cambiar el texto o la acción
        bg=colores['boton_normal'],
        fg=colores['texto_boton'],
        font=fuentes['botones'],
        activebackground=colores['boton_hover'],
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)

    # 📝 A partir de aquí, el compañero debe agregar:
    # - Más botones (producto punto, magnitud, ángulo)
    # - Funciones internas para validar y operar con los vectores
    # - Labels dinámicos para mostrar resultados
