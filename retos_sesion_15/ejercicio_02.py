'''
2. Crea un programa que permita construir una canasta de frutas solicitando ingresar frutas por teclado,
    una por una, y almacenándolas en una lista. El programa debe finalizar cuando se ingrese "salir".
    Solo se permiten las siguientes frutas: 🍅, 🍇, 🍈, 🍉, 🍊, 🍌, 🍍, 🍑
Si se ingresa una fruta no permitida, el programa debe lanzar una excepción personalizada que indique
que la fruta no es válida.
'''
class FrutaNoPermitida (Exception):
    pass
#---
canasta_de_frutas=[]
#---
while True:
    try:
        fruta_usr=input("Ingrese fruta: ")
        if fruta_usr == "salir":
            break
        elif fruta_usr in "🍅🍇🍈🍉🍊🍌🍍🍑":
            canasta_de_frutas.append(fruta_usr)
        else:
            raise FrutaNoPermitida ("Solo se ingresan frutas permitidas.")
    except FrutaNoPermitida as e:
      print("🚫 Error:", e)
#---
print(f"Canasta final: {canasta_de_frutas}")  

