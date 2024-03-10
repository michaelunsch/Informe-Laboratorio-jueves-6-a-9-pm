#3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la lista hacia adelante y hacia atrás.

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
        # Método para agregar un nuevo nodo al final de la lista.
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

    def insertar_en_posicion(self, valor, posicion):
        # Método para insertar un nuevo nodo en una posición específica de la lista.
        nuevo_nodo = Nodo(valor)
        # Crea un nuevo nodo con el valor proporcionado.
        if posicion == 0:
            # Si la posición es 0, se inserta en la cabeza de la lista.
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            # Actualiza la cabeza de la lista.
        else:
            actual = self.cabeza
            contador = 0
            # Inicializa un contador y un puntero para recorrer la lista desde la cabeza.
            while actual:
                # Itera sobre los nodos de la lista.
                if contador == posicion - 1:
                    # Cuando se alcanza la posición anterior a la que se va a insertar el nuevo nodo:
                    nuevo_nodo.siguiente = actual.siguiente
                    # El nuevo nodo apunta al siguiente nodo del actual.
                    if actual.siguiente:
                        actual.siguiente.anterior = nuevo_nodo
                    else:
                        self.cola = nuevo_nodo
                    # Actualiza la cola de la lista si es necesario.
                    actual.siguiente = nuevo_nodo
                    nuevo_nodo.anterior = actual
                    # Establece los enlaces del nuevo nodo.
                    break
                contador += 1
                actual = actual.siguiente
                # Avanza al siguiente nodo.

    def imprimir_adelante(self):
        # Método para imprimir los valores de los nodos de la lista desde la cabeza hasta la cola.
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self):
        # Método para imprimir los valores de los nodos de la lista desde la cola hasta la cabeza.
        actual = self.cola
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.anterior
        print("None")

# Crear la lista
lista = ListaEnlazada()
# Crea una instancia de la lista enlazada.
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
# Agrega valores a la lista enlazada.

# Insertar un nuevo nodo en la posición 3 con el dato 15
lista.insertar_en_posicion(15, 2)
# Inserta un nuevo nodo con el valor 15 en la posición 2 (considerando la indexación desde 0).

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()
# Imprime la lista enlazada en ambas direcciones.