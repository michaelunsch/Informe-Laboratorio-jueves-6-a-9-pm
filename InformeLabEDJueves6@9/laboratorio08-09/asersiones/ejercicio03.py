def validar_calificacion(calificacion, rango_min, rango_max):
    if calificacion >= rango_min and calificacion <= rango_max:
        return True
    else:
        return False

# Ejemplo de uso
calificacion = 15
rango_min = 0
rango_max = 20

if validar_calificacion(calificacion, rango_min, rango_max):
    print("La calificación está dentro del rango.")
else:
    print("La calificación está fuera del rango.")