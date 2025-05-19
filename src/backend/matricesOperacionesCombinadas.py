# src/backend/matricesOperacionesCombinadas.py
# Funciones: multiplicación por escalar y operación combinada αA + βB

def multiplicar_por_escalar(matriz, escalar):
    """
    Multiplica todos los elementos de la matriz por un escalar.
    :param matriz: lista de listas (matriz numérica)
    :param escalar: número (int o float)
    :return: nueva matriz resultante o None si la matriz no es válida o el escalar no es numérico.
    """
    if not isinstance(escalar, (int, float)):
        print("Error en multiplicar_por_escalar: El escalar debe ser un número (int o float).")
        return None

    valida, mensaje = es_matriz_valida(matriz)
    if not valida:
        if matriz: 
             print(f"Error al multiplicar por escalar: {mensaje}")
        return None if matriz else [] 

    matriz_resultante = []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            nueva_fila.append(elemento * escalar)
        matriz_resultante.append(nueva_fila)
    return matriz_resultante


def operacion_combinada(alpha, A, beta, B):
    """
    Calcula la operación αA + βB para matrices del mismo tamaño.
    :param alpha: escalar multiplicador de A
    :param A: matriz A (lista de listas)
    :param beta: escalar multiplicador de B
    :param B: matriz B (lista de listas)
    :return: matriz resultante αA + βB o None si hay errores.
    """
    if not isinstance(alpha, (int, float)):
        print("Error en operacion_combinada: El escalar alpha debe ser un número (int o float).")
        return None
    if not isinstance(beta, (int, float)):
        print("Error en operacion_combinada: El escalar beta debe ser un número (int o float).")
        return None

    valida_A, mensaje_A = es_matriz_valida(A)
    if not valida_A:
        print(f"Error en operacion_combinada: Matriz A no es válida. {mensaje_A}")
        return None
    valida_B, mensaje_B = es_matriz_valida(B)
    if not valida_B:
        print(f"Error en operacion_combinada: Matriz B no es válida. {mensaje_B}")
        return None

    if not dimensiones_iguales(A, B):
        print("Error en operacion_combinada: Las matrices A y B deben tener las mismas dimensiones.")
        return None

    if not A and not B: # Ambas son []
        return []
    if A == [[]] and B == [[]]: # Ambas son [[]]
        return [[]]

    matriz_alpha_A = multiplicar_por_escalar(A, alpha)
    if matriz_alpha_A is None and A: 
        return None

    matriz_beta_B = multiplicar_por_escalar(B, beta)
    if matriz_beta_B is None and B: 
        return None
    
    if matriz_alpha_A == [] and matriz_beta_B == []: # Resultado de multiplicar matrices vacías
        return []
    if matriz_alpha_A == [[]] and matriz_beta_B == [[]]: # Resultado de multiplicar matrices [[]]
        return [[]]

    num_filas = len(A)
    if num_filas == 0: return [] # Debería estar cubierto arriba, pero por si acaso
    num_columnas = len(A[0]) 

    matriz_suma = []
    for i in range(num_filas):
        fila_suma = []
        for j in range(num_columnas):
            suma_elemento = matriz_alpha_A[i][j] + matriz_beta_B[i][j]
            fila_suma.append(suma_elemento)
        matriz_suma.append(fila_suma)
    return matriz_suma


def es_matriz_valida(matriz):
    """
    Verifica que la matriz sea rectangular y numérica.
    """
    if not isinstance(matriz, list):
        return False, "La estructura principal de la matriz debe ser una lista."
    if not matriz:
        return True, "Matriz vacía." # Matriz vacía [] es válida

    num_columnas_primera_fila = -1
    for i, fila in enumerate(matriz):
        if not isinstance(fila, list):
            return False, f"Cada fila debe ser una lista. Fila en índice {i} no lo es."
        if i == 0:
            num_columnas_primera_fila = len(fila)
        elif len(fila) != num_columnas_primera_fila:
            return False, "Todas las filas deben tener el mismo número de columnas."
        for j, elemento in enumerate(fila):
            if not isinstance(elemento, (int, float)):
                return False, f"Elemento '{elemento}' en fila {i}, col {j} no es numérico."
    return True, "La matriz es válida."


def dimensiones_iguales(A, B):
    """
    Verifica si las matrices A y B tienen el mismo número de filas y columnas.
    """
    if not isinstance(A, list) or not isinstance(B, list):
        return False 
    if len(A) != len(B):
        return False
    if not A: # Ambas son []
        return True
    if not isinstance(A[0], list) or not isinstance(B[0], list): # Si no son [], deben tener filas como listas
        return False
    if len(A[0]) != len(B[0]):
        return False
    return True

# (Opcional) Para pruebas internas
if __name__ == "__main__":
    # ... (puedes añadir tus pruebas aquí si lo deseas) ...
    pass
