
texto = input("Ingrese una cadena de texto: ")

# Contar el número de vocales en la cadena
contador_vocales = sum(1 for char in texto if char.lower() in "aeiou")

# Mostrar el resultado
print(f"El número de vocales en la cadena es: {contador_vocales}")