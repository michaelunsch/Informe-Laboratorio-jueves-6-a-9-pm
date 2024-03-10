def numeros_pares(n):
    if n>=2: #caso base
        if n%2==0:#caso recursivo
            print(f'el numero {n} es par')
        numeros_pares(n-1)
numeros_pares(100)
 