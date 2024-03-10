import numpy as np

# Matriz de ejemplo
matriz_ejemplo = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Número por el cual multiplicar la matriz
numero = 2

# Multiplicar la matriz por el número
matriz_resultado = matriz_ejemplo * numero

# Imprimir la matriz original y la matriz resultante
print("Matriz Original:")
print(matriz_ejemplo)

print("\nMatriz Resultante (Multiplicada por {}):".format(numero))
print(matriz_resultado)