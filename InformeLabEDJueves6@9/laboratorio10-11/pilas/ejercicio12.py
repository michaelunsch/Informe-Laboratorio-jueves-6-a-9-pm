#12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar expresiones.

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

    def ver_tope(self):
        # Método para ver el elemento en la parte superior de la pila sin eliminarlo.
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None
            # Devuelve None si la pila está vacía.

def calcular_expresion(expresion):
    # Función para calcular el resultado de una expresión en notación polaca inversa.
    pila = Pila()  # Crea una instancia de la clase Pila.
    tokens = expresion.split()  # Divide la expresión en una lista de tokens.

    for token in tokens:
        # Itera sobre cada token en la lista de tokens.
        if token.isdigit():
            # Si el token es un número, lo apila en la pila.
            pila.apilar(int(token))
        elif token in ['+', '-', '*', '/']:
            # Si el token es un operador, realiza la operación correspondiente.
            if pila.esta_vacia():
                return "Expresión incorrecta"  # La pila no tiene suficientes operandos.
            operando2 = pila.desapilar()
            if pila.esta_vacia():
                return "Expresión incorrecta"  # La pila no tiene suficientes operandos.
            operando1 = pila.desapilar()

            # Realiza la operación correspondiente según el operador.
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                if operando2 == 0:
                    return "División por cero"  # No se puede dividir por cero.
                resultado = operando1 / operando2

            pila.apilar(resultado)  # Apila el resultado de la operación.
        else:
            return "Token no válido"  # El token no es ni número ni operador.

    if pila.esta_vacia() or len(pila.items) > 1:
        return "Expresión incorrecta"  # La pila no tiene un solo resultado.
    else:
        return pila.desapilar()  # Devuelve el resultado final de la expresión.

expresion = "5 2 + 3 *"
# Expresión en notación polaca inversa (postfija): "5 2 + 3 *"
# Equivalente a la expresión infija: "(5 + 2) * 3"
resultado = calcular_expresion(expresion)
print(f"El resultado de la expresión '{expresion}' es: {resultado}")
# Imprime el resultado de la evaluación de la expresión.