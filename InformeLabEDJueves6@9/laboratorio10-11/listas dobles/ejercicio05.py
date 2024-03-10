#5. Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el primero y viceversa) e imprime la lista hacia adelante y hacia atrás.

class Nodo:
    # Define la clase Nodo para los nodos individuales de la lista enlazada.
    def __init__(self, valor):
        # Constructor de la clase Nodo que inicializa el nodo con un valor.
        self.valor = valor
        # Establece el valor del nodo.
        self.siguiente = None
        # Inicializa el puntero al siguiente nodo como None.

class ListaEnlazada:
    # Define la clase ListaEnlazada para la lista enlazada en su conjunto.
    def __init__(self):
        # Constructor de la clase ListaEnlazada que inicializa la cabeza de la lista como None.
        self.cabeza = None

    def agregar(self, valor):
        # Método para agregar un nuevo nodo al final de la lista.
        nuevo_nodo = Nodo(valor)
        # Crea un nuevo nodo con el valor proporcionado.
        if not self.cabeza:
            # Si la lista está vacía:
            self.cabeza = nuevo_nodo
            # Establece el nuevo nodo como la cabeza.
        else:
            # Si la lista no está vacía:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            # Avanza hasta el último nodo y enlaza el nuevo nodo.

    def imprimir_adelante(self):
        # Método para imprimir los valores de los nodos de la lista desde la cabeza hasta el final.
        actual = self.cabeza
        # Inicializa un puntero para recorrer la lista, comenzando desde la cabeza.
        while actual:
            # Itera sobre la lista mientras haya nodos.
            print(actual.valor, end=" -> ")
            # Imprime el valor del nodo actual seguido de una flecha "->".
            actual = actual.siguiente
            # Mueve el puntero al siguiente nodo en la lista.
        print("None")
        # Imprime "None" al final para indicar el final de la lista.

    def invertir_lista(self):
        # Método para invertir la lista enlazada.
        anterior = None
        # Inicializa un puntero para el nodo anterior, comenzando desde None.
        actual = self.cabeza
        # Inicializa un puntero para el nodo actual, comenzando desde la cabeza.
        while actual:
            # Itera sobre la lista mientras haya nodos.
            siguiente_temp = actual.siguiente
            # Almacena el siguiente nodo temporalmente.
            actual.siguiente = anterior
            # Invierte el enlace del nodo actual para que apunte al nodo anterior.
            anterior = actual
            # Mueve el puntero del nodo anterior al nodo actual.
            actual = siguiente_temp
            # Mueve el puntero del nodo actual al siguiente nodo.
        self.cabeza = anterior
        # Actualiza la cabeza de la lista para que apunte al último nodo (anterior).

# Crear la lista con al menos 6 nodos
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)

# Imprimir la lista original hacia adelante y hacia atrás
print("Lista original hacia adelante:")
lista.imprimir_adelante()

# Invertir la lista
lista.invertir_lista()

# Imprimir la lista invertida hacia adelante y hacia atrás
print("Lista invertida hacia adelante:")
lista.imprimir_adelante()