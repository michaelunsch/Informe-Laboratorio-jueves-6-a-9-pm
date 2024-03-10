def numeros_divisibles(conjunto_numeros, divisor):
    return {numero for numero in conjunto_numeros if numero % divisor == 0}

# Ejemplo de uso
conjunto_numeros_original = {56,25,70,66,99}
divisor_deseado = 5
conjunto_numeros_divisibles = numeros_divisibles(conjunto_numeros_original, divisor_deseado)

print("Conjunto original de números:", conjunto_numeros_original)
print(f"Números divisibles por {divisor_deseado}:", conjunto_numeros_divisibles)