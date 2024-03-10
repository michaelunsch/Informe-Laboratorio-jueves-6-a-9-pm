#2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado actual de la cola.

    def procesar_pedido(self):
        # Método para procesar el primer pedido de la cola.
        if self.pedidos:
            # Verifica si hay pedidos en la cola.
            pedido_procesado = self.pedidos.pop(0)
            # Elimina y recupera el primer pedido de la cola utilizando el método pop(0).
            print(f"Pedido '{pedido_procesado}' procesado.")
            # Imprime un mensaje indicando que el pedido ha sido procesado.
        else:
            # Si no hay pedidos en la cola:
            print("No hay pedidos para procesar.")
            # Imprime un mensaje indicando que no hay pedidos para procesar.

    def mostrar_estado(self):
        # Método para mostrar el estado actual de la cola de pedidos.
        if self.pedidos:
            # Verifica si hay pedidos en la cola.
            print("Estado actual de la cola de pedidos:")
            # Imprime un mensaje indicando que se mostrará el estado de la cola.
            for pedido in self.pedidos:
                # Itera sobre cada pedido en la cola de pedidos.
                print(pedido)
                # Imprime cada pedido en una nueva línea.
        else:
            # Si no hay pedidos en la cola:
            print("La cola de pedidos está vacía.")
            # Imprime un mensaje indicando que la cola de pedidos está vacía.

        # Crear una instancia de ColaPedidos
        cola_pedidos = ColaPedidos()

        # Agregar pedidos a la cola
        cola_pedidos.agregar_pedido("Pizza")
        cola_pedidos.agregar_pedido("Hamburguesa")
        cola_pedidos.agregar_pedido("Sushi")

        # Mostrar el estado actual de la cola de pedidos
        cola_pedidos.mostrar_estado()

        # Procesar dos pedidos de la cola
        cola_pedidos.procesar_pedido()
        cola_pedidos.procesar_pedido()

        # Mostrar el estado actual de la cola después de procesar pedidos
        cola_pedidos.mostrar_estado()