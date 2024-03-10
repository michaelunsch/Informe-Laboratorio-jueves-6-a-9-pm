import numpy as np

# Crear una matriz de ejemplo
matriz_ejemplo = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calcular la media de todos los elementos de la matriz
media_total = np.mean(matriz_ejemplo)

# Imprimir la matriz y la media
print("Matriz:")
print(matriz_ejemplo)

print("\nMedia de todos los elementos de la matriz:", media_total)


# Calcular la media a lo largo de las filas
media_por_filas = np.mean(matriz_ejemplo, axis=1)
print("\nMedia por filas:", media_por_filas)

# Calcular la media a lo largo de las columnas
media_por_columnas = np.mean(matriz_ejemplo, axis=0)
print("Media por columnas:", media_por_columnas)