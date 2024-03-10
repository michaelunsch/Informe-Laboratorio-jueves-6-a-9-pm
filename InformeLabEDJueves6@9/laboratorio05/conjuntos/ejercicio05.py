def diferencia_entre_conjuntos(conjunto1, conjunto2):
    return conjunto1 - conjunto2

# Ejemplo de uso
conjunto_numeros1 = {100, 200, 300, 400,}
conjunto_numeros2 = {300, 400,900,700}

diferencia = diferencia_entre_conjuntos(conjunto_numeros1, conjunto_numeros2)

print("Conjunto 1:", conjunto_numeros1)
print("Conjunto 2:", conjunto_numeros2)
print("Diferencia:", diferencia)