'''
1. Crea una funcion que reciba una lista de calificaciones y devuelva el promedio de las mismas.
    Las calificaciones son: 50, 75, 80, 91, 70
'''
calificaciones=[50, 75, 80, 91, 70]
def calcular_promedios (lista):
    return sum(lista)/len(lista)
#---
promedio=calcular_promedios(calificaciones)
#----
print(f"Promedio: {round(promedio,2)}")