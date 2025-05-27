from tkinter import Frame, Label, Entry, Button, StringVar
from tkinter.ttk import Combobox, Style
import tkinter as tk
import tkinter.messagebox as messagebox
import os, sys

# Ajuste de rutas
current_dir = os.path.dirname(os.path.abspath(__file__))
root_src_dir = os.path.dirname(current_dir)

if root_src_dir not in sys.path:
    sys.path.insert(0, root_src_dir)

# Importación del backend
from backend.vectores import suma_vectores, resta_vectores, producto_punto, producto_cruz, angulo_entre_vectores, modulo_vector as magnitud_vector, multiplicar_por_escalar as multiplicacion_por_escalar

def interfaz_vectores(parent, colores, fuentes):
    """
    Carga la interfaz de operaciones con vectores en el área principal.
    Esta versión solo muestra las operaciones sin gráficas.
    """
    # Frame principal
    frame = Frame(parent, bg=colores['fondo_principal'])
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título principal
    Label(
        frame,
        text="Operaciones con Vectores",
        bg=colores['fondo_principal'],
        fg=colores['titulo'],
        font=fuentes['titulo']
    ).pack(pady=(0, 15))

    # Selector de operaciones
    opciones = [
        "Suma", "Resta", "Multiplicación por escalar",
        "Producto punto", "Producto cruz", "Magnitud", "Ángulo entre vectores",
        "Componentes rectangulares"
    ]
    
    # Frame para controles
    control_frame = Frame(frame, bg=colores['fondo_principal'])
    control_frame.pack(fill="x", pady=10)
    
    Label(control_frame, 
          text="Seleccione operación:", 
          bg=colores['fondo_principal'],
          font=fuentes['botones']).pack(side="left", padx=5)
    
    cmb_opciones = Combobox(control_frame, values=opciones, state="readonly", width=25)
    cmb_opciones.pack(side="left", padx=5)
    cmb_opciones.current(0)

    # Frame para operaciones
    operacion_frame = Frame(frame, bg=colores['fondo_principal'], bd=2, relief="groove")
    operacion_frame.pack(fill="both", expand=True, pady=10, padx=10)

    # Resultado
    resultado_var = StringVar()
    resultado_label = Label(frame, 
                          textvariable=resultado_var,
                          bg=colores['fondo_principal'],
                          fg="#000000",
                          font=fuentes['botones'],
                          justify="left",
                          wraplength=600)
    resultado_label.pack(pady=10)

    def mostrar_operacion(operacion):
        # Limpiar frame de operación
        for widget in operacion_frame.winfo_children():
            widget.destroy()
        
        if operacion == "Suma":
            setup_suma()
        elif operacion == "Resta":
            setup_resta()
        elif operacion == "Multiplicación por escalar":
            setup_multiplicacion()
        elif operacion == "Producto punto":
            setup_producto_punto()
        elif operacion == "Producto cruz":
            setup_producto_cruz()
        elif operacion == "Magnitud":
            setup_magnitud()
        elif operacion == "Ángulo entre vectores":
            setup_angulo()
        elif operacion == "Componentes rectangulares":
            setup_componentes_rectangulares()

    def setup_suma():
        Label(operacion_frame, 
              text="Suma de Vectores (A + B)",
              bg=operacion_frame['bg'],
              font=fuentes['subtitulo']).pack(pady=5)
        
        frame_inputs = Frame(operacion_frame, bg=operacion_frame['bg'])
        frame_inputs.pack(pady=10)
        
        # Vector A
        Label(frame_inputs, 
              text="Vector A :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_a = Entry(frame_inputs, width=30)
        entry_a.grid(row=0, column=1, padx=5)
        entry_a.insert(0, "1,2,3")
        
        # Vector B
        Label(frame_inputs, 
              text="Vector B :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=1, column=0, padx=5, sticky="e")
        entry_b = Entry(frame_inputs, width=30)
        entry_b.grid(row=1, column=1, padx=5)
        entry_b.insert(0, "4,5,6")
        
        # Botón calcular
        Button(operacion_frame,
               text="Calcular Suma",
               command=lambda: calcular_suma(entry_a.get(), entry_b.get()),
               bg=colores['boton_normal'],
               fg=colores['texto_boton'],
               font=fuentes['botones']).pack(pady=10)
    
    def calcular_suma(a_str, b_str):
        try:
            a = [float(x.strip()) for x in a_str.split(',')]
            b = [float(x.strip()) for x in b_str.split(',')]
            
            if len(a) != len(b):
                resultado_var.set("Error: Los vectores deben tener la misma dimensión")
                return
                
            resultado = suma_vectores(a, b)
            resultado_var.set(f"Resultado: {resultado}")
            
        except ValueError:
            resultado_var.set("Error: Ingrese vectores válidos (números separados por comas)")

    def setup_resta():
        Label(operacion_frame, 
              text="Resta de Vectores (A - B)",
              bg=operacion_frame['bg'],
              font=fuentes['subtitulo']).pack(pady=5)
        
        frame_inputs = Frame(operacion_frame, bg=operacion_frame['bg'])
        frame_inputs.pack(pady=10)
        
        # Vector A
        Label(frame_inputs, 
              text="Vector A :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_a = Entry(frame_inputs, width=30)
        entry_a.grid(row=0, column=1, padx=5)
        entry_a.insert(0, "1,2,3")
        
        # Vector B
        Label(frame_inputs, 
              text="Vector B :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=1, column=0, padx=5, sticky="e")
        entry_b = Entry(frame_inputs, width=30)
        entry_b.grid(row=1, column=1, padx=5)
        entry_b.insert(0, "4,5,6")
        
        # Botón calcular
        Button(operacion_frame,
               text="Calcular Resta",
               command=lambda: calcular_resta(entry_a.get(), entry_b.get()),
               bg=colores['boton_normal'],
               fg=colores['texto_boton'],
               font=fuentes['botones']).pack(pady=10)
    
    def calcular_resta(a_str, b_str):
        try:
            a = [float(x.strip()) for x in a_str.split(',')]
            b = [float(x.strip()) for x in b_str.split(',')]
            
            if len(a) != len(b):
                resultado_var.set("Error: Los vectores deben tener la misma dimensión")
                return
                
            resultado = resta_vectores(a, b)
            resultado_var.set(f"Resultado: {resultado}")
            
        except ValueError:
            resultado_var.set("Error: Ingrese vectores válidos (números separados por comas)")

    def setup_multiplicacion():
        Label(operacion_frame, 
              text="Multiplicación por Escalar",
              bg=operacion_frame['bg'],
              font=fuentes['subtitulo']).pack(pady=5)
        
        frame_inputs = Frame(operacion_frame, bg=operacion_frame['bg'])
        frame_inputs.pack(pady=10)
        
        # Vector
        Label(frame_inputs, 
              text="Vector:",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_vec = Entry(frame_inputs, width=30)
        entry_vec.grid(row=0, column=1, padx=5)
        entry_vec.insert(0, "1,2,3")
        
        # Escalar
        Label(frame_inputs, 
              text="Escalar:",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=1, column=0, padx=5, sticky="e")
        entry_esc = Entry(frame_inputs, width=30)
        entry_esc.grid(row=1, column=1, padx=5)
        entry_esc.insert(0, "2")
        
        # Botón calcular
        Button(operacion_frame,
               text="Calcular Multiplicación",
               command=lambda: calcular_multiplicacion(entry_vec.get(), entry_esc.get()),
               bg=colores['boton_normal'],
               fg=colores['texto_boton'],
               font=fuentes['botones']).pack(pady=10)
    
    def calcular_multiplicacion(vec_str, esc_str):
        try:
            vector = [float(x.strip()) for x in vec_str.split(',')]
            escalar = float(esc_str)
            
            resultado = multiplicacion_por_escalar(vector, escalar)
            resultado_var.set(f"Resultado: {resultado}")
            
        except ValueError:
            resultado_var.set("Error: Ingrese valores válidos")

    def setup_producto_punto():
        Label(operacion_frame, 
              text="Producto Punto (A · B)",
              bg=operacion_frame['bg'],
              font=fuentes['subtitulo']).pack(pady=5)
        
        frame_inputs = Frame(operacion_frame, bg=operacion_frame['bg'])
        frame_inputs.pack(pady=10)
        
        # Vector A
        Label(frame_inputs, 
              text="Vector A :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_a = Entry(frame_inputs, width=30)
        entry_a.grid(row=0, column=1, padx=5)
        entry_a.insert(0, "1,2,3")
        
        # Vector B
        Label(frame_inputs, 
              text="Vector B :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=1, column=0, padx=5, sticky="e")
        entry_b = Entry(frame_inputs, width=30)
        entry_b.grid(row=1, column=1, padx=5)
        entry_b.insert(0, "4,5,6")
        
        # Botón calcular
        Button(operacion_frame,
               text="Calcular Producto Punto",
               command=lambda: calcular_producto_punto(entry_a.get(), entry_b.get()),
               bg=colores['boton_normal'],
               fg=colores['texto_boton'],
               font=fuentes['botones']).pack(pady=10)
    
    def calcular_producto_punto(a_str, b_str):
        try:
            a = [float(x.strip()) for x in a_str.split(',')]
            b = [float(x.strip()) for x in b_str.split(',')]
            
            if len(a) != len(b):
                resultado_var.set("Error: Los vectores deben tener la misma dimensión")
                return
                
            resultado = producto_punto(a, b)
            resultado_var.set(f"Resultado: {resultado}")
            
        except ValueError:
            resultado_var.set("Error: Ingrese vectores válidos (números separados por comas)")

    def setup_producto_cruz():
        Label(operacion_frame, 
              text="Producto Cruz (A × B) - Solo 3D",
              bg=operacion_frame['bg'],
              font=fuentes['subtitulo']).pack(pady=5)
        
        frame_inputs = Frame(operacion_frame, bg=operacion_frame['bg'])
        frame_inputs.pack(pady=10)
        
        # Vector A
        Label(frame_inputs, 
              text="Vector A :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_a = Entry(frame_inputs, width=30)
        entry_a.grid(row=0, column=1, padx=5)
        entry_a.insert(0, "1,2,3")
        
        # Vector B
        Label(frame_inputs, 
              text="Vector B :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=1, column=0, padx=5, sticky="e")
        entry_b = Entry(frame_inputs, width=30)
        entry_b.grid(row=1, column=1, padx=5)
        entry_b.insert(0, "4,5,6")
        
        # Botón calcular
        Button(operacion_frame,
               text="Calcular Producto Cruz",
               command=lambda: calcular_producto_cruz(entry_a.get(), entry_b.get()),
               bg=colores['boton_normal'],
               fg=colores['texto_boton'],
               font=fuentes['botones']).pack(pady=10)
    
    def calcular_producto_cruz(a_str, b_str):
        try:
            a = [float(x.strip()) for x in a_str.split(',')]
            b = [float(x.strip()) for x in b_str.split(',')]
            
            if len(a) != 3 or len(b) != 3:
                resultado_var.set("Error: El producto cruz solo funciona con vectores 3D")
                return
                
            resultado = producto_cruz(a, b)
            resultado_var.set(f"Resultado: {resultado}")
            
        except ValueError:
            resultado_var.set("Error: Ingrese vectores válidos (3 números separados por comas)")

    def setup_magnitud():
        Label(operacion_frame, 
              text="Magnitud de un Vector",
              bg=operacion_frame['bg'],
              font=fuentes['subtitulo']).pack(pady=5)
        
        frame_inputs = Frame(operacion_frame, bg=operacion_frame['bg'])
        frame_inputs.pack(pady=10)
        
        # Vector
        Label(frame_inputs, 
              text="Vector :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_vec = Entry(frame_inputs, width=30)
        entry_vec.grid(row=0, column=1, padx=5)
        entry_vec.insert(0, "1,2,3")
        
        # Botón calcular
        Button(operacion_frame,
               text="Calcular Magnitud",
               command=lambda: calcular_magnitud(entry_vec.get()),
               bg=colores['boton_normal'],
               fg=colores['texto_boton'],
               font=fuentes['botones']).pack(pady=10)
    
    def calcular_magnitud(vec_str):
        try:
            vector = [float(x.strip()) for x in vec_str.split(',')]
            resultado = magnitud_vector(vector)
            resultado_var.set(f"Magnitud: {resultado}")
            
        except ValueError:
            resultado_var.set("Error: Ingrese un vector válido (números separados por comas)")

    def setup_angulo():
        Label(operacion_frame, 
              text="Ángulo entre Vectores",
              bg=operacion_frame['bg'],
              font=fuentes['subtitulo']).pack(pady=5)
        
        frame_inputs = Frame(operacion_frame, bg=operacion_frame['bg'])
        frame_inputs.pack(pady=10)
        
        # Vector A
        Label(frame_inputs, 
              text="Vector A :",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_a = Entry(frame_inputs, width=30)
        entry_a.grid(row=0, column=1, padx=5)
        entry_a.insert(0, "1,0,0")
        
        # Vector B
        Label(frame_inputs, 
              text="Vector B:",
              bg=frame_inputs['bg'],
              font=fuentes['botones']).grid(row=1, column=0, padx=5, sticky="e")
        entry_b = Entry(frame_inputs, width=30)
        entry_b.grid(row=1, column=1, padx=5)
        entry_b.insert(0, "0,1,0")
        
        # Botón calcular
        Button(operacion_frame,
               text="Calcular Ángulo",
               command=lambda: calcular_angulo(entry_a.get(), entry_b.get()),
               bg=colores['boton_normal'],
               fg=colores['texto_boton'],
               font=fuentes['botones']).pack(pady=10)
    
    def calcular_angulo(a_str, b_str):
        try:
            a = [float(x.strip()) for x in a_str.split(',')]
            b = [float(x.strip()) for x in b_str.split(',')]
            
            if len(a) != len(b):
                resultado_var.set("Error: Los vectores deben tener la misma dimensión")
                return
                
            resultado = angulo_entre_vectores(a, b)
            resultado_var.set(f"Ángulo: {resultado}°")
            
        except ValueError:
            resultado_var.set("Error: Ingrese vectores válidos (números separados por comas)")

    # Configurar eventos
    cmb_opciones.bind("<<ComboboxSelected>>", lambda e: mostrar_operacion(cmb_opciones.get()))
    
    def setup_componentes_rectangulares():
            
        Label(operacion_frame, 
            text="Componentes Rectangulares",
            bg=operacion_frame['bg'],
            font=fuentes['subtitulo']).pack(pady=5)

        frame_inputs = Frame(operacion_frame, bg=operacion_frame['bg'])
        frame_inputs.pack(pady=10)

        # Magnitud
        Label(frame_inputs, 
            text="Magnitud:",
            bg=frame_inputs['bg'],
            font=fuentes['botones']).grid(row=0, column=0, padx=5, sticky="e")
        entry_mag = Entry(frame_inputs, width=30)
        entry_mag.grid(row=0, column=1, padx=5)
        entry_mag.insert(0, "10")

        # Ángulo
        Label(frame_inputs, 
            text="Ángulo (°):",
            bg=frame_inputs['bg'],
            font=fuentes['botones']).grid(row=1, column=0, padx=5, sticky="e")
        entry_ang = Entry(frame_inputs, width=30)
        entry_ang.grid(row=1, column=1, padx=5)
        entry_ang.insert(0, "45")

        # Botón calcular
        Button(operacion_frame,
            text="Calcular Componentes",
            command=lambda: calcular_componentes(entry_mag.get(), entry_ang.get()),
            bg=colores['boton_normal'],
            fg=colores['texto_boton'],
            font=fuentes['botones']).pack(pady=10)

    def calcular_componentes(mag_str, ang_str):
        from backend.vectores import componentes_rectangulares
        try:
            mag = float(mag_str)
            ang = float(ang_str)
            resultado = componentes_rectangulares(mag, ang)
            resultado_var.set(f"Componentes rectangulares: {resultado}")
        except ValueError:
            resultado_var.set("Error: Ingrese números válidos para magnitud y ángulo")



    # Mostrar operación inicial
    mostrar_operacion(cmb_opciones.get())

    return frame
    

# Bloque de prueba
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Operaciones con Vectores")
    root.geometry("800x600")
    
    colores = {
        'fondo_principal': "#f8f9fa",
        'titulo': "#212529",
        'boton_normal': "#6c757d",
        'boton_hover': "#5a6268",
        'texto_boton': "white"
    }
    
    fuentes = {
        'titulo': ("Arial", 16, "bold"),
        'subtitulo': ("Arial", 12),
        'botones': ("Arial", 10)
    }
    
    interfaz_vectores(root, colores, fuentes)
    root.mainloop()