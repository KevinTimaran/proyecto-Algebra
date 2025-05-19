from tkinter import Frame, Label, Button, Entry

def interfaz_sumas(parent, colores, fuentes):
    """
    Construye la interfaz gráfica para la operación de suma de matrices.

    Esta función se llama desde la interfaz principal cuando el usuario selecciona "Sumar Matrices".

    Parámetros:
    - parent: Frame contenedor donde se insertará esta sección (self.area_principal).
    - colores: Diccionario de colores globales definidos en la interfaz principal.
    - fuentes: Diccionario de fuentes tipográficas usadas por toda la app.
    """

    # 🧱 Contenedor principal del módulo de suma
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    # 🏷️ Título de la sección
    Label(
        frame,
        text="Suma de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # ℹ️ Mensaje de guía temporal
    Label(
        frame,
        text="(Aquí puedes ingresar las dos matrices para sumarlas)",
        bg=colores['fondo_principal'],
        fg="#495057",
        font=fuentes['subtitulo']
    ).pack(pady=(0, 10))

    # -----------------------------
    # 📥 Entrada para matriz A
    # -----------------------------
    Label(
        frame,
        text="Matriz A (usa comas y punto y coma, ej: 1,2;3,4):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    entry_matriz_a = Entry(frame, width=50)
    entry_matriz_a.pack(pady=(0, 10))

    # -----------------------------
    # 📥 Entrada para matriz B
    # -----------------------------
    Label(
        frame,
        text="Matriz B (usa comas y punto y coma, ej: 5,6;7,8):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    entry_matriz_b = Entry(frame, width=50)
    entry_matriz_b.pack(pady=(0, 20))

    # -----------------------------
    # 🚀 Botón para calcular suma
    # -----------------------------
    Button(
        frame,
        text="Calcular Suma",
        bg=colores['boton_normal'],
        fg=colores['texto_boton'],
        font=fuentes['botones'],
        activebackground=colores['boton_hover'],
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)

    # 📝 A partir de aquí, el compañero debe:
    # - Agregar funciones internas para convertir texto a matriz (parseo)
    # - Validar tamaños iguales
    # - Realizar la suma (usando backend)
    # - Mostrar resultado en pantalla (con Label dinámico o nuevo frame)
