#10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.

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

def ordenar_pila_ascendente(pila):
    # Función para ordenar una pila en orden ascendente.
    pila_ordenada = Pila()
    # Crea una nueva pila para almacenar los elementos ordenados.

    while not pila.esta_vacia():
        # Mientras la pila original no esté vacía:
        elemento_actual = pila.desapilar()
        # Desapila un elemento de la pila original.

        while not pila_ordenada.esta_vacia() and pila_ordenada.ver_tope() > elemento_actual:
            # Mientras la pila ordenada no esté vacía y el elemento en la parte superior sea mayor que el elemento actual:
            pila.apilar(pila_ordenada.desapilar())
            # Desapila elementos de la pila ordenada y los apila en la pila original.

        pila_ordenada.apilar(elemento_actual)
        # Apila el elemento actual en la pila ordenada.

    return pila_ordenada
    # Devuelve la pila ordenada de manera ascendente.

pila = Pila()
pila.apilar(5)
pila.apilar(3)
pila.apilar(8)
pila.apilar(1)
pila.apilar(6)

pila_ordenada = ordenar_pila_ascendente(pila)

# Imprimir la pila ordenada
print("Pila ordenada de manera ascendente:")
while not pila_ordenada.esta_vacia():
    print(pila_ordenada.desapilar())
    # Desapila y muestra los elementos de la pila ordenada.