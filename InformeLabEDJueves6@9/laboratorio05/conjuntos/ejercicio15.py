def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_ordenados(conjunto_numeros):
    primos_ordenados = {numero for numero in sorted(conjunto_numeros) if es_primo(numero)}
    return primos_ordenados

# Ejemplo de uso:
conjunto_numeros = {5, 2, 8, 1, 3, 7, 11, 4}
primos_ordenados = numeros_primos_ordenados(conjunto_numeros)
print("Números primos ordenados:", primos_ordenados)