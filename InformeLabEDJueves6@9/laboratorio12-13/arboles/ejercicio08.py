#8. Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz hasta una hoja).

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

    def altura_arbol(self, nodo):
        # Método para calcular la altura de un subárbol a partir de un nodo dado.
        if nodo is None:
            # Si el nodo es nulo, devuelve 0.
            return 0
        else:
            # Calcula la altura de los subárboles izquierdo y derecho.
            altura_izquierda = self.altura_arbol(nodo.izquierda)
            altura_derecha = self.altura_arbol(nodo.derecha)

            # La altura del árbol es la altura máxima entre la altura de los subárboles izquierdo y derecho, más uno (para contar la raíz).
            return max(altura_izquierda, altura_derecha) + 1

    def altura_total(self):
        # Método para obtener la altura total del árbol.
        return self.altura_arbol(self.raiz)


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

# Calculamos la altura del árbol
altura_arbol = arbol.altura_total()
print("La altura del árbol es:", altura_arbol)