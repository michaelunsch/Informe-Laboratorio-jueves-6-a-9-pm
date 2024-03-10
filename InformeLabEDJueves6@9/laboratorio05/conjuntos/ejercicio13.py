def numeros_duplicados(conjunto_numeros):
    numeros_vistos = set()
    duplicados = set()

    for numero in conjunto_numeros:
        if numero in numeros_vistos:
            duplicados.add(numero)
        else:
            numeros_vistos.add(numero)

    return duplicados

# Ejemplo de uso:
conjunto_numeros = {1, 2, 3, 2, 4, 5, 6, 4}
duplicados = numeros_duplicados(conjunto_numeros)
print("Números duplicados:", duplicados)