palabra=input("ingrese una palabra:")
string=str(palabra)
reverse=string[::-1]
print(string)
print(reverse)
if string==reverse:
    print("la palabra es palindrome",palabra)
else:
    print("la palabra no es palindrome",palabra)