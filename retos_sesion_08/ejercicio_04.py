'''
4. Las notas de un estudiante durante un semestre son:
    10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100
Genera una tupla con los resultados y calcula el promedio para saber si aprobó o no el semestre utiliza la función sum() y len()
El promedio debe ser mayor o igual a 51 para aprobar
'''
notas=(10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)
total=sum(notas)
num_materias=len(notas)
promedio=total/num_materias
verificacion=promedio>=51
print(f"Promedio: {round(promedio,2)}\n¿Aprobó?: {verificacion}")