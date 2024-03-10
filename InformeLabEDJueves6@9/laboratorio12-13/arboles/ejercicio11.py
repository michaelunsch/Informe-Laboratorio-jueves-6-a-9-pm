#11. Implementar una función que encuentre el nodo con el valor máximo en el árbol.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None  # Define la clase Nodo que representa un nodo en un árbol binario, con un valor y punteros a los nodos izquierdo y derecho.

class ArbolBinario:
    def __init__(self, raiz):
        self.raiz = raiz  # Define la clase ArbolBinario que representa un árbol binario con una raíz dada.

    def encontrar_valor_maximo(self, nodo=None):
        if nodo is None:
            nodo = self.raiz  # Si el nodo dado es None, se establece como la raíz.

        if nodo is None:
            return None  # Si no hay nodo, devuelve None.

        # Itera hacia la derecha hasta encontrar el nodo más grande.
        while nodo.derecha is not None:
            nodo = nodo.derecha

        return nodo.valor  # Devuelve el valor del nodo más grande.

# Creamos los nodos del árbol
nodo1 = Nodo(5)
nodo2 = Nodo(3)
nodo3 = Nodo(7)
nodo4 = Nodo(2)
nodo5 = Nodo(4)
nodo6 = Nodo(6)
nodo7 = Nodo(8)

# Configuramos las conexiones entre los nodos para formar un árbol
nodo1.izquierda = nodo2
nodo1.derecha = nodo3
nodo2.izquierda = nodo4
nodo2.derecha = nodo5
nodo3.izquierda = nodo6
nodo3.derecha = nodo7

# Creamos el árbol con la raíz nodo1
arbol = ArbolBinario(nodo1)

# Encontramos el valor máximo en el árbol
valor_maximo = arbol.encontrar_valor_maximo()
print("El valor máximo en el árbol es:", valor_maximo)  # Imprime el valor máximo encontrado en el árbol.