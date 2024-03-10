#8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila.

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

def evaluar_expresion_posfija(expresion):
    # Función para evaluar una expresión en notación posfija.
    pila = Pila()

    for token in expresion.split():
        # Itera sobre cada token en la expresión separada por espacios.
        if token.isdigit():
            # Si el token es un número, lo apila.
            pila.apilar(int(token))
        else:
            # El token es un operador
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()

            if operando1 is None or operando2 is None:
                return "Expresión incorrecta"
                # Si falta algún operando, la expresión es incorrecta.

            if token == '+':
                # Si el token es '+', suma los operandos y apila el resultado.
                pila.apilar(operando1 + operando2)
            elif token == '-':
                # Si el token es '-', resta los operandos y apila el resultado.
                pila.apilar(operando1 - operando2)
            elif token == '*':
                # Si el token es '*', multiplica los operandos y apila el resultado.
                pila.apilar(operando1 * operando2)
            elif token == '/':
                # Si el token es '/', verifica que el divisor no sea cero, luego divide los operandos y apila el resultado.
                if operando2 == 0:
                    return "División por cero"
                pila.apilar(operando1 / operando2)
            else:
                return "Operador no válido"
                # Si el token no es un operador válido, la expresión es incorrecta.

    resultado = pila.desapilar()

    if not pila.esta_vacia():
        return "Expresión incorrecta"
        # Si la pila no está vacía al final, la expresión es incorrecta.

    return resultado
    # Devuelve el resultado de la evaluación de la expresión.

expresion_posfija = "3 4 + 2 *"
# Expresión posfija a evaluar: 3 + 4 * 2
resultado_evaluacion = evaluar_expresion_posfija(expresion_posfija)
print("El resultado de la expresión posfija es:", resultado_evaluacion)
# Imprime el resultado de la evaluación de la expresión posfija.