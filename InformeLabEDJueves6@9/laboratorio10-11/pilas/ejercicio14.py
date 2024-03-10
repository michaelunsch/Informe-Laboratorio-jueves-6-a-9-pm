#14. Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los deshaceres.

class SistemaDeshacer:
    # Define la clase SistemaDeshacer para administrar acciones y su deshacer/rehacer.
    def __init__(self):
        # Constructor de la clase SistemaDeshacer que inicializa las pilas de acciones y deshacer.
        self.pila_acciones = []     # Pila para almacenar las acciones realizadas.
        self.pila_deshacer = []     # Pila para almacenar las acciones deshechas.

    def realizar_accion(self, accion):
        # Método para realizar una acción y almacenarla en la pila de acciones.
        self.pila_acciones.append(accion)
        print(f"Acción realizada: {accion}")

    def deshacer_accion(self):
        # Método para deshacer la última acción realizada.
        if self.pila_acciones:
            accion_deshacer = self.pila_acciones.pop()  # Obtener la última acción realizada.
            self.pila_deshacer.append(accion_deshacer)  # Almacenar la acción en la pila de deshacer.
            print(f"Se deshizo la acción: {accion_deshacer}")
        else:
            print("No hay acciones para deshacer")

    def rehacer_accion(self):
        # Método para rehacer la última acción deshecha.
        if self.pila_deshacer:
            accion_rehacer = self.pila_deshacer.pop()   # Obtener la última acción deshecha.
            self.pila_acciones.append(accion_rehacer)   # Agregar la acción de nuevo a la pila de acciones.
            print(f"Se rehizo la acción: {accion_rehacer}")
        else:
            print("No hay acciones para rehacer")

sistema = SistemaDeshacer()

# Realizar algunas acciones
sistema.realizar_accion("Escribir mensaje")
sistema.realizar_accion("Borrar texto")
sistema.realizar_accion("Copiar contenido")

# Deshacer acciones
sistema.deshacer_accion()
sistema.deshacer_accion()

# Rehacer una acción
sistema.rehacer_accion()