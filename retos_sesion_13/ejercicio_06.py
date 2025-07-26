'''
6. Crea un ciclo infinito que reciba un número por teclado y verifique si el número es múltiplo de 7.
    La ejecución termina si se ingresa el número 0
'''
while True:
    numero=int(input("Ingrese número: "))
    if numero==0:
        break
    elif numero%7==0:
        print(f"{numero}: Es múltiplo de 7.")
    else:
        print(f"{numero}: No es múltiplo de 7.")