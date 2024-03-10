#5. Implementar una función que cuente la cantidad de nodos en el árbol.

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

    def contar_nodos(self, nodo):
        # Método para contar el número de nodos en el árbol a partir del nodo dado.
        if nodo is None:
            # Si el nodo es nulo, devuelve 0.
            return 0
        else:
            # Si el nodo no es nulo, cuenta recursivamente los nodos en los subárboles izquierdo y derecho,
            # y agrega 1 para el nodo actual.
            return 1 + self.contar_nodos(nodo.izquierda) + self.contar_nodos(nodo.derecha)

    def cantidad_total_nodos(self):
        # Método para obtener la cantidad total de nodos en el árbol.
        return self.contar_nodos(self.raiz)


# Creamos los nodos del árbol
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

# Configuramos las conexiones entre los nodos para formar un árbol
nodo1.izquierda = nodo2
nodo1.derecha = nodo3
nodo2.izquierda = nodo4
nodo2.derecha = nodo5

# Creamos el árbol con la raíz nodo1
arbol = ArbolBinario(nodo1)

# Contamos la cantidad de nodos en el árbol
cantidad_nodos = arbol.cantidad_total_nodos()
print("La cantidad de nodos en el árbol es:", cantidad_nodos)