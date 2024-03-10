def numeros_ordenados(conjunto_numeros):
    # Convertimos el conjunto a una lista y la ordenamos
    lista_ordenada = sorted(list(conjunto_numeros))

    # Convertimos la lista ordenada de nuevo a un conjunto
    conjunto_ordenado = set(lista_ordenada)

    return conjunto_ordenado

# Ejemplo de uso:
conjunto_numeros = {5, 2, 8, 1, 3}
conjunto_ordenado = numeros_ordenados(conjunto_numeros)
print("Conjunto de números ordenados:", conjunto_ordenado)