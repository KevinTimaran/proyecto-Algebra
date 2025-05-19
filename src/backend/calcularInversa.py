# calcularInversa.py
# Módulo para calcular determinantes e inversas de matrices 2x2 y 3x3

# ===================== Validaciones básicas ======================

def es_matriz_cuadrada(matriz):
    """
    Verifica si una matriz es cuadrada.
    """
    return all(len(fila) == len(matriz) for fila in matriz)

def es_matriz_valida(matriz):
    """
    Verifica si todos los elementos son numéricos y la matriz es cuadrada.
    Retorna una tupla (bool, mensaje).
    """
    if not matriz or not es_matriz_cuadrada(matriz):
        return False, "La matriz debe ser cuadrada para calcular su determinante."
    
    for fila in matriz:
        for elemento in fila:
            if not isinstance(elemento, (int, float)):
                return False, "Todos los elementos deben ser valores numéricos."
    
    return True, ""

# ===================== Determinantes ======================

def calcular_determinante(matriz):
    """
    Calcula el determinante de una matriz 2x2 o 3x3.
    Devuelve (valor, explicación) o lanza error si el tamaño es inválido.
    """
    n = len(matriz)
    
    if n == 2:
        a, b = matriz[0]
        c, d = matriz[1]
        explicacion = f"({a} * {d}) - ({b} * {c}) = {a*d} - {b*c}"
        return a * d - b * c, explicacion
    
    elif n == 3:
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        
        positivos = a*e*i + b*f*g + c*d*h
        negativos = c*e*g + b*d*i + a*f*h
        
        explicacion = (
            f"Positivos: {a}*{e}*{i} + {b}*{f}*{g} + {c}*{d}*{h} = {positivos}\n"
            f"Negativos: {c}*{e}*{g} + {b}*{d}*{i} + {a}*{f}*{h} = {negativos}\n"
            f"Resultado: {positivos} - {negativos} = {positivos - negativos}"
        )
        return positivos - negativos, explicacion
    
    else:
        raise ValueError("Solo se puede calcular el determinante de matrices 2x2 o 3x3.")

# ===================== Inversa de matriz 2x2 ======================

def matriz_inversa_2x2(matriz):
    """
    Calcula la inversa de una matriz 2x2.
    """
    det, _ = calcular_determinante(matriz)
    if det == 0:
        return "Error: La matriz no tiene inversa (determinante = 0)"
    
    a, b = matriz[0]
    c, d = matriz[1]
    
    inversa = [
        [round(d / det, 2), round(-b / det, 2)],
        [round(-c / det, 2), round(a / det, 2)]
    ]
    return inversa

# ===================== Cofactores (para 3x3) ======================

def calcular_menor(matriz, fila, columna):
    """
    Extrae el menor de una matriz (elimina fila y columna indicadas).
    """
    return [f[:columna] + f[columna+1:] for i, f in enumerate(matriz) if i != fila]

def determinante_2x2(m):
    """
    Calcula determinante de matriz 2x2.
    """
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def matriz_cofactores(matriz):
    """
    Calcula la matriz de cofactores para una matriz 3x3.
    """
    if len(matriz) != 3 or any(len(f) != 3 for f in matriz):
        return "Error: Los cofactores solo están implementados para matrices 3x3."

    cofactores = []
    for i in range(3):
        fila = []
        for j in range(3):
            menor = calcular_menor(matriz, i, j)
            det_menor = determinante_2x2(menor)
            signo = (-1) ** (i + j)
            fila.append(round(signo * det_menor, 2))
        cofactores.append(fila)
    
    return cofactores

# ===================== Inversa de matriz 3x3 ======================

def matriz_inversa_3x3(matriz):
    """
    Calcula la inversa de una matriz 3x3 usando cofactores y transposición.
    :param matriz: lista de listas 3x3
    :return: matriz inversa (lista de listas) o mensaje de error (str)
    """
    pass

def adjunta_traspuesta(cofactores):
    """
    Calcula la transpuesta de la matriz de cofactores (adjunta).
    :param cofactores: matriz de cofactores 3x3
    :return: adjunta transpuesta (lista de listas)
    """
    pass

def prueba_matriz_inversa():
    """
    Función de prueba para verificar el cálculo de la inversa en matrices 2x2 y 3x3.
    Se debe usar dentro del bloque __main__ para probar el módulo.
    """
    pass

# ===================== Mostrar matriz (opcional para GUI) ======================

def formatear_matriz(matriz):
    """
    Devuelve un string visualmente alineado para mostrar matrices.
    """
    return "\n".join(["\t".join([f"{elem:6.2f}" for elem in fila]) for fila in matriz])

# ===================== Bloque de prueba interna ======================

if __name__ == "__main__":
    # Aquí se puede llamar prueba_matriz_inversa() una vez implementada
    pass
