#6. Utilizar una pila para invertir el orden de los caracteres de una cadena.

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

def invertir_cadena_con_pila(cadena):
    # Función para invertir una cadena utilizando una pila.
    pila = Pila()
    # Crea una instancia de la clase Pila.
    # Apilar cada carácter en la pila
    for caracter in cadena:
        # Itera sobre cada carácter en la cadena.
        pila.apilar(caracter)
        # Apila cada carácter en la pila.

    # Construir la cadena invertida desapilando la pila
    cadena_invertida = ""
    # Inicializa una cadena vacía para almacenar la cadena invertida.
    while not pila.esta_vacia():
        # Itera hasta que la pila esté vacía.
        cadena_invertida += pila.desapilar()
        # Desapila cada carácter y los concatena en la cadena invertida.

    return cadena_invertida
    # Devuelve la cadena invertida.

cadena_original = "Hola Mundo!"
# Define una cadena de ejemplo.
cadena_invertida = invertir_cadena_con_pila(cadena_original)
# Invierte la cadena utilizando la función invertir_cadena_con_pila.
print("Cadena original:", cadena_original)
# Imprime la cadena original.
print("Cadena invertida:", cadena_invertida)
# Imprime la cadena invertida.