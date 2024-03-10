def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palindromos_en_conjunto(conjunto_palabras):
    palindromos = set()

    for palabra in conjunto_palabras:
        if es_palindromo(palabra):
            palindromos.add(palabra)

    return palindromos

# Ejemplo de uso
conjunto_palabras = {"ana", "ilo","oso"}
resultado = palindromos_en_conjunto(conjunto_palabras)

print("Conjunto de palíndromos:", resultado)
