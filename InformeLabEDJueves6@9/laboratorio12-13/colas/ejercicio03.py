#3. Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.

from collections import deque

class Laberinto:
    def __init__(self):
        # Inicialización del laberinto y atributos relacionados
        self.laberinto = []  # Matriz que representa el laberinto
        self.filas = 0        # Número de filas en el laberinto
        self.columnas = 0     # Número de columnas en el laberinto

    def cargar_laberinto(self, nombre_archivo):
        # Método para cargar el laberinto desde un archivo
        with open(nombre_archivo, 'r') as file:
            for linea in file:
                # Leer cada línea del archivo y agregarla al laberinto
                self.laberinto.append(list(linea.strip()))  # Eliminar espacios en blanco al final de la línea
                self.filas += 1                              # Incrementar el contador de filas
                self.columnas = len(linea.strip())            # Obtener la longitud de la fila

    def encontrar_camino(self, inicio, destino):
        # Método para encontrar el camino más corto desde el inicio hasta el destino
        visitado = set()                    # Conjunto para almacenar nodos visitados
        cola = deque([(inicio, [])])        # Cola para realizar el recorrido BFS (Breadth-First Search)

        while cola:
            (fila, columna), camino = cola.popleft()  # Obtener el nodo y el camino actual desde la cola
            if (fila, columna) == destino:            # Si llegamos al destino, devolvemos el camino
                return camino + [(fila, columna)]

            if (fila, columna) not in visitado and self.es_valido(fila, columna):
                # Si el nodo actual no ha sido visitado y es válido, exploramos sus vecinos
                visitado.add((fila, columna))  # Marcamos el nodo actual como visitado
                for nueva_fila, nueva_columna in self.obtener_vecinos(fila, columna):
                    # Para cada vecino válido, agregamos su ubicación y el camino actualizado a la cola
                    cola.append(((nueva_fila, nueva_columna), camino + [(fila, columna)]))
        return None

    def es_valido(self, fila, columna):
        # Método para verificar si una posición en el laberinto es válida
        return 0 <= fila < self.filas and 0 <= columna < self.columnas and self.laberinto[fila][columna] != '*'

    def obtener_vecinos(self, fila, columna):
        # Método para obtener los vecinos válidos de una posición dada en el laberinto
        movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Movimientos posibles: abajo, arriba, derecha, izquierda
        vecinos = []
        for dx, dy in movimientos:
            nueva_fila, nueva_columna = fila + dx, columna + dy
            if self.es_valido(nueva_fila, nueva_columna):
                # Si la posición del vecino es válida, la agregamos a la lista de vecinos
                vecinos.append((nueva_fila, nueva_columna))
        return vecinos

    def mostrar_laberinto(self):
        # Método para imprimir el laberinto en la consola
        for fila in self.laberinto:
            print(''.join(fila))  # Imprimir cada fila concatenada

laberinto = Laberinto()
laberinto.cargar_laberinto('laberinto.txt')  # Cargar el laberinto desde un archivo

print("Laberinto:")
laberinto.mostrar_laberinto()  # Mostrar el laberinto en la consola

inicio = (0, 0)      # Posición de inicio
destino = (5, 5)     # Posición de destino

camino_mas_corto = laberinto.encontrar_camino(inicio, destino)
if camino_mas_corto:
    # Si se encontró un camino, imprimirlo
    print("Camino más corto:")
    for paso in camino_mas_corto:
        print(paso)
else:
    print("No se encontró un camino al destino.")  # Si no se encontró un camino, imprimir un mensaje