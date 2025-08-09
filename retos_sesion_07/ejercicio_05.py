'''
5. Escribe un programa que reciba una cadena y retorna verdadero o falso
    si es palindrome sin importar los espacios, mayúsculas o minúsculas.
'''
cadena=input("Ingrese cadena: ").lower()
quitar_espacios=cadena.replace(" ","")
cadena_invertida=quitar_espacios[::-1]
verificacion=(quitar_espacios==cadena_invertida)
print(f"¿Es palindrome?: {verificacion}")
