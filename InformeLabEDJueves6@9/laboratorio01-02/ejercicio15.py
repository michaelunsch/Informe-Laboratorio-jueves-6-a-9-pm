numero=int(input("ingrese un numero entero:"))
suma=0
while numero>0:
    suma=suma+(numero%10)
    numero=numero//10
else:
    print("la suma de los digitos es: ",suma)