import numpy as np

def encontrar_maximo(matriz):
    """
    Encuentra el elemento máximo de una matriz.

    Parámetros:
    - matriz: NumPy array, la matriz de entrada.

    Retorna:
    - maximo: el valor máximo encontrado en la matriz.
    """
    maximo = np.max(matriz)
    return maximo

# Crear una matriz de ejemplo
matriz_ejemplo = np.array([
    [1, 2, 3],
    [4, 8, 6],
    [7, 8, 9]
])

# Llamar a la función para encontrar el máximo
maximo_encontrado = encontrar_maximo(matriz_ejemplo)

# Imprimir el resultado
print("Matriz:")
print(matriz_ejemplo)
print("\nEl elemento máximo de la matriz es:", maximo_encontrado)