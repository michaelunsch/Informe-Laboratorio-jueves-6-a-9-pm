# Inicializar los primeros dos términos de la serie
fibonacci = [0, 1]

# Generar la serie de Fibonacci
while len(fibonacci) < 10:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)

# Mostrar los primeros 10 números de la serie de Fibonacci
print(f"Primeros 10 números de la serie de Fibonacci: {fibonacci}")