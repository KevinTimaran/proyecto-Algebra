from tkinter import Frame, Label, Button, Entry

def interfaz_combinadas(parent, colores, fuentes):
    """
    Construye la interfaz gráfica para realizar operaciones combinadas entre matrices.

    Esta función se activa cuando el usuario presiona "Operaciones Combinadas" desde el menú principal.

    Parámetros:
    - parent: Frame donde se dibuja la sección (usualmente self.area_principal).
    - colores: Diccionario global de colores para mantener coherencia visual.
    - fuentes: Diccionario global de fuentes tipográficas usadas por la app.
    """

    # 🧱 Contenedor principal del módulo
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    # 🏷️ Título de la sección
    Label(
        frame,
        text="Operaciones Combinadas con Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # ℹ️ Instrucción inicial
    Label(
        frame,
        text="(Ejemplo: (A + B) × C — Las matrices deben tener tamaños compatibles)",
        bg=colores['fondo_principal'],
        fg="#495057",
        font=fuentes['subtitulo']
    ).pack(pady=(0, 10))

    # -----------------------------
    # 📥 Entrada para matriz A
    # -----------------------------
    Label(
        frame,
        text="Matriz A (ej: 1,2;3,4):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    entry_a = Entry(frame, width=50)
    entry_a.pack(pady=(0, 10))

    # 📥 Entrada para matriz B
    Label(
        frame,
        text="Matriz B (ej: 5,6;7,8):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    entry_b = Entry(frame, width=50)
    entry_b.pack(pady=(0, 10))

    # 📥 Entrada para matriz C
    Label(
        frame,
        text="Matriz C (ej: 1,0;0,1):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    entry_c = Entry(frame, width=50)
    entry_c.pack(pady=(0, 20))

    # -----------------------------
    # 🚀 Botón de operación combinada
    # -----------------------------
    Button(
        frame,
        text="Resolver (A + B) × C",
        bg=colores['boton_normal'],
        fg=colores['texto_boton'],
        font=fuentes['botones'],
        activebackground=colores['boton_hover'],
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)

    # 🧠 A partir de aquí, tu compañero debe:
    # - Leer y convertir A, B, C a listas de listas (matrices reales)
    # - Verificar que A y B sean del mismo tamaño, y que (A + B) pueda multiplicarse por C
    # - Realizar la operación combinada con funciones del backend
    # - Mostrar el resultado (por ejemplo, en un Label debajo)
