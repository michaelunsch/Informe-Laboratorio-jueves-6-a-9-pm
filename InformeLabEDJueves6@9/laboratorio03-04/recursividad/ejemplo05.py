def multiplicar(n, multiplicador=0):
    if multiplicador <= 12:
        resultado = n * multiplicador
        print(f"{n} x {multiplicador} = {resultado}")
        multiplicar(n, multiplicador + 1)

# Llamada a la función para imprimir la tabla de multiplicar del 5
multiplicar(8)