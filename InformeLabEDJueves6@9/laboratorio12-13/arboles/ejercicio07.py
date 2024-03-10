#7. Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo).

class Nodo:
    def __init__(self, valor):
        # Inicialización de un nodo con un valor dado.
        self.valor = valor
        # Inicialización de los punteros a los nodos hijos izquierdo y derecho.
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz):
        # Inicialización de un árbol binario con la raíz dada.
        self.raiz = raiz

    def contar_nodos_internos(self, nodo):
        # Método para contar el número de nodos internos en el subárbol a partir del nodo dado.
        if nodo is None:
            # Si el nodo es nulo, devuelve 0.
            return 0
        elif nodo.izquierda is not None or nodo.derecha is not None:
            # Si el nodo tiene al menos un hijo, es un nodo interno.
            # Se cuenta el nodo actual y se busca recursivamente en los subárboles izquierdo y derecho.
            return 1 + self.contar_nodos_internos(nodo.izquierda) + self.contar_nodos_internos(nodo.derecha)
        else:
            # Si el nodo no tiene hijos, no es un nodo interno, devuelve 0.
            return 0

    def cantidad_nodos_internos(self):
        # Método para obtener la cantidad de nodos internos en el árbol.
        return self.contar_nodos_internos(self.raiz)


# Ejemplo de uso
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

# Contamos la cantidad de nodos internos en el árbol
cantidad_nodos_internos = arbol.cantidad_nodos_internos()
print("La cantidad de nodos internos en el árbol es:", cantidad_nodos_internos)