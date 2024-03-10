
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos_en_conjunto(conjunto):
    primos = set()
    for numero in conjunto:
        if es_primo(numero):
            primos.add(numero)
    return primos

# Ejemplo de uso
conjunto_original = {1, 2, 31, 41, 5, 6, 71,}
conjunto_primos = numeros_primos_en_conjunto(conjunto_original)

print("Conjunto Original:", conjunto_original)
print("Conjunto de Números Primos:", conjunto_primos)