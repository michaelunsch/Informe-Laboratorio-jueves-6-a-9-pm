import numpy as np

# Crear una matriz de ejemplo (puede tener un número impar o par de filas y columnas)
matriz_ejemplo = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Obtener las dimensiones de la matriz
filas, columnas = matriz_ejemplo.shape

# Acceder al elemento central
if filas % 2 == 1 and columnas % 2 == 1:  # Matriz con número impar de filas y columnas
    elemento_central = matriz_ejemplo[filas // 2, columnas // 2]
    print("Elemento central:", elemento_central)
else:  # Matriz con número par de filas y/o columnas
    fila_central_superior = filas // 2 - 1
    fila_central_inferior = filas // 2
    columna_central_izquierda = columnas // 2 - 1
    columna_central_derecha = columnas // 2

    elemento_central_superior_izquierda = matriz_ejemplo[fila_central_superior, columna_central_izquierda]
    elemento_central_superior_derecha = matriz_ejemplo[fila_central_superior, columna_central_derecha]
    elemento_central_inferior_izquierda = matriz_ejemplo[fila_central_inferior, columna_central_izquierda]
    elemento_central_inferior_derecha = matriz_ejemplo[fila_central_inferior, columna_central_derecha]

    print("Elementos centrales:", elemento_central_superior_izquierda, elemento_central_superior_derecha, elemento_central_inferior_izquierda, elemento_central_inferior_derecha)