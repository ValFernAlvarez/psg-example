'''
2. Crea un diccionario de alimentos y que animales domésticos lo consumen.
    a. Añade al diccionario 4 alimentos más, usando update(clave=valor)
    b. Existe en el diccionario de alimentos la comida 'trigo'?
    c. Elimina la comida 'zanahoria' del diccionario de alimentos
'''
alimentos_para_animales={
    "carne" : ["gato", "perro"],
    "zanahoria" : ["conejo"]}
print(f"Alimentos para Animales:\n{alimentos_para_animales}")
#---Para 'a'---
alimentos_para_animales.update(semillas=["canario","hámster"],lechuga="tortuga",pescado="gato",frutas="loro")
print(f"\nPARA 'A':\nAlimentos para Animales Actualizado:\n{alimentos_para_animales}")
#---Para 'b'---
existe_trigo="trigo" in alimentos_para_animales
print(f"\nPARA 'B':\n¿Existe trigo?: {existe_trigo}")
#---Para 'c'---
del alimentos_para_animales ["zanahoria"]
print(f"\nPARA 'C':\nAlimentos para Animales Sin Zanahoria:\n{alimentos_para_animales}")
#---