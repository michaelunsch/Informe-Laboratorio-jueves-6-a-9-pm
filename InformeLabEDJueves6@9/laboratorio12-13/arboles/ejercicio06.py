#6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).

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

    def contar_nodos_hoja(self, nodo):
        # Método para contar el número de nodos hoja en el subárbol a partir del nodo dado.
        if nodo is None:
            # Si el nodo es nulo, devuelve 0.
            return 0
        elif nodo.izquierda is None and nodo.derecha is None:
            # Si el nodo no tiene hijos, es un nodo hoja.
            return 1
        else:
            # Si el nodo tiene hijos, se cuenta recursivamente los nodos hoja en los subárboles izquierdo y derecho.
            return self.contar_nodos_hoja(nodo.izquierda) + self.contar_nodos_hoja(nodo.derecha)

    def cantidad_nodos_hoja(self):
        # Método para obtener la cantidad de nodos hoja en el árbol.
        return self.contar_nodos_hoja(self.raiz)


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

# Contamos la cantidad de nodos hoja en el árbol
cantidad_nodos_hoja = arbol.cantidad_nodos_hoja()
print("La cantidad de nodos hoja en el árbol es:", cantidad_nodos_hoja)