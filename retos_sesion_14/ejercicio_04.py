'''
4. Crear una función anónima para obtener el valor absoluto de un número.
'''
calcular_valor_absoluto = lambda numero : numero*(-1) if numero<0 else numero*(1)
numero_usr=int(input("Ingrese número: "))
valor_absoluto=calcular_valor_absoluto(numero_usr)
#---
print(f"Valor Absoluto |{numero_usr}| : {valor_absoluto}")