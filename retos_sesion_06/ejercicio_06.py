'''
6. ¿El cubo de 300 se encuentra en el siguiente rango? [N > 0 & N < 27_000_000]
'''
numero=300
cubo=300**3
mayor_a=cubo>0
menor_a=cubo<27000000
verificacion=mayor_a and menor_a
print("¿El cubo de 300 se encuentra en el rango?: ", verificacion)