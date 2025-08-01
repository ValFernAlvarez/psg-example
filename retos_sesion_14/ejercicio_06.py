'''
6. Crear una función que reciba una lista de números y devuelva una lista con los números pares
    y otra lista con los números impares
'''
def contar_pares_impares (lista):
    pares=[int(numero) for numero in lista if int(numero)%2==0]
    impares=[int(numero) for numero in lista if int(numero)%2!=0]
    return pares, impares
#----
lista_usr=list(input("Ingrese números separados por espacios: ").replace(" ",""))
#---
lista_pares,lista_impares=contar_pares_impares(lista_usr)
print(f"Lista del Usuario: {lista_usr}\nLista de Pares: {lista_pares}\nLista de Impares: {lista_impares}")