# multiplicacionMatrices.py
# Módulo para multiplicar matrices A x B con validación de dimensiones

def es_matriz_valida(matriz):
    """
    Verifica que una matriz sea válida:
    - No vacía
    - Todas las filas del mismo largo
    - Todos los elementos son números
    """
    if not matriz or not isinstance(matriz, list):
        return False, "Error: La matriz no puede estar vacía."

    columnas = len(matriz[0])
    for fila in matriz:
        if len(fila) != columnas:
            return False, "Error: Las filas de la matriz deben tener la misma longitud."
        for valor in fila:
            if not isinstance(valor, (int, float)):
                return False, "Error: Todos los elementos deben ser números reales."

    return True, ""


def multiplicar_matrices(A, B):
    """
    Multiplica dos matrices A y B si sus dimensiones son compatibles.
    :param A: matriz A (m x n)
    :param B: matriz B (n x p)
    :return: matriz resultante (m x p) o mensaje de error (str)
    """
    # Validar ambas matrices
    valida_A, error_A = es_matriz_valida(A)
    valida_B, error_B = es_matriz_valida(B)

    if not valida_A:
        return error_A
    if not valida_B:
        return error_B

    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])

    # Validar compatibilidad para multiplicación
    if columnas_A != filas_B:
        return "Error: No se puede multiplicar. Columnas de A deben ser iguales a filas de B."

    # Multiplicación A x B
    resultado = []
    for i in range(filas_A):
        fila_resultado = []
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):  # o filas_B
                suma += A[i][k] * B[k][j]
            fila_resultado.append(round(suma, 2))
        resultado.append(fila_resultado)

    return resultado


def formatear_matriz(matriz):
    """
    Devuelve una cadena con formato visual para mostrar una matriz.
    """
    return "\n".join(["\t".join(f"{valor:7.2f}" for valor in fila) for fila in matriz])
