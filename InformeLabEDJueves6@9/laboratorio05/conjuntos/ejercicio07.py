def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def anagramas_en_conjunto(conjunto_palabras):
    anagramas = set() #se crea un conjunto vacio

    # Iterar sobre cada par de palabras en el conjunto
    for palabra1 in conjunto_palabras:
        for palabra2 in conjunto_palabras:
            # Verificar si son anagramas y no la misma palabra
            if palabra1 != palabra2 and son_anagramas(palabra1, palabra2):
                # Agregar al conjunto de anagramas
                anagramas.add(palabra1)
                anagramas.add(palabra2)

    return anagramas

# Ejemplo de uso
conjunto_original = {"saco", "amor", "cosa", "roma", "rosa", "flor"}
conjunto_anagramas = anagramas_en_conjunto(conjunto_original)

print("Conjunto original de palabras:", conjunto_original)
print("Conjunto de anagramas:", conjunto_anagramas)