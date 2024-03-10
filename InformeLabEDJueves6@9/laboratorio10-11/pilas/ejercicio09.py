#9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una pila.

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

def verificar_operadores(expresion):
    # Función para verificar si los paréntesis, corchetes y llaves en la expresión están correctamente anidados.
    pila = Pila()
    # Crea una pila para rastrear los operadores abiertos.

    pares = {')': '(', ']': '[', '}': '{'}
    # Diccionario que mapea los operadores de cierre a sus correspondientes operadores de apertura.

    for caracter in expresion:
        # Itera sobre cada caracter en la expresión.
        if caracter in '([{':
            # Si el caracter es un operador de apertura, lo apila.
            pila.apilar(caracter)
        elif caracter in ')]}':
            # Si el caracter es un operador de cierre:
            if pila.esta_vacia():
                # Si la pila está vacía, la expresión está mal anidada.
                return False
            elif pila.desapilar() != pares[caracter]:
                # Si el operador de apertura correspondiente no está en la parte superior de la pila, la expresión está mal anidada.
                return False

    return pila.esta_vacia()
    # Devuelve True si la pila está vacía al final, lo que indica que todos los operadores están correctamente anidados.

expresion1 = "((2 + 3) * [5 - 4])"
expresion2 = "[(2 + 3) * {5 - 4}]"
expresion3 = "((2 + 3) * [5 - 4})"
expresion4 = "((2 + 3) * {5 - 4]"
expresion5 = "((2 + 3) * 5 - 4)"

print("La expresión", expresion1, "está correctamente anidada:", verificar_operadores(expresion1))
print("La expresión", expresion2, "está correctamente anidada:", verificar_operadores(expresion2))
print("La expresión", expresion3, "está correctamente anidada:", verificar_operadores(expresion3))
print("La expresión", expresion4, "está correctamente anidada:", verificar_operadores(expresion4))
print("La expresión", expresion5, "está correctamente anidada:", verificar_operadores(expresion5))
# Imprime el resultado de la verificación de cada expresión.