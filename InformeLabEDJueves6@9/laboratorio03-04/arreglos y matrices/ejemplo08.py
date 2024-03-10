import numpy as np

# Matrices internas
matriz_interna_1 = np.array([[1, 2, 3], [4, 5, 6]])
matriz_interna_2 = np.array([[7, 8, 9], [10, 11, 12]])
matriz_interna_3 = np.array([[13, 14, 15], [16, 17, 18]])


# Crear una matriz de matrices
matriz_de_matrices = np.array([matriz_interna_1, matriz_interna_2, matriz_interna_3])
print(matriz_de_matrices)
# Accediendo a elementos de las matrices internas
print(matriz_de_matrices[0, 1, 2])  # Imprime el elemento en la primera fila, segunda matriz interna y tercera columna, que es 6