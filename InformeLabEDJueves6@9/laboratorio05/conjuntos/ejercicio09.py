def filtrar_palabras_por_longitud(conjunto_palabras, longitud_deseada):
    """
    Filtra las palabras en el conjunto dado por la longitud especificada.

    Parameters:
    - conjunto_palabras: Conjunto de palabras a filtrar.
    - longitud_deseada: Longitud deseada de las palabras a incluir en el resultado.

    Returns:
    - Conjunto de palabras con la longitud especificada.
    """
    return {palabra for palabra in conjunto_palabras if len(palabra) == longitud_deseada}

# Ejemplo de uso:
conjunto_palabras_entrada = {"hola", "adios", "python", "gpt", "openai", "ejemplo"}
longitud_deseada = 5

resultado = filtrar_palabras_por_longitud(conjunto_palabras_entrada, longitud_deseada)
print(resultado)