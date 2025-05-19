# vectores.py

import numpy as np
import math

def validar_vector(v):
    """
    Verifica que el vector sea una lista de números reales.
    """
    try:
        return [float(x) for x in v]
    except (ValueError, TypeError):
        return None

def suma_vectores(A, B):
    """
    Suma dos vectores A y B de igual tamaño.
    """
    A = validar_vector(A)
    B = validar_vector(B)
    
    if not A or not B:
        return "Error: Los vectores deben contener solo números."
    
    if len(A) != len(B):
        return "Error: Los vectores deben tener el mismo tamaño."
    
    return [round(a + b, 2) for a, b in zip(A, B)]

def resta_vectores(A, B):
    """
    Resta el vector B al vector A.
    """
    A = validar_vector(A)
    B = validar_vector(B)

    if not A or not B:
        return "Error: Los vectores deben contener solo números."
    
    if len(A) != len(B):
        return "Error: Los vectores deben tener el mismo tamaño."
    
    return [round(a - b, 2) for a, b in zip(A, B)]

def producto_punto(A, B):
    """
    Calcula el producto punto entre los vectores A y B.
    """
    A = validar_vector(A)
    B = validar_vector(B)

    if not A or not B:
        return "Error: Los vectores deben contener solo números."

    if len(A) != len(B):
        return "Error: Los vectores deben tener el mismo tamaño."
    
    return round(sum(a * b for a, b in zip(A, B)), 2)

def multiplicar_por_escalar(vector, escalar):
    """
    Multiplica un vector por un escalar.
    """
    vector = validar_vector(vector)

    try:
        escalar = float(escalar)
    except ValueError:
        return "Error: El escalar debe ser un número."

    if not vector:
        return "Error: El vector debe contener solo números."
    
    return [round(escalar * v, 2) for v in vector]

def producto_cruz(A, B):
    """
    Calcula el producto cruz entre dos vectores 3D.
    """
    A = validar_vector(A)
    B = validar_vector(B)

    if not A or not B:
        return "Error: Los vectores deben contener solo números."
    
    if len(A) != 3 or len(B) != 3:
        return "Error: El producto cruz solo está definido para vectores 3D."

    resultado = np.cross(A, B)
    return [round(x, 2) for x in resultado]

def componentes_rectangulares(magnitud, angulo_grados):
    """
    Convierte magnitud y ángulo a componentes rectangulares (x, y).
    Ángulo en grados desde el eje X positivo.
    """
    try:
        magnitud = float(magnitud)
        angulo_rad = math.radians(float(angulo_grados))
    except ValueError:
        return "Error: Magnitud y ángulo deben ser números."

    x = round(magnitud * math.cos(angulo_rad), 2)
    y = round(magnitud * math.sin(angulo_rad), 2)

    return [x, y]

def modulo_vector(vector):
    """
    Retorna la magnitud del vector.
    """
    vector = validar_vector(vector)
    if not vector:
        return "Error: El vector debe contener solo números."

    return round(math.sqrt(sum(v**2 for v in vector)), 2)

def angulo_entre_vectores(A, B):
    """
    Calcula el ángulo entre dos vectores en grados.
    """
    A = validar_vector(A)
    B = validar_vector(B)

    if not A or not B:
        return "Error: Los vectores deben contener solo números."

    if len(A) != len(B):
        return "Error: Los vectores deben tener el mismo tamaño."

    producto = producto_punto(A, B)
    modulo_A = modulo_vector(A)
    modulo_B = modulo_vector(B)

    if isinstance(producto, str) or isinstance(modulo_A, str) or isinstance(modulo_B, str):
        return "Error: No se pudo calcular el ángulo."

    if modulo_A == 0 or modulo_B == 0:
        return "Error: No se puede calcular ángulo con un vector nulo."

    cos_theta = producto / (modulo_A * modulo_B)
    cos_theta = max(min(cos_theta, 1), -1)  # limitar por seguridad
    angulo_rad = math.acos(cos_theta)
    angulo_deg = math.degrees(angulo_rad)

    return round(angulo_deg, 2)

def prueba_vectores():
    """
    Prueba general de operaciones vectoriales.
    """
    A = [3, 4]
    B = [1, 2]
    escalar = 2
    print("A =", A)
    print("B =", B)
    print("Suma:", suma_vectores(A, B))
    print("Resta:", resta_vectores(A, B))
    print("Punto:", producto_punto(A, B))
    print("Escalar por A:", multiplicar_por_escalar(A, escalar))
    print("Módulo A:", modulo_vector(A))
    print("Ángulo entre A y B:", angulo_entre_vectores(A, B))

    # Para producto cruz y componentes
    A3 = [1, 0, 0]
    B3 = [0, 1, 0]
    print("Producto cruz (A3 x B3):", producto_cruz(A3, B3))
    print("Componentes de magnitud=10, ángulo=45°:", componentes_rectangulares(10, 45))


if __name__ == "__main__":
    prueba_vectores()