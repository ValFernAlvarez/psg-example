'''
6. Crea una calculadora por consola que realice las operaciones de suma,
    resta, multiplicación y división. Las operaciones se ingresan por
    teclado separadas por comas en el siguiente formato:
-numero1, número2, operación
-ejemplo: 10, 5, +
verifica si la operación solicitada es válida y muestra el resultado
'''
#---
operacion_usr=input("\nFORMATO: numero1, número2, operación\nIngrese operación básica: ").replace(" ","").split(",")
#---
numero1=float(operacion_usr[0])
numero2=float(operacion_usr[1])
#---
operaciones_basicas={
   "+":numero1+numero2,
   "-":numero1-numero2,
   "*":numero1*numero2,
    "/":numero1/numero2}
#---
if operacion_usr[2] in operaciones_basicas:
    resultado=operaciones_basicas[operacion_usr[2]]
    print(f"-------------\nResultado: {round(resultado,2)}")
else:
    print("No es una operación válida.")

