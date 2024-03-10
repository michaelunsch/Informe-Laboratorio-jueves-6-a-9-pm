#1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para comparar los caracteres de la palabra en orden original y reverso.

class Cola:
    # Define la clase Cola para representar una cola de elementos.
    def __init__(self):
        # Constructor de la clase Cola que inicializa una lista vacía para almacenar los elementos.
        self.items = []

    def esta_vacia(self):
        # Método para verificar si la cola está vacía.
        return len(self.items) == 0

    def encolar(self, item):
        # Método para agregar un elemento al final de la cola.
        self.items.append(item)

    def desencolar(self):
        # Método para eliminar y devolver el primer elemento de la cola.
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

def es_palindromo(palabra):
    # Función para verificar si una palabra es un palíndromo.
    cola = Cola()
    palabra = palabra.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios

    # Encolar los caracteres de la palabra en orden original
    for caracter in palabra:
        cola.encolar(caracter)

    # Comparar los caracteres de la palabra en orden original y reverso
    while not cola.esta_vacia():
        if cola.desencolar() != palabra[-1]:
            return False
        palabra = palabra[:-1]

    return True

print(es_palindromo("anita lava la tina"))  # True
print(es_palindromo("oso"))                 # True
print(es_palindromo("python"))              # False