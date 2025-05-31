print("TIPOS DE DATOS BOOLEANOS")
print(True)
print(False)
print("OPERACIONES CON BOOLEANOS")
print(True+True)
print(True*True)
print(True*False)
print(False+False)
print(False*False)
#---
print("NÚMEROS Y BOOLEANOS")
print(10+True)
print(10+False)
print(10*True)
print(10*False)
#---
print ("DECLARAR BOOLEANAS")
var_booleana=True
print(var_booleana)
print(type(var_booleana))
var_booleana=False
print(var_booleana)
print(type(var_booleana))
#---
print("FUNCIÓN: bool()")
var_booleana=bool(1)
print(var_booleana)
print(type(var_booleana))
var_booleana=bool(0)
print(var_booleana)
print(type(var_booleana))
var_booleana=bool(15)
print(var_booleana)
print(type(var_booleana))
#---
print("COMPARACIÓN")
print(10==10)
print(10!=10)
print(10<10)
print(10>10)
print(10<=10)
print(10>=10)
a=10
b=10
print(a is b)
print(a is not b)
#---
print("ASIGNACIÓN")
x=10
mayor_que_cero=x>0
print(mayor_que_cero)
diferente_de_10=x!=10
print(diferente_de_10)
#---
print("OPERADORES LÓGICOS")
print(True and True)
print(True and False)
print(False or True)
print(False or False)
print(not True)
print(not False)
#---
print("OPERADORES LÓGICOS Y PRIORIDAD")
print(False and False or True)
print(False and (False or True))
print(not True and False or True)
print(not (True and False or False))
print(not True and (False or False))
print(not True and False or False)
#---
print("TABLAS DE VERDAD")
print("AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("OR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("NOT")
print(not True)
print(not False)
print("NAND")
print(not(True and True))
print(not(True and False))
print(not(False and True))
print(not(False and False))
print("NOR")
print(not(True or True))
print(not(True or False))
print(not(False or True))
print(not(False or False))
print ("XOR")
a=True
b=False
print((a or b) and not (a and b))
a=True
b=True
print((a or b) and not (a and b))
#---
print ("Ejemplo de uso Sensor y Batería")
sensor = True
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = True
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)
#---
print("EJEMPLO 1:\nDeterminar si el número 20 está en el rango 0 a 100.")
numero=20
comparacion=numero>=0 and numero<=100
print(comparacion)
#---
print("EJEMPLO 2:\nUn estudiante obtuvo las siguientes notas en sus exámenes: 15, 20, 16 determinar si el estudiante aprobó con una nota superior a 50.")
nota_a=15
nota_b=20
nota_c=16
aprobacion=(nota_a+nota_b+nota_c)>50
print(aprobacion)
#---
print("EJEMPLO 3:\nDeterminar si el número 15 es divisible por 3 y 5, pero no por 2.")
numero=15
divisible_3=numero%3==0
divisible_5=numero%5==0
no_divisible_2=numero%2!=0
verificacion=divisible_3 and divisible_5 and no_divisible_2
print(verificacion)
#---
print("CORTOCIRCUITOS")
print ("CON AND")
x=1
y=0
print (x > 2 and (x/y) > 2)
print (x > 0 and (x/y) > 0)
print ("CON OR")
x=1
y=0
print (x > 0 or (x/y) > 0)
print (x > 2 or (x/y) > 2)