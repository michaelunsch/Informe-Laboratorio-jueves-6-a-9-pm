#7. Implementar un programa que convierta un número decimal a su representación en sistema binario utilizando una pila.

class Pila:
    # Define la clase Pila para implementar una estructura de datos de pila.
    def __init__(self):
        # Constructor de la clase Pila que inicializa la pila como una lista vacía.
        self.items = []

    def esta_vacia(self):
        # Método para verificar si la pila está vacía.
        return len(self.items) == 0

    def apilar(self, item):
        # Método para agregar un elemento a la parte superior de la pila.
        self.items.append(item)

    def desapilar(self):
        # Método para eliminar y devolver el elemento en la parte superior de la pila.
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None
            # Devuelve None si la pila está vacía.

def decimal_a_binario(decimal):
    # Función para convertir un número decimal a binario.
    pila = Pila()

    # Caso especial si el número es 0
    if decimal == 0:
        return "0"

    # Mientras el decimal sea mayor que 0, dividir y apilar los restos
    while decimal > 0:
        resto = decimal % 2
        pila.apilar(resto)
        decimal = decimal // 2

    # Construir el número binario desapilando la pila
    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())

    return binario

# Solicitar al usuario un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
binario_resultante = decimal_a_binario(numero_decimal)

# Mostrar el resultado
print(f"El número binario equivalente a {numero_decimal} es: {binario_resultante}")