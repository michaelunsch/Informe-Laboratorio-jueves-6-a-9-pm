#9. Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz hasta el nodo).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None  # Define la clase Nodo que representa un nodo en un árbol binario, con un valor y punteros a los nodos izquierdo y derecho.

class ArbolBinario:
    def __init__(self, raiz):
        self.raiz = raiz  # Define la clase ArbolBinario que representa un árbol binario con una raíz dada.

    def profundidad_nodo(self, nodo_busqueda, nodo_actual=None, profundidad=0):
        if nodo_actual is None:
            nodo_actual = self.raiz  # Si el nodo actual es None, se establece como la raíz.

        if nodo_actual is None:
            return -1  # Si no hay nodo actual, devuelve -1.

        if nodo_actual == nodo_busqueda:
            return profundidad  # Si el nodo actual es el buscado, devuelve la profundidad actual.

        # Verifica si el nodo izquierdo no es None antes de llamar a la función
        if nodo_actual.izquierda is not None:
            # Llama recursivamente a la función para buscar en el subárbol izquierdo.
            profundidad_izquierda = self.profundidad_nodo(nodo_busqueda, nodo_actual.izquierda, profundidad + 1)
            if profundidad_izquierda != -1:  # Si el nodo fue encontrado en el subárbol izquierdo.
                return profundidad_izquierda

        # Verifica si el nodo derecho no es None antes de llamar a la función
        if nodo_actual.derecha is not None:
            # Llama recursivamente a la función para buscar en el subárbol derecho.
            profundidad_derecha = self.profundidad_nodo(nodo_busqueda, nodo_actual.derecha, profundidad + 1)
            return profundidad_derecha

        return -1  # Si el nodo no se encuentra, devuelve -1.

# Creamos los nodos del árbol
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

# Configuramos las conexiones entre los nodos para formar un árbol
nodo1.izquierda = nodo2
nodo1.derecha = nodo3
nodo2.izquierda = nodo4
nodo2.derecha = nodo5
nodo3.derecha = nodo6

# Creamos el árbol con la raíz nodo1
arbol = ArbolBinario(nodo1)

# Calculamos la profundidad del nodo con valor 5
nodo_a_buscar = nodo5
profundidad_nodo = arbol.profundidad_nodo(nodo_a_buscar)
if profundidad_nodo != -1:
    print(f"La profundidad del nodo con valor {nodo_a_buscar.valor} es:", profundidad_nodo)
else:
    print(f"No se encontró el nodo con valor {nodo_a_buscar.valor} en el árbol.")

    print(f"No se encontró el nodo con valor {nodo_a_buscar.valor} en el árbol.")