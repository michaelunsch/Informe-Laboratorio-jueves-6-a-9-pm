def palabras_con_letra(conjunto_palabras, letra_inicial):
    return {palabra for palabra in conjunto_palabras if palabra.startswith(letra_inicial)}

# Ejemplo de uso
conjunto_palabras_original = {"messi", "neymar", "ronaldo", "maradona", "zico", "pirlo",}
letra_inicial_deseada = "m"
#llamada a la funcion
conjunto_palabras_filtrado = palabras_con_letra(conjunto_palabras_original, letra_inicial_deseada)

print("Conjunto original de palabras:", conjunto_palabras_original)
print(f"Palabras que comienzan con '{letra_inicial_deseada}':", conjunto_palabras_filtrado)