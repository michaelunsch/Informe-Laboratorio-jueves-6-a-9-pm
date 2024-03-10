#13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo.

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

def es_palindromo(palabra):
    # Función para verificar si una palabra es un palíndromo.
    palabra = palabra.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    pila = Pila()  # Crear una instancia de la clase Pila.

    # Apilar los caracteres de la palabra en la pila
    for caracter in palabra:
        pila.apilar(caracter)

    # Comparar los caracteres apilados con los de la palabra original
    for caracter in palabra:
        if caracter != pila.desapilar():
            return False
            # Si los caracteres no coinciden, la palabra no es un palíndromo.

    return True
    # Si se termina de recorrer la palabra sin discrepancias, es un palíndromo.

palabra1 = "anita lava la tina"
palabra2 = "oso"
palabra3 = "python"

print(f"¿'{palabra1}' es un palíndromo?: {es_palindromo(palabra1)}")
print(f"¿'{palabra2}' es un palíndromo?: {es_palindromo(palabra2)}")
print(f"¿'{palabra3}' es un palíndromo?: {es_palindromo(palabra3)}")
# Imprime si las palabras son palíndromos o no.