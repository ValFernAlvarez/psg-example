'''
1. Crea una calculadora interactiva que solicite dos números por teclado y realice las operaciones de suma,
    resta, multiplicación y división. El programa debe seguir solicitando dos números hasta que se ingrese
    "salir". Se debe incluir el manejo de excepciones para evitar errores al ingresar datos no numéricos,
    al intentar dividir entre cero, o ante cualquier otro error inesperado.
'''
def calcular_operacion_basica (numero_1,numero_2,operacion):
    if operacion == "+":
        return numero_1 + numero_2
    elif operacion == "-":
        return numero_1 - numero_2
    elif operacion == "*":
        return numero_1 * numero_2
    elif operacion == "/":
        if numero_2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return numero_1 / numero_2
    else:
        raise ValueError("Operación inválida. Usa '+', '-', '*', '/'.")
#---

#---
while True:
    try:
        numero_1_usr=input("Ingrese primer número (o 'salir'): ").strip().lower()
        if numero_1_usr == "salir":
            break
        numero_2_usr=input("Ingrese segundo número (o 'salir'): ").strip().lower()
        if numero_2_usr == "salir":
            break
        operacion_usr=input("Ingrese operación ('+','-','*','/'): ").strip()
        numero_convertido_1=float(numero_1_usr)
        numero_convertido_2=float(numero_2_usr)
        resultado=calcular_operacion_basica(numero_convertido_1,numero_convertido_2,operacion_usr)
    except ValueError as e:
        print("\n🚫  Error de valor:", e, type(e))
    except ZeroDivisionError as e:
        print("\n0️⃣  Error:", e, type(e))
    except Exception as e:
        print("\n💀  Error:", e, type(e))
    else:
        print(f"\nResultado: {round(resultado,2)}")