'''
1. Imprimir los 20 primeros números de la sucesión de Lucas.
'''
print("\nSucesión de Lucas")
#---
actual=2
siguiente=1
#---
for termino in range (20):
    print(actual,end=", " if termino<20-1 else " ")
    temporal=actual
    actual=siguiente
    siguiente+=temporal
print("\n")