import tkinter as tk
from tkinter import messagebox, ttk

def interfaz_operaciones_combinadas(parent, colores, fuentes):
    frame = tk.Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(frame, text="Operación con Matrices",
             bg=colores['fondo_principal'], fg=colores['titulo'],
             font=fuentes['titulo']).pack(pady=(0, 20))

    modo_var = tk.StringVar(value="Combinada (αA + βB)")
    selector = ttk.Combobox(frame, textvariable=modo_var, values=["Combinada (αA + βB)", "Escalar (αA)"],
                            state="readonly", font=fuentes['botones'], width=30)
    selector.pack(pady=(0, 10))

    subtitulo = tk.Label(frame, text="Selecciona el tipo de operación",
                         bg=colores['fondo_principal'], fg="#495057",
                         font=fuentes['subtitulo'])
    subtitulo.pack(pady=(0, 10))

    entradas_frame = tk.Frame(frame, bg=colores['fondo_principal'])
    entradas_frame.pack(pady=10)

    resultado_var = tk.StringVar()
    tk.Label(frame, textvariable=resultado_var, bg=colores['fondo_principal'],
             fg="#000", font=fuentes['botones'], justify="left").pack(pady=10)

    def limpiar_entradas():
        for widget in entradas_frame.winfo_children():
            widget.destroy()

    def construir_formulario():
        limpiar_entradas()
        modo = modo_var.get()

        tk.Label(entradas_frame, text="Matriz A:", bg=colores['fondo_principal'], font=fuentes['botones']).grid(row=0, column=0, sticky="w")
        entry_A = tk.Entry(entradas_frame, width=40)
        entry_A.insert(0, "1,2;3,4")
        entry_A.grid(row=0, column=1)

        tk.Label(entradas_frame, text="Escalar α:", bg=colores['fondo_principal'], font=fuentes['botones']).grid(row=1, column=0, sticky="w")
        entry_alpha = tk.Entry(entradas_frame, width=10)
        entry_alpha.insert(0, "1")
        entry_alpha.grid(row=1, column=1, sticky="w")

        entry_B = entry_beta = None
        if "Combinada" in modo:
            tk.Label(entradas_frame, text="Matriz B:", bg=colores['fondo_principal'], font=fuentes['botones']).grid(row=2, column=0, sticky="w")
            entry_B = tk.Entry(entradas_frame, width=40)
            entry_B.insert(0, "5,6;7,8")
            entry_B.grid(row=2, column=1)

            tk.Label(entradas_frame, text="Escalar β:", bg=colores['fondo_principal'], font=fuentes['botones']).grid(row=3, column=0, sticky="w")
            entry_beta = tk.Entry(entradas_frame, width=10)
            entry_beta.insert(0, "1")
            entry_beta.grid(row=3, column=1, sticky="w")

        def parsear_matriz(cadena):
            try:
                matriz = []
                filas = cadena.strip().split(';')
                for fila in filas:
                    fila_limpia = fila.replace(',', ' ').split()
                    matriz.append([float(x) for x in fila_limpia])
                return matriz, None
            except ValueError:
                return None, "Error: Valores no válidos en la matriz."

        def calcular():
            A, errA = parsear_matriz(entry_A.get())
            if errA:
                messagebox.showerror("Error matriz A", errA)
                return

            try:
                alpha = float(entry_alpha.get())
            except:
                messagebox.showerror("Error escalar α", "α debe ser un número.")
                return

            if entry_B and entry_beta:
                B, errB = parsear_matriz(entry_B.get())
                if errB:
                    messagebox.showerror("Error matriz B", errB)
                    return

                try:
                    beta = float(entry_beta.get())
                except:
                    messagebox.showerror("Error escalar β", "β debe ser un número.")
                    return

                if len(A) != len(B) or len(A[0]) != len(B[0]):
                    messagebox.showerror("Error", "Las matrices deben tener el mismo tamaño.")
                    return

                resultado = [[round(alpha * a + beta * b, 2) for a, b in zip(fa, fb)] for fa, fb in zip(A, B)]
            else:
                resultado = [[round(alpha * val, 2) for val in row] for row in A]

            texto = "\n".join("  ".join(f"{n:.2f}" for n in fila) for fila in resultado)
            resultado_var.set(f"Resultado:\n{texto}")

        tk.Button(entradas_frame, text="Calcular",
                  bg=colores['boton_normal'], fg=colores['texto_boton'],
                  font=fuentes['botones'], relief="flat",
                  activebackground=colores['boton_hover'],
                  cursor="hand2", command=calcular).grid(row=5, columnspan=2, pady=10)

    selector.bind("<<ComboboxSelected>>", lambda e: construir_formulario())
    construir_formulario()

    return frame
