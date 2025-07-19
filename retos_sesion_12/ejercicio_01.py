'''
1. Crear un script que pida un número entero y verifique si es
    múltiplo de 5 usando operador ternario.
'''
numero=int(input("Ingrese un número entero: "))
#---
verficacion=("Es múltiplo de 5." if numero%5==0 else "No es múltiplo de 5.")
print(f"\n{numero}: {verficacion}")
