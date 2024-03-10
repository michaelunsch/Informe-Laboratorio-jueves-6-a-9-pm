#1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista duplicada hacia adelante y hacia atrás.

class Nodo:
# Se define la clase Nodo, que representa un nodo individual en una lista doblemente enlazada.
    def __init__(self, valor):
        self.valor = valor
        # Se asigna el valor pasado como parámetro al atributo 'valor' del nodo.
        self.siguiente = None
        # Se inicializa el atributo 'siguiente' como None, que apunta al siguiente nodo en la lista.
        self.anterior = None
        # Se inicializa el atributo 'anterior' como None, que apunta al nodo anterior en la lista.

class ListaEnlazada:
# Se define la clase ListaEnlazada, que representa la lista enlazada en su conjunto.
    def __init__(self):
        self.cabeza = None
        # Se inicializa el atributo 'cabeza' como None, que apunta al primer nodo de la lista.
        self.cola = None
        # Se inicializa el atributo 'cola' como None, que apunta al último nodo de la lista.

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        # Se crea un nuevo nodo con el valor especificado.
        if not self.cabeza:
            # Si la lista está vacía:
            self.cabeza = nuevo_nodo
            # El nuevo nodo se convierte en la cabeza de la lista.
            self.cola = nuevo_nodo
            # El nuevo nodo también se convierte en la cola de la lista.
        else:
            # Si la lista no está vacía:
            nuevo_nodo.anterior = self.cola
            # Se establece el nodo anterior del nuevo nodo como el nodo actualmente en la cola.
            self.cola.siguiente = nuevo_nodo
            # Se establece el nodo siguiente del nodo actualmente en la cola como el nuevo nodo.
            self.cola = nuevo_nodo
            # El nuevo nodo ahora se convierte en la cola de la lista.

    def imprimir_adelante(self):
        actual = self.cabeza
        # Se inicializa un nodo 'actual' al principio de la lista.
        while actual:
            # Mientras 'actual' no sea None:
            print(actual.valor, end=" -> ")
            # Se imprime el valor del nodo actual seguido de una flecha.
            actual = actual.siguiente
            # 'actual' se mueve al siguiente nodo en la lista.
        print("None")
        # Una vez que se alcanza el final de la lista, se imprime 'None' para indicar el final de la lista.

    def imprimir_atras(self):
        actual = self.cola
        # Se inicializa un nodo 'actual' al final de la lista.
        while actual:
            # Mientras 'actual' no sea None:
            print(actual.valor, end=" -> ")
            # Se imprime el valor del nodo actual seguido de una flecha.
            actual = actual.anterior
            # 'actual' se mueve al nodo anterior en la lista.
        print("None")
        # Una vez que se alcanza el principio de la lista, se imprime 'None' para indicar el inicio de la lista.

def duplicar_nodos(lista):
    actual = lista.cabeza
    # Se inicializa un nodo 'actual' al principio de la lista.
    while actual:
        # Mientras 'actual' no sea None:
        nuevo_nodo = Nodo(actual.valor)
        # Se crea un nuevo nodo con el mismo valor que el nodo actual.
        nuevo_nodo.anterior = actual
        # Se establece el nodo anterior del nuevo nodo como el nodo actual.
        nuevo_nodo.siguiente = actual.siguiente
        # Se establece el nodo siguiente del nuevo nodo como el nodo siguiente del nodo actual.

        if actual.siguiente:
            # Si hay un nodo siguiente al nodo actual:
            actual.siguiente.anterior = nuevo_nodo
            # Se establece el nodo anterior del nodo siguiente como el nuevo nodo.
        else:
            # Si no hay un nodo siguiente al nodo actual (es el último nodo en la lista):
            lista.cola = nuevo_nodo
            # El nuevo nodo se convierte en la cola de la lista.

        actual.siguiente = nuevo_nodo
        # Se establece el nodo siguiente del nodo actual como el nuevo nodo.
        actual = nuevo_nodo.siguiente
        # Se mueve al siguiente nodo en la lista para continuar el proceso de duplicación.

# Crear la lista
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

# Duplicar los nodos
duplicar_nodos(lista)

# Imprimir la lista original hacia adelante y hacia atrás
print("Lista original hacia adelante:")
lista.imprimir_adelante()
print("Lista original hacia atrás:")
lista.imprimir_atras()

# Imprimir la lista duplicada hacia adelante y hacia atrás
print("Lista duplicada hacia adelante:")
lista.imprimir_adelante()
print("Lista duplicada hacia atrás:")
lista.imprimir_atras()