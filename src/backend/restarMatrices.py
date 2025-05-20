def restarMatrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])

    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila)

    return resultado
