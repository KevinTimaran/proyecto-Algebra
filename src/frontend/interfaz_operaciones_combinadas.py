import tkinter as tk
from tkinter import messagebox, ttk

def interfaz_operaciones_combinadas(parent, colores, fuentes):
    # Asegurarnos de que todas las claves necesarias existan
    colores.setdefault('texto_resultado', '#000000')  # Negro por defecto
    colores.setdefault('boton_secundario', '#2196F3')  # Azul por defecto
    fuentes.setdefault('entradas', ('Arial', 10))  # Fuente por defecto para entradas
    fuentes.setdefault('resultado', ('Consolas', 10))  # Fuente monoespaciada para resultados

    frame = tk.Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    def construir_formulario():
        for widget in entradas_frame.winfo_children():
            widget.destroy()

        try:
            filas = int(entry_filas.get())
            columnas = int(entry_columnas.get())
            if filas <= 0 or columnas <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Filas y columnas deben ser enteros positivos.")
            return

        modo = modo_var.get()

        # Frame para matrices
        matrices_frame = tk.Frame(entradas_frame, bg=colores['fondo_principal'])
        matrices_frame.pack(pady=10)

        # Frame para matriz A
        frame_A = tk.Frame(matrices_frame, bg=colores['fondo_principal'])
        frame_A.pack(side="left", padx=20)

        tk.Label(frame_A, text="Matriz A", bg=colores['fondo_principal'], 
                font=fuentes['subtitulo']).pack()

        entries_A = []
        for i in range(filas):
            fila_frame = tk.Frame(frame_A, bg=colores['fondo_principal'])
            fila_frame.pack()
            fila = []
            for j in range(columnas):
                e = tk.Entry(fila_frame, width=5, font=fuentes['entradas'], justify="center")
                e.pack(side="left", padx=2, pady=2)
                e.insert(0, "0")  # Valor por defecto
                fila.append(e)
            entries_A.append(fila)

        entries_B = []
        entry_beta = None

        if "Combinada" in modo:
            # Frame para matriz B
            frame_B = tk.Frame(matrices_frame, bg=colores['fondo_principal'])
            frame_B.pack(side="left", padx=20)

            tk.Label(frame_B, text="Matriz B", bg=colores['fondo_principal'], 
                    font=fuentes['subtitulo']).pack()

            for i in range(filas):
                fila_frame = tk.Frame(frame_B, bg=colores['fondo_principal'])
                fila_frame.pack()
                fila = []
                for j in range(columnas):
                    e = tk.Entry(fila_frame, width=5, font=fuentes['entradas'], justify="center")
                    e.pack(side="left", padx=2, pady=2)
                    e.insert(0, "0")  # Valor por defecto
                    fila.append(e)
                entries_B.append(fila)

        # Frame para escalares
        escalares_frame = tk.Frame(entradas_frame, bg=colores['fondo_principal'])
        escalares_frame.pack(pady=10)

        tk.Label(escalares_frame, text="Escalar α:", bg=colores['fondo_principal'], 
                font=fuentes['botones']).pack(side="left")
        entry_alpha = tk.Entry(escalares_frame, width=5, font=fuentes['entradas'])
        entry_alpha.pack(side="left", padx=5)
        entry_alpha.insert(0, "1.0")

        if "Combinada" in modo:
            tk.Label(escalares_frame, text="Escalar β:", bg=colores['fondo_principal'], 
                    font=fuentes['botones']).pack(side="left", padx=(20, 5))
            entry_beta = tk.Entry(escalares_frame, width=5, font=fuentes['entradas'])
            entry_beta.pack(side="left")
            entry_beta.insert(0, "1.0")

        # Frame para botón calcular
        boton_frame = tk.Frame(entradas_frame, bg=colores['fondo_principal'])
        boton_frame.pack(pady=20)

        def leer_matriz(entries):
            try:
                return [[float(e.get()) for e in fila] for fila in entries], None
            except ValueError:
                return None, "Todos los valores de la matriz deben ser números."

        def calcular():
            A, errA = leer_matriz(entries_A)
            if errA:
                messagebox.showerror("Error en matriz A", errA)
                return

            try:
                alpha = float(entry_alpha.get())
            except:
                messagebox.showerror("Error en α", "α debe ser un número.")
                return

            if "Combinada" in modo:
                B, errB = leer_matriz(entries_B)
                if errB:
                    messagebox.showerror("Error en matriz B", errB)
                    return
                try:
                    beta = float(entry_beta.get())
                except:
                    messagebox.showerror("Error en β", "β debe ser un número.")
                    return

                resultado = [[round(alpha * a + beta * b, 2) for a, b in zip(fa, fb)] for fa, fb in zip(A, B)]
            else:
                resultado = [[round(alpha * val, 2) for val in fila] for fila in A]

            # Formatear el resultado como matriz
            texto = "Resultado:\n"
            for fila in resultado:
                texto += "| " + "  ".join(f"{val:>7.2f}" for val in fila) + " |\n"
            resultado_var.set(texto)

        tk.Button(boton_frame, text="Calcular",
                bg=colores['boton_normal'], fg=colores['texto_boton'],
                font=fuentes['botones'], relief="flat",
                activebackground=colores['boton_hover'],
                cursor="hand2", command=calcular).pack()

    # Título
    tk.Label(frame, text="Operación con Matrices",
            bg=colores['fondo_principal'], fg=colores['titulo'],
            font=fuentes['titulo']).pack(pady=(0, 20))

    # Controles superiores
    controles_frame = tk.Frame(frame, bg=colores['fondo_principal'])
    controles_frame.pack(fill="x", pady=(0, 15))

    # Selector de modo
    modo_var = tk.StringVar(value="Combinada (αA + βB)")
    tk.Label(controles_frame, text="Tipo de operación:", 
            bg=colores['fondo_principal'], font=fuentes['botones']).pack(side="left", padx=(0, 10))
    selector = ttk.Combobox(controles_frame, textvariable=modo_var, 
                          values=["Combinada (αA + βB)", "Escalar (αA)"],
                          state="readonly", font=fuentes['botones'], width=20)
    selector.pack(side="left")

    # Tamaño de matriz
    size_frame = tk.Frame(controles_frame, bg=colores['fondo_principal'])
    size_frame.pack(side="right")
    
    tk.Label(size_frame, text="Tamaño:", bg=colores['fondo_principal'], 
            font=fuentes['botones']).pack(side="left")
    
    tk.Label(size_frame, text="Filas:", bg=colores['fondo_principal'], 
            font=fuentes['botones']).pack(side="left", padx=(10, 2))
    entry_filas = tk.Entry(size_frame, width=3, font=fuentes['botones'])
    entry_filas.insert(0, "2")
    entry_filas.pack(side="left", padx=2)

    tk.Label(size_frame, text="Columnas:", bg=colores['fondo_principal'], 
            font=fuentes['botones']).pack(side="left", padx=(10, 2))
    entry_columnas = tk.Entry(size_frame, width=3, font=fuentes['botones'])
    entry_columnas.insert(0, "2")
    entry_columnas.pack(side="left", padx=2)

    btn_actualizar = tk.Button(size_frame, text="Actualizar", 
                             font=fuentes['botones'], command=construir_formulario,
                             bg=colores['boton_secundario'], fg=colores['texto_boton'],
                             relief="flat", cursor="hand2")
    btn_actualizar.pack(side="left", padx=(10, 0))

    # Frame para entradas
    entradas_frame = tk.Frame(frame, bg=colores['fondo_principal'])
    entradas_frame.pack(fill="both", expand=True)

    # Frame para resultado
    resultado_frame = tk.Frame(frame, bg=colores['fondo_principal'])
    resultado_frame.pack(fill="x", pady=(10, 0))
    
    resultado_var = tk.StringVar()
    tk.Label(resultado_frame, textvariable=resultado_var, bg=colores['fondo_principal'],
            fg=colores['texto_resultado'], font=fuentes['resultado'], 
            justify="left").pack()

    # Eventos
    selector.bind("<<ComboboxSelected>>", lambda e: construir_formulario())
    entry_filas.bind("<Return>", lambda e: construir_formulario())
    entry_columnas.bind("<Return>", lambda e: construir_formulario())

    construir_formulario()
    return frame