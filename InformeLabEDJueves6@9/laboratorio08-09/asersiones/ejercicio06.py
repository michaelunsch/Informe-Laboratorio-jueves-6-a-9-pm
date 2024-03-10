ejecutar = True

while ejecutar:
    # Código que se ejecuta en cada iteración del ciclo

    # Lógica para decidir si se debe salir del ciclo
    respuesta = input("¿Deseas continuar? (s/n): ")
    if respuesta.lower() == "n":
        ejecutar = False

# Código que se ejecuta después de salir del ciclo
print("Fin del programa.")