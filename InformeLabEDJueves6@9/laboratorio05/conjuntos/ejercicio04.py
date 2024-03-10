def numeros_comunes(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

# Ejemplo de uso
conjunto_numeros1 = {10,30,50,60}
conjunto_numeros2 = {50,70,90}

conjunto_comun = numeros_comunes(conjunto_numeros1, conjunto_numeros2)

print("Conjunto 1:", conjunto_numeros1)
print("Conjunto 2:", conjunto_numeros2)
print("Números comunes:", conjunto_comun)