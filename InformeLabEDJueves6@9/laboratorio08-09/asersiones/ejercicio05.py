class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.nombre == other.nombre and self.edad == other.edad
        return False

# Crear dos objetos de la clase Persona
persona1 = Persona("michael", 28)
persona2 = Persona("diana", 26)

# Validar la igualdad de los objetos
if persona1 == persona2:
    print("Los objetos son iguales.")
else:
    print("Los objetos son diferentes.")