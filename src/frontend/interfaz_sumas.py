# src/frontend/interfaz_suma.py

from tkinter import Frame, Label

def interfaz_suma(parent, colores, fuentes):
    """
    Construye la interfaz gráfica para la operación de Suma de Matrices.

    Parámetros:
    - parent: Frame contenedor donde se colocará esta interfaz (usualmente self.area_principal).
    - colores: Diccionario de colores globales definidos en la interfaz principal.
    - fuentes: Diccionario de fuentes globales definidos en la interfaz principal.
    """

    # ✅ Este frame debe mantenerse (no modificar)
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # ✅ Este título principal debe mantenerse
    Label(
        frame,
        text="Suma de Matrices",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 20))

    # 🔧 A partir de aquí, el compañero puede agregar entradas, botones, resultados, etc.
    # Por ejemplo: campos para matrices A y B, botón "Sumar", y área para mostrar la matriz resultado

    return frame  # Opcional: devolver el frame si se necesita manipular más tarde
