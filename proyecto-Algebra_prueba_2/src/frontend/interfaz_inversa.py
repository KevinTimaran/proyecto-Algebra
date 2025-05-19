from tkinter import Frame, Label, Button, Entry

def interfaz_inversa(parent, colores, fuentes):
    """
    Construye la interfaz gráfica para calcular la inversa de una matriz.

    Esta función se conecta con el botón "Inversa de Matrices" en la GUI principal.

    Parámetros:
    - parent: Frame destino dentro de self.area_principal.
    - colores: Diccionario global de colores compartidos.
    - fuentes: Diccionario global de fuentes compartidas.
    """

    # 🧱 Crear contenedor principal de esta sección
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    # 🏷️ Título principal
    Label(
        frame,
        text="Inversa de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # ℹ️ Instrucción inicial para el usuario
    Label(
        frame,
        text="(Solo se admiten matrices cuadradas 2x2 o 3x3)",
        bg=colores['fondo_principal'],
        fg="#495057",
        font=fuentes['subtitulo']
    ).pack(pady=(0, 10))

    # -----------------------------
    # 📥 Entrada de matriz
    # -----------------------------
    Label(
        frame,
        text="Matriz (usa comas y punto y coma, ej: 1,2;3,4):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    entry_matriz = Entry(frame, width=50)
    entry_matriz.pack(pady=(0, 20))

    # -----------------------------
    # 🚀 Botón para calcular inversa
    # -----------------------------
    Button(
        frame,
        text="Calcular Inversa",
        bg=colores['boton_normal'],
        fg=colores['texto_boton'],
        font=fuentes['botones'],
        activebackground=colores['boton_hover'],
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)

    # 🧠 A partir de aquí, el compañero debe:
    # - Agregar funciones internas para convertir el texto en matriz
    # - Validar que sea 2x2 o 3x3 y que el determinante ≠ 0
    # - Calcular inversa usando el backend (por cofactores o fórmula directa)
    # - Mostrar la inversa en pantalla con Labels u otro método visual
