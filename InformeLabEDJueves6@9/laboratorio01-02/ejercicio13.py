# Solicitar al usuario que ingrese un número para generar la tabla de multiplicar
try:
    numero = int(input("Ingrese un número para generar la tabla de multiplicar: "))

    # Mostrar la tabla de multiplicar
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print("Por favor, ingrese un número entero válido.")