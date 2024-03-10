def palabras_con_letra(conjunto_palabras, letra):
    palabras_seleccionadas = {palabra for palabra in sorted(conjunto_palabras, reverse=True) if letra in palabra}
    return palabras_seleccionadas

# Ejemplo de uso:
conjunto_palabras = {"manzana", "pera", "uva", "kiwi", "melon", "coco"}
letra_seleccionada = "a"
palabras_seleccionadas = palabras_con_letra(conjunto_palabras, letra_seleccionada)
print(f"Palabras con la letra '{letra_seleccionada}':", palabras_seleccionadas)