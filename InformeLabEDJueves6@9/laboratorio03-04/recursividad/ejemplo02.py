
def imprimir_suma(n,suma=0):
    if n >= 1:
        suma += n
        imprimir_suma(n - 1, suma)
    else:
        print("La suma es:", suma)

# Llamada a la función para imprimir la suma de los números del 1 al n
imprimir_suma(10)