import numpy as np

# Crear una matriz de números complejos
matriz_numeros_complejos = np.array([
    [1 + 2j, 2 - 1j, 3 + 4j],
    [4 + 3j, 5 - 2j, 6 + 1j],
    [7 - 1j, 8 + 2j, 9 - 3j]
])

# Accediendo a elementos de la matriz
print(matriz_numeros_complejos[0, 2])  # Imprime el elemento en la primera fila y tercera columna, que es 3 + 4j