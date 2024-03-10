def funcion_ejemplo():
    # Código de la función
    return 10

# Llamada a la función y verificación del valor de retorno
resultado = funcion_ejemplo()
valor_esperado = 10

assert resultado == valor_esperado, f"El valor de retorno {resultado} no es el esperado"

# Código que se ejecuta después de la verificación
print("La función retornó el valor esperado.")