def palabras_con_letra(conjunto_palabras, letra):
    palabras_con_la_letra = set()

    for palabra in conjunto_palabras:
        if letra in palabra:
            palabras_con_la_letra.add(palabra)

    return palabras_con_la_letra

# Ejemplo de uso:
conjunto_palabras = {"gato", "perro", "elefante", "jirafa", "leon"}
letra_deseada = "o"

resultado = palabras_con_letra(conjunto_palabras, letra_deseada)
print("Palabras que contienen la letra '{}': {}".format(letra_deseada, resultado))