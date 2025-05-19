# resolucionSistemas.py
# Módulo unificado con: Método de Cramer, determinante por Sarrus y cofactores (para sistemas 3x3)

import numpy as np

# ===================== Método de Cramer =====================

def resolver_cramer(A, B):
    """
    Resuelve el sistema AX = B usando el método de Cramer.
    Devuelve un diccionario con determinantes, matrices modificadas y solución.
    """
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    if A.shape[0] != A.shape[1]:
        return "Error: La matriz A debe ser cuadrada."

    d = np.linalg.det(A)

    if np.isclose(d, 0):
        return "Error: El sistema no tiene solución única (|A| = 0)."

    n = len(B)
    soluciones = []
    determinantes = []
    matrices = []

    for k in range(n):
        Ak = A.copy()
        Ak[:, k] = B
        det_Ak = np.linalg.det(Ak)
        determinantes.append(round(det_Ak, 4))
        matrices.append(Ak.tolist())
        soluciones.append(round(det_Ak / d, 4))

    return {
        "det_A": round(d, 4),
        "det_Ak": determinantes,
        "matrices_Ak": matrices,
        "solucion": soluciones
    }

# ===================== Determinante por Sarrus =====================

def determinante_sarrus(matriz):
    """
    Calcula el determinante de una matriz 3x3 por el método de Sarrus.
    """
    if len(matriz) != 3 or any(len(f) != 3 for f in matriz):
        return "Error: La matriz no es 3x3."

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    diag_principal = a * e * i + b * f * g + c * d * h
    diag_secundaria = c * e * g + a * f * h + b * d * i

    return round(diag_principal - diag_secundaria, 4)

# ===================== Matriz de Cofactores =====================

def calcular_cofactor(matriz, fila, columna):
    """
    Calcula el cofactor de un elemento en posición [fila][columna].
    """
    submatriz = np.delete(np.delete(matriz, fila, axis=0), columna, axis=1)
    det = np.linalg.det(submatriz)
    return round(((-1) ** (fila + columna)) * det, 4)

def matriz_de_cofactores(matriz):
    """
    Calcula la matriz de cofactores de una matriz 3x3.
    """
    matriz = np.array(matriz, dtype=float)
    if matriz.shape != (3, 3):
        return "Error: La matriz debe ser de tamaño 3x3."

    cofactores = np.zeros((3, 3))

    for i in range(3):
        for j in range(3):
            cofactores[i, j] = calcular_cofactor(matriz, i, j)

    return cofactores.round(4).tolist()

# ===================== Formateo (opcional para GUI) =====================

def formatear_matriz(matriz):
    """
    Devuelve una representación de texto de una matriz.
    """
    return "\n".join(["\t".join([f"{val:7.4f}" for val in fila]) for fila in matriz])
