'''
3. Crea un programa que simule el funcionamiento de un cajero automático solicitando
    al usuario un monto a retirar. Si el monto ingresado es mayor al saldo disponible,
    el programa debe lanzar una excepción personalizada que indique que no hay fondos
    suficientes. Además, si el monto ingresado es mayor a 1000, debe lanzarse una
    excepción genérica que advierta que el monto excede el límite permitido por transacción.
'''

class FondosInsuficientes(Exception):
    pass
#---

#---

saldo_disponible=800
print(f"\n¡BIENVENID@!\nSaldo Disponible: {saldo_disponible}")
#---

try:
    retiro_usr=float(input("Ingrese el monto a retirar: "))
    if retiro_usr<=0:
         raise ValueError ("El monto debe ser mayor a 0.")
    if retiro_usr>1000:
        raise Exception ("El monto excede el límite permitido por transacción (1000 $.).")
    if retiro_usr>saldo_disponible:
        raise FondosInsuficientes ("Fondos insuficientes.")
except ValueError as e:
    print("🚫 Error: ", e)
except FondosInsuficientes as e:
    print("🚫 Error: ", e)
except Exception as e:
    print("🚫 Error: ", e)
else:
    saldo_disponible-=retiro_usr
    print(f"\n¡Retiro exitoso!\nSaldo actual: {saldo_disponible}")
