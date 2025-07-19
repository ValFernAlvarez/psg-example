# print ("Inicio")
# condicion = True
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# print ("Fin")
# #---
# print ("Inicio")
# numero = 4
# if numero % 2 == 0: # Si el módulo de 2 es 0
#     print ("El número es par")
# print ("Fin")
# #---
# if condicion:
#     print ("Cumple")
# else:
#     print ("No cumple")
# #---
# print ("Inicio")
# condicion = False
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# else:
#     # Bloque de código
#     print ("No cumple condición")
# print ("Fin")
# #---
# print ("Inicio")
# numero = 3
# if numero % 2 == 0: # Si el módulo de 2 es 0
#     print ("El número es par")
# else:
#     print ("El número es impar")
# print ("Fin")
# #---
# if condicion_1:
#     print ("Cumple 1")
#     if condicion_2:
#         print ("Cumple 2")
#     else:
#         print ("No cumple 2")
# else:
#     print ("No cumple 1")
# #---
# print ("Inicio Anidado")
# condicion_1 = True
# condicion_2 = False
# if condicion_1:
#     print ("Cumple condición 1")
#     if condicion_2:
#         print ("Cumple condición 2")
#     else:
#         print ("No cumple condición 2")
# else:
#     print ("No cumple condición 1")
# print ("Fin")
# #---
# print ("Inicio Par, Impar o Cero")
# numero = 0  
# if numero > 0 or numero < 0:
#     if numero % 2 == 0: # Si el módulo de 2 es 0
#         print ("El número es par")
#     else:
#         print ("El número es impar")
# else:
#     print ("El número es cero")
# print ("Fin")
# #---
# if condicion_1:
#     print ("Cumple 1")
# elif condicion_2:
#     print ("Cumple 2")
# else:
#     print ("No cumple 1 ni 2")
# #---
# print ("Inicio ELIF")
# condicion_1 = False
# condicion_2 = True
# if condicion_1:
#     print ("Cumple condición 1")
# elif condicion_2:
#     print ("Cumple condición 2")
# else:
#     print ("No cumple condición 1 ni 2")
# print ("Fin")
# #---
# print ("Inicio Positivo, Negativo o Cero")
# numero = -1
# if numero > 0:
#     print ("El número es positivo")
# elif numero < 0:
#     print ("El número es negativo")
# else:
#     print ("El número es cero")
# #---
# print ("Inicio Ternario")
# condicion = True
# resultado = "Cumple" if condicion else "No cumple"
# print (resultado)
# print ("Fin")
# #---
# print ("Truthiness Enteros")
# dividendo = int(input("Dividendo: "))
# divisor = int(input("Divisor: "))
# print (dividendo,divisor)
# if divisor: #divisor != 0
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")
# #---
# print ("Truthiness Flotantes")
# dividendo = float(input("Dividendo: "))
# divisor = float(input("Divisor: "))
# print (dividendo,divisor)
# if divisor: #divisor != 0.0
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")
# #---
# print ("Truthiness Cadenas")
# cadena = input("Cadena: ")
# print (cadena)
# if cadena: # len(cadena) != 0 or cadena != "" 
#     print ("La cadena no está vacía")
# else:
#     print ("La cadena está vacía")
# print ("Fin")
# #---
# print ("Truthiness Tuplas")
# tupla = tuple(input("Tupla: "))
# print (tupla)
# if tupla: # len(tupla) != 0 or tupla != ()
#     print ("La tupla no está vacía")
# else:
#     print ("La tupla está vacía")
# print ("Fin")
# #---
# print ("Truthiness Listas")
# lista = list(input("Lista: "))
# print (lista)
# if lista: # len(lista) != 0 or lista != []
#     print ("La lista no está vacía")
# else:
#     print ("La lista está vacía")
# print ("Fin")
# #---
# print ("Truthiness Conjuntos")
# conjunto = set(input("Conjunto: "))
# print (conjunto)
# if conjunto: 
#     print ("El conjunto no está vacío")
# else:
#     print ("El conjunto está vacío")
# print ("Fin")
# #---
# print ("Truthiness Diccionarios")
# diccionario = {}
# clave = input("Clave: ")
# valor = input("Valor: ")
# if clave:
#   diccionario = {clave:valor}
# print (diccionario)
# if diccionario: # diccionario != {}
#     print ("El diccionario no está vacío")
# else:
#     print ("El diccionario está vacío")
# print ("Fin")
# #---
# print ("Truthiness None")
# valor = None
# print (valor, type(valor))
# if valor: # valor != None
#     print ("El valor no es None")
# else:
#     print ("El valor es None")
# print ("Fin")
# #---
# entero = int(input("Entero: "))
# resultado = "Diferente de 0" if entero else "Igual a 0"
# print (resultado)
# flotante = float(input("Flotante: "))
# resultado = "Diferente de 0.0" if flotante else "Igual a 0.0"
# print (resultado)
# cadena = input("Cadena: ")
# resultado = "No está vacía" if cadena else "Está vacía"
# print (resultado)
#---
#---
# temperatura=float(input("Ingrese temperatura en C: "))
# #---
# if temperatura>30:
#     ventilador="Encendido"
# elif temperatura<20:
#     ventilador="Apagado"
# else:
#     ventilador="Invalido"
# #---
# print(f"Ventilador: {ventilador}")


# cesta_de_frutas=["banana","naranja"]
# #----
# if "manzana" in cesta_de_frutas:
#     compra="Si"
# else:
#     compra="No"
#     cesta_de_frutas.extend([])
#  #---
# print(f"Es necesario comprar?: {compra}")
# print(cesta_de_frutas)
#---
sexo=input("Sexo ('f' o 'm'): ").lower
edad=int(input("Edad: "))
nivel_de_hemoglobina=float(input("Nivel de hemoglobina: "))
#---
paciente=[]
paciente.append(sexo)
paciente.append(edad)
paciente.append(nivel_de_hemoglobina)
#---
resultado_a= ("m" in paciente) and (edad in paciente and edad>18) and (nivel_de_hemoglobina in paciente and nivel_de_hemoglobina<13.5)
resultado_b= ("f" in paciente) and (edad in paciente and edad>18) and (nivel_de_hemoglobina in paciente and nivel_de_hemoglobina<12)
resultado_c= (("m" or "f") in paciente) and (edad in paciente and edad<18) and (nivel_de_hemoglobina in paciente and nivel_de_hemoglobina<11)



