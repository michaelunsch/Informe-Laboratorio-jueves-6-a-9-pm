#4. Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.

class Nodo:
    # Define la clase Nodo para los nodos individuales de la lista enlazada.
    def __init__(self, valor):
        # Constructor de la clase Nodo que inicializa el nodo con un valor.
        self.valor = valor
        # Establece el valor del nodo.
        self.siguiente = None
        # Inicializa el puntero al siguiente nodo como None.
        self.anterior = None
        # Inicializa el puntero al nodo anterior como None.

class ListaEnlazada:
    # Define la clase ListaEnlazada para la lista enlazada en su conjunto.
    def __init__(self):
        # Constructor de la clase ListaEnlazada que inicializa la cabeza y la cola de la lista como None.
        self.cabeza = None
        # Inicializa el puntero a la cabeza de la lista como None.
        self.cola = None
        # Inicializa el puntero a la cola de la lista como None.

    def agregar(self, valor):
        # Método para agregar un nuevo nodo al final de la lista enlazada.
        nuevo_nodo = Nodo(valor)
        # Crea un nuevo nodo con el valor proporcionado.
        if not self.cabeza:
            # Si la lista está vacía:
            self.cabeza = nuevo_nodo
            # Establece el nuevo nodo como la cabeza.
            self.cola = nuevo_nodo
            # Establece el nuevo nodo como la cola.
        else:
            # Si la lista no está vacía:
            nuevo_nodo.anterior = self.cola
            # Establece el nodo anterior del nuevo nodo como la cola actual.
            self.cola.siguiente = nuevo_nodo
            # Establece el siguiente nodo de la cola actual como el nuevo nodo.
            self.cola = nuevo_nodo
            # Actualiza la cola para que apunte al nuevo nodo.

    def eliminar_duplicados(self):
        # Método para eliminar nodos duplicados de la lista enlazada.
        valores_vistos = set()
        # Inicializa un conjunto para almacenar los valores vistos.
        actual = self.cabeza
        # Inicializa un puntero para recorrer la lista desde la cabeza.
        while actual:
            # Itera sobre los nodos de la lista.
            if actual.valor in valores_vistos:
                # Si el valor del nodo actual ya ha sido visto:
                siguiente_nodo = actual.siguiente
                # Guarda una referencia al siguiente nodo.
                self.eliminar_nodo(actual)
                # Elimina el nodo actual.
                actual = siguiente_nodo
                # Avanza al siguiente nodo.
            else:
                # Si el valor del nodo actual no ha sido visto:
                valores_vistos.add(actual.valor)
                # Agrega el valor del nodo actual al conjunto de valores vistos.
                actual = actual.siguiente
                # Avanza al siguiente nodo.

    def eliminar_nodo(self, nodo):
        # Método para eliminar un nodo específico de la lista enlazada.
        if nodo.anterior:
            # Si el nodo tiene un nodo anterior:
            nodo.anterior.siguiente = nodo.siguiente
            # El siguiente del nodo anterior apunta al siguiente del nodo actual.
        else:
            # Si el nodo es la cabeza de la lista:
            self.cabeza = nodo.siguiente
            # Actualiza la cabeza de la lista al siguiente nodo.
        if nodo.siguiente:
            # Si el nodo tiene un nodo siguiente:
            nodo.siguiente.anterior = nodo.anterior
            # El anterior del nodo siguiente apunta al anterior del nodo actual.
        else:
            # Si el nodo es la cola de la lista:
            self.cola = nodo.anterior
            # Actualiza la cola de la lista al nodo anterior.

    def imprimir_adelante(self):
        # Método para imprimir los valores de los nodos de la lista desde la cabeza hasta la cola.
        actual = self.cabeza
        # Inicializa un puntero para recorrer la lista desde la cabeza.
        while actual:
            # Itera sobre los nodos de la lista.
            print(actual.valor, end=" -> ")
            # Imprime el valor del nodo actual.
            actual = actual.siguiente
            # Avanza al siguiente nodo.
        print("None")

    def imprimir_atras(self):
        # Método para imprimir los valores de los nodos de la lista desde la cola hasta la cabeza.
        actual = self.cola
        # Inicializa un puntero para recorrer la lista desde la cola.
        while actual:
            # Itera sobre los nodos de la lista.
            print(actual.valor, end=" -> ")
            # Imprime el valor del nodo actual.
            actual = actual.anterior
            # Retrocede al nodo anterior.
        print("None")

# Crear la lista con datos duplicados
lista = ListaEnlazada()
# Crea una instancia de la lista enlazada.
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(2)
lista.agregar(4)
lista.agregar(3)
lista.agregar(5)
lista.agregar(1)
# Agrega valores a la lista enlazada.

# Eliminar nodos duplicados
lista.eliminar_duplicados()
# Elimina los nodos duplicados de la lista.

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_adelante()
# Imprime la lista desde la cabeza hasta la cola.
print("Lista hacia atrás:")
lista.imprimir_atras()
# Imprime la lista desde la cola hasta la cabeza.