#4. Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como completadas y mostrar la próxima tarea pendiente.

class GestorTareas:
    # Definición de la clase GestorTareas para gestionar tareas.
    def __init__(self):
        # Inicialización de la lista de tareas.
        self.tareas = []

    def agregar_tarea(self, descripcion):
        # Método para agregar una tarea con su descripción a la lista de tareas.
        self.tareas.append({'descripcion': descripcion, 'completada': False})
        # Mensaje que indica que se ha agregado una tarea.
        print(f"Tarea '{descripcion}' agregada.")

    def marcar_completada(self, indice):
        # Método para marcar una tarea como completada en la lista de tareas.
        if 0 <= indice < len(self.tareas):
            # Si el índice es válido, se marca la tarea como completada.
            self.tareas[indice]['completada'] = True
            # Mensaje que indica que se ha marcado la tarea como completada.
            print(f"Tarea '{self.tareas[indice]['descripcion']}' marcada como completada.")
        else:
            # Si el índice es inválido, se muestra un mensaje de error.
            print("Índice de tarea inválido.")

    def mostrar_proxima_pendiente(self):
        # Método para mostrar la próxima tarea pendiente en la lista de tareas.
        for tarea in self.tareas:
            if not tarea['completada']:
                # Si la tarea no está completada, se muestra como próxima pendiente.
                print(f"Próxima tarea pendiente: {tarea['descripcion']}")
                return
        # Si no hay tareas pendientes, se muestra un mensaje indicando esto.
        print("No hay tareas pendientes.")

gestor = GestorTareas()

# Agregar algunas tareas al gestor
gestor.agregar_tarea("Hacer la compra")
gestor.agregar_tarea("Estudiar para el examen")
gestor.agregar_tarea("Llamar al cliente")

# Marcar la primera tarea como completada
gestor.marcar_completada(0)

# Mostrar la próxima tarea pendiente
gestor.mostrar_proxima_pendiente()