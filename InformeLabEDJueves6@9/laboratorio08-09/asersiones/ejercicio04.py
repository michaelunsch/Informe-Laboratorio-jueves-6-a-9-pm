def validar_lista(lista):
    if len(lista) > 0:
        return True
    else:
        return False

# Ejemplo de uso
mi_lista = [1,]

if validar_lista(mi_lista):
    print("La lista no está vacía.")
else:
    print("La lista está vacía.")