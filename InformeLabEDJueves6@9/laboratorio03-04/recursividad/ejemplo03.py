def piramide(n, p=1):#definir dos parametros 'n' filas y p un parametro opcional
    if p <= n: #maximo valor de final de la piramide
        # Imprimir espacios para alinear la pirámide
        print(" " * (n - p), end="")

        # Imprimir números en la fila actual
        for i in range(1, p + 1):
            print(i, end=" ")

        print()  # Saltar a una nueva línea después de imprimir la fila

        # Llamar recursivamente para la siguiente fila
        piramide(n, p + 1)
piramide(5)