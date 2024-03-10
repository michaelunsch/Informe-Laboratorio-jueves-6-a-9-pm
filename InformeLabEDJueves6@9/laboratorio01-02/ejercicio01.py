
a=int(input("ingrese un numero:"))
b=int(input("ingrese el siguiente numero:"))
suma=a+b
resta=a-b
multiplicacion=a*b
if b==0:
    print(" la suma es:",suma,"\n la resta es",resta,"\n la multiplicacion es:",
          multiplicacion,"\n division: No se puede dividir entre cero")
else:
    division=a/b
    print(" la suma es:",suma,"\n la resta es",resta,"\n la multiplicacion es:",
          multiplicacion,"\n la division es:",division)
