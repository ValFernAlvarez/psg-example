'''
5. Crear una función que reciba una cadena y devuelva la cantidad de vocales que tiene.
'''
def contador_de_vocales (cadena):
    cantidad_de_vocales=sum([1 for letra in cadena.strip().lower() if letra in "aeiou"])
    return cantidad_de_vocales
#---
cadena_usr=input("Ingrese cadena: ")
vocales=contador_de_vocales(cadena_usr)
#---
print(f"Cadena: {cadena_usr}\nTotal de Vocales: {vocales}")