#aserciones
import datetime

def validar_edad(fecha_nacimiento):
    fecha_actual = datetime.date.today()
    edad = fecha_actual.year - fecha_nacimiento.year
    if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):
        edad -= 1
    return edad

# Ejemplo de uso
fecha_nacimiento = datetime.date(1994, 7, 21)  # Reemplaza con la fecha de nacimiento del usuario
edad = validar_edad(fecha_nacimiento)
print("La edad del usuario es:", edad)