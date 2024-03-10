import numpy as np

# Matriz A de 2x3
matriz_A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Matriz B de 3x2 (diferente tamaño que la matriz A)
matriz_B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

# Intentar sumar las matrices de tamaños diferentes
try:
    matriz_suma = matriz_A + matriz_B
except ValueError as e:
    print("Error:", e)