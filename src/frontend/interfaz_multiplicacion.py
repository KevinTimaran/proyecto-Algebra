from tkinter import Frame, Label, Button, Entry

def interfaz_multiplicacion(parent, colores, fuentes):
    """
    Construye la interfaz gráfica para multiplicación de matrices.

    Esta función es llamada desde la interfaz principal cuando el usuario selecciona "Multiplicar Matrices".

    Parámetros:
    - parent: Frame contenedor (viene de self.area_principal en la GUI).
    - colores: Diccionario de colores globales compartidos.
    - fuentes: Diccionario de fuentes tipográficas compartidas.
    """

    # 🧱 Crear un frame contenedor para todos los widgets de esta sección
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    # 🏷️ Título de sección
    Label(
        frame,
        text="Multiplicación de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # ℹ️ Instrucción inicial
    Label(
        frame,
        text="(Ingresa dos matrices compatibles: columnas de A = filas de B)",
        bg=colores['fondo_principal'],
        fg="#495057",
        font=fuentes['subtitulo']
    ).pack(pady=(0, 10))

    # -----------------------------
    # 📥 Entrada para Matriz A
    # -----------------------------
    Label(
        frame,
        text="Matriz A (ej: 1,2;3,4):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    entry_matriz_a = Entry(frame, width=50)
    entry_matriz_a.pack(pady=(0, 10))

    # -----------------------------
    # 📥 Entrada para Matriz B
    # -----------------------------
    Label(
        frame,
        text="Matriz B (ej: 5,6;7,8):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    entry_matriz_b = Entry(frame, width=50)
    entry_matriz_b.pack(pady=(0, 20))

    # -----------------------------
    # 🚀 Botón para multiplicar
    # -----------------------------
    Button(
        frame,
        text="Calcular Producto",
        bg=colores['boton_normal'],
        fg=colores['texto_boton'],
        font=fuentes['botones'],
        activebackground=colores['boton_hover'],
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)

    # 🧠 A partir de aquí, el compañero debe:
    # - Crear funciones internas para convertir texto → matriz
    # - Validar si columnas de A == filas de B
    # - Multiplicar matrices (usando módulo backend si existe)
    # - Mostrar el resultado visualmente (Label o tabla)
