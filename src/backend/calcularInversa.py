# calcularInversa.py
# Módulo para calcular determinantes e inversas de matrices 2x2 y 3x3

# ===================== Validaciones ======================

def es_matriz_cuadrada(matriz):
    return all(len(fila) == len(matriz) for fila in matriz)

def es_matriz_valida(matriz):
    if not matriz or not es_matriz_cuadrada(matriz):
        return False, "La matriz debe ser cuadrada para calcular su determinante."
    for fila in matriz:
        for elemento in fila:
            if not isinstance(elemento, (int, float)):
                return False, "Todos los elementos deben ser valores numéricos."
    return True, ""

# ===================== Determinante ======================

def calcular_determinante(matriz):
    n = len(matriz)
    if n == 2:
        a, b = matriz[0]
        c, d = matriz[1]
        return a * d - b * c, f"({a}*{d}) - ({b}*{c}) = {a*d - b*c}"
    elif n == 3:
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        positivos = a*e*i + b*f*g + c*d*h
        negativos = c*e*g + b*d*i + a*f*h
        return positivos - negativos, f"{positivos} - {negativos} = {positivos - negativos}"
    else:
        raise ValueError("Solo se permite matriz 2x2 o 3x3.")

# ===================== Inversa 2x2 ======================

def matriz_inversa_2x2(matriz):
    det, _ = calcular_determinante(matriz)
    if det == 0:
        return "Error: La matriz no tiene inversa (determinante = 0)"
    a, b = matriz[0]
    c, d = matriz[1]
    return [
        [round(d / det, 2), round(-b / det, 2)],
        [round(-c / det, 2), round(a / det, 2)]
    ]

# ===================== Cofactores para 3x3 ======================

def calcular_menor(matriz, fila, columna):
    return [f[:columna] + f[columna+1:] for i, f in enumerate(matriz) if i != fila]

def determinante_2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def matriz_cofactores(matriz):
    cofactores = []
    for i in range(3):
        fila = []
        for j in range(3):
            menor = calcular_menor(matriz, i, j)
            signo = (-1) ** (i + j)
            fila.append(round(signo * determinante_2x2(menor), 2))
        cofactores.append(fila)
    return cofactores

def adjunta_traspuesta(cofactores):
    return [[cofactores[j][i] for j in range(3)] for i in range(3)]

# ===================== Inversa 3x3 ======================

def matriz_inversa_3x3(matriz):
    valido, mensaje = es_matriz_valida(matriz)
    if not valido:
        return mensaje
    det, _ = calcular_determinante(matriz)
    if det == 0:
        return "Error: La matriz no tiene inversa (determinante = 0)"
    cofactores = matriz_cofactores(matriz)
    adjunta = adjunta_traspuesta(cofactores)
    return [[round(adjunta[i][j] / det, 2) for j in range(3)] for i in range(3)]

# ===================== Utilidad ======================

def formatear_matriz(matriz):
    return "\n".join(["\t".join([f"{elem:6.2f}" for elem in fila]) for fila in matriz])

def prueba_matriz_inversa():
    print("Matriz 2x2:")
    print(formatear_matriz(matriz_inversa_2x2([[4, 7], [2, 6]])))
    print("\nMatriz 3x3:")
    print(formatear_matriz(matriz_inversa_3x3([[2, -1, 0], [1, 2, 1], [3, 0, 1]])))

if __name__ == "__main__":
    prueba_matriz_inversa()