#11. Eliminar los elementos duplicados de una pila.

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

def eliminar_elementos_duplicados(pila):
    # Función para eliminar elementos duplicados de una pila.
    elementos_unicos = set()  # Conjunto para rastrear elementos únicos
    pila_temporal = Pila()    # Pila temporal para almacenar elementos únicos en orden

    while not pila.esta_vacia():
        # Mientras la pila original no esté vacía:
        elemento_actual = pila.desapilar()

        # Verificar si el elemento es único
        if elemento_actual not in elementos_unicos:
            elementos_unicos.add(elemento_actual)
            # Agrega el elemento a conjunto de elementos únicos
            pila_temporal.apilar(elemento_actual)
            # Apila el elemento único en la pila temporal

    # Reapilar los elementos únicos en la pila original
    while not pila_temporal.esta_vacia():
        # Mientras la pila temporal no esté vacía:
        pila.apilar(pila_temporal.desapilar())
        # Reapila los elementos únicos en la pila original

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(2)
pila.apilar(4)
pila.apilar(3)
pila.apilar(5)

print("Pila original:")
while not pila.esta_vacia():
    # Muestra la pila original
    print(pila.desapilar())

eliminar_elementos_duplicados(pila)

print("Pila sin elementos duplicados:")
while not pila.esta_vacia():
    # Muestra la pila sin elementos duplicados
    print(pila.desapilar())