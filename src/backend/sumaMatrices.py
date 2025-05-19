# sumaMatrices.py

def crear_matriz(filas, columnas, datos):
    """
    Valida y crea una matriz a partir de datos ingresados.
    :param filas: número de filas esperadas
    :param columnas: número de columnas esperadas
    :param datos: lista de listas con los valores
    :return: matriz válida o mensaje de error (str)
    """
    if len(datos) != filas:
        return "Error: el número de filas no coincide con los datos."

    for fila in datos:
        if len(fila) != columnas:
            return "Error: el número de columnas no coincide con los datos."
        for valor in fila:
            try:
                float(valor)  # verificar si es un número
            except ValueError:
                return "Error: todos los elementos deben ser números reales."

    # Si todo está bien, convertir todo a float
    matriz = [[float(valor) for valor in fila] for fila in datos]
    return matriz


def sumar_matrices(A, B):
    """
    Suma dos matrices A y B del mismo tamaño.
    :param A: matriz A (lista de listas)
    :param B: matriz B (lista de listas)
    :return: matriz suma (lista de listas) o mensaje de error (str)
    """
    if len(A) != len(B):
        return "Error: Las matrices no tienen el mismo número de filas."

    if len(A[0]) != len(B[0]):
        return "Error: Las matrices no tienen el mismo número de columnas."

    resultado = []
    for i in range(len(A)):
        fila_resultado = []
        for j in range(len(A[0])):
            suma = A[i][j] + B[i][j]
            fila_resultado.append(round(suma, 2))
        resultado.append(fila_resultado)

    return resultado
