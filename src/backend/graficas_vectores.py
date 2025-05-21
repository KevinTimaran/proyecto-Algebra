# src/backend/graficas_vectores.py

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar_vectores_en_2d(canvas_parent, vectores, colores=None, labels=None, titulo=""):
    """
    Dibuja uno o más vectores en un gráfico 2D dentro de un frame de Tkinter.
    
    Parámetros:
    - canvas_parent: el frame de Tkinter donde se insertará la gráfica.
    - vectores: lista de vectores [[x1, y1], [x2, y2], ...]
    - colores: lista opcional de colores ['red', 'blue']
    - labels: lista opcional de etiquetas ['A', 'B']
    - titulo: título opcional del gráfico.
    """
    fig, ax = plt.subplots(figsize=(4.5, 4))
    ax.set_title(titulo)
    ax.axhline(0, color='gray', lw=0.5)
    ax.axvline(0, color='gray', lw=0.5)
    ax.grid(True)
    ax.set_aspect('equal')

    max_val = max([abs(coord) for v in vectores for coord in v] + [1])
    ax.set_xlim(-max_val - 1, max_val + 1)
    ax.set_ylim(-max_val - 1, max_val + 1)

    for i, v in enumerate(vectores):
        color = colores[i] if colores and i < len(colores) else None
        label = labels[i] if labels and i < len(labels) else None
        ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

    if labels:
        ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=canvas_parent)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
