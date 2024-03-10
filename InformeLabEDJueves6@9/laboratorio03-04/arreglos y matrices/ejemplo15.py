import numpy as np

# Crear una matriz de ejemplo
matriz_ejemplo = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calcular la media de todos los elementos de la matriz
media_total = np.mean(matriz_ejemplo)

# Calcular la mediana de todos los elementos de la matriz
mediana_total = np.median(matriz_ejemplo)

# Calcular la desviación estándar de todos los elementos de la matriz
desviacion_estandar_total = np.std(matriz_ejemplo)

# Imprimir los resultados
print("Matriz:")
print(matriz_ejemplo)

print("\nMedia de todos los elementos de la matriz:", media_total)
print("Mediana de todos los elementos de la matriz:", mediana_total)
print("Desviación estándar de todos los elementos de la matriz:", desviacion_estandar_total)