'''
5. Escribe un programa que reciba una cadena y retorna verdadero o falso
    si es palindrome sin importar los espacios, mayúsculas o minúsculas.
'''
cadena=input("Ingrese cadena: ").lower()
quitar_espacios=cadena.replace(" ","")
cadena_invertida=cadena[::-1]
verificacion=cadena==cadena_invertida
print(f"¿Es palindrome?: {verificacion}")
