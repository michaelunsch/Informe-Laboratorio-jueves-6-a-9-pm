def triangulo_invertido(n, p=1):
    if p <= n:
        # Imprimir espacios para alinear el triángulo
        print(" " * (p - 1), end="")

        # Imprimir puntos en la fila actual
        imprimir_puntos(2 * (n - p) + 1)

        print()  # Saltar a una nueva línea después de imprimir la fila

        # Llamar recursivamente para la siguiente fila
        triangulo_invertido(n, p + 1)

def imprimir_puntos(num):
    if num >= 1:
        print(".", end="")
        imprimir_puntos(num - 1)

# Llamada a la función para imprimir el triángulo nabla
triangulo_invertido(3)