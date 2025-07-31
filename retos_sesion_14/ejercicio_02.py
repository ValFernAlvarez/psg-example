'''
2.  Crear una función que reciba dos números y una operación (suma, resta, multiplicación, división)
    y devuelva el resultado de la operación
'''
def calcular_operacion_basica (numero_1,numero_2,operacion):
    if operacion == "suma":
        return numero_1 + numero_2
    elif operacion == "resta":
        return numero_1 - numero_2
    elif operacion == "multiplicacion":
        return numero_1 * numero_2
    elif operacion == "division":
        return numero_1 / numero_2
    else:
        return "Operación inválida."
#---
numero_1_usr=float(input("Ingrese primer número: "))
numero_2_usr=float(input("Ingrese segundo número: "))
operacion_usr=input("Ingrese operación: ").strip().lower()
#---
resultado=calcular_operacion_basica(numero_1_usr,numero_2_usr,operacion_usr)
print(f"Resultado: {round(resultado,2)}")