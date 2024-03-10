#2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato impar e imprime la lista hacia adelante y hacia atrás.

class Nodo:
# Se define la clase Nodo, que representa un nodo individual en una lista doblemente enlazada.
    def __init__(self, valor):
        self.valor = valor
        # Se asigna el valor al nodo.
        self.siguiente = None
        # Se establece la referencia al siguiente nodo como None.
        self.anterior = None
        # Se establece la referencia al nodo anterior como None.

class ListaEnlazada:
# Se define la clase ListaEnlazada para manejar la lista enlazada.
    def __init__(self):
        self.cabeza = None
        # Se inicializa la cabeza de la lista como None.
        self.cola = None
        # Se inicializa la cola de la lista como None.

    def agregar(self, valor):
        # Método para agregar un nuevo nodo al final de la lista.
        nuevo_nodo = Nodo(valor)
        # Se crea un nuevo nodo con el valor proporcionado.
        if not self.cabeza:
            # Si la lista está vacía:
            self.cabeza = nuevo_nodo
            # Se establece el nuevo nodo como la cabeza.
            self.cola = nuevo_nodo
            # También se establece como la cola.
        else:
            nuevo_nodo.anterior = self.cola
            # El nodo anterior del nuevo nodo apunta a la cola actual.
            self.cola.siguiente = nuevo_nodo
            # El siguiente nodo de la cola actual apunta al nuevo nodo.
            self.cola = nuevo_nodo
            # El nuevo nodo se convierte en la nueva cola.

    def imprimir_adelante(self):
        # Método para imprimir la lista desde la cabeza hasta la cola.
        actual = self.cabeza
        # Se comienza desde la cabeza.
        while actual:
            # Mientras haya nodos en la lista:
            print(actual.valor, end=" -> ")
            # Se imprime el valor del nodo.
            actual = actual.siguiente
            # Se pasa al siguiente nodo.
        print("None")

    def imprimir_atras(self):
        # Método para imprimir la lista desde la cola hasta la cabeza.
        actual = self.cola
        # Se comienza desde la cola.
        while actual:
            # Mientras haya nodos en la lista:
            print(actual.valor, end=" -> ")
            # Se imprime el valor del nodo.
            actual = actual.anterior
            # Se pasa al nodo anterior.
        print("None")

    def contar_pares_impares(self):
        # Método para contar nodos con valores pares e impares.
        contador_pares = 0
        contador_impares = 0
        actual = self.cabeza
        # Se inicia desde la cabeza.
        while actual:
            # Mientras haya nodos en la lista:
            if actual.valor % 2 == 0:
                # Si el valor del nodo es par:
                contador_pares += 1
                # Se incrementa el contador de pares.
            else:
                # Si el valor del nodo es impar:
                contador_impares += 1
                # Se incrementa el contador de impares.
            actual = actual.siguiente
            # Se avanza al siguiente nodo.
        return contador_pares, contador_impares
        # Se devuelve el conteo de pares e impares.

# Crear la lista y agregar nodos
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
lista.agregar(7)
lista.agregar(8)
lista.agregar(9)

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()

# Contar nodos con datos pares e impares
pares, impares = lista.contar_pares_impares()
print(f"Nodos con datos pares: {pares}")
print(f"Nodos con datos impares: {impares}")