from tkinter import Frame, Label

def interfaz_resta(parent, colores, fuentes):
    """
    Construye la interfaz gráfica para la operación de Resta de Matrices.
    """
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    Label(
        frame,
        text="Resta de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # Aquí tu compañero puede agregar entradas, botones, resultados, etc.

    return frame
