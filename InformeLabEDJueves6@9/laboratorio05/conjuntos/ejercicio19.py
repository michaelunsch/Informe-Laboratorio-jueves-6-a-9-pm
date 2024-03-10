def numeros_ordenados_no_duplicados(conjunto_numeros):
    numeros_ordenados = sorted(set(conjunto_numeros))
    return numeros_ordenados

# Ejemplo de uso:
conjunto_numeros = {3, 1, 5, 2, 4, 2, 6, 4}
numeros_ordenados_sin_duplicados = numeros_ordenados_no_duplicados(conjunto_numeros)
print("Números ordenados sin duplicados:", numeros_ordenados_sin_duplicados)