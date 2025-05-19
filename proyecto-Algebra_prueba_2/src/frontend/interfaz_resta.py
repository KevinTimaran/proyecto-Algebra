from tkinter import Frame, Label, Button, Entry

def interfaz_resta(parent, colores, fuentes):
    """
    Construye la interfaz gráfica para la operación de resta de matrices.

    Esta función se invoca desde la interfaz principal cuando el usuario selecciona "Restar Matrices".

    Parámetros:
    - parent: Frame donde se montará esta sección (típicamente self.area_principal).
    - colores: Diccionario de colores estándar definidos globalmente.
    - fuentes: Diccionario de fuentes tipográficas estándar.
    """

    # 🧱 Contenedor principal para los widgets de esta sección
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(padx=30, pady=30, fill="both", expand=True)

    # 🏷️ Título visual de la sección
    Label(
        frame,
        text="Resta de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # 📝 Instrucción inicial (puede eliminarse si no se desea)
    Label(
        frame,
        text="(Introduce las dos matrices del mismo tamaño para restarlas)",
        bg=colores['fondo_principal'],
        fg="#495057",
        font=fuentes['subtitulo']
    ).pack(pady=(0, 10))

    # -----------------------------
    # 📥 Entrada para matriz A
    # -----------------------------
    Label(
        frame,
        text="Matriz A (ejemplo: 1,2;3,4):",
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
        text="Matriz B (ejemplo: 5,6;7,8):",
        bg=colores['fondo_principal'],
        fg="#212529",
        font=fuentes['botones']
    ).pack(anchor="w", padx=5)

    entry_matriz_b = Entry(frame, width=50)
    entry_matriz_b.pack(pady=(0, 20))

    # -----------------------------
    # 🚀 Botón para ejecutar la operación
    # -----------------------------
    Button(
        frame,
        text="Calcular Resta",
        bg=colores['boton_normal'],
        fg=colores['texto_boton'],
        font=fuentes['botones'],
        activebackground=colores['boton_hover'],
        relief="flat",
        cursor="hand2"
    ).pack(pady=5)

    # 🧠 A partir de aquí, el compañero puede:
    # - Crear funciones internas para convertir los textos a matrices
    # - Verificar que ambas matrices sean del mismo tamaño
    # - Realizar la operación de resta con lógica de backend
    # - Mostrar el resultado visualmente con un nuevo Label o Frame
