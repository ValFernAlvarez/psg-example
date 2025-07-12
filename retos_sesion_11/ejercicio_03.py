'''
3. Crea un diccionario con la siguiente tupla de especies animales:
    a. Del diccionario obtén y elimina el valor de la clave 'aves'
    b. Modifica el valor de la clave 'felino' por '🐈'
    c. Cambia la clave canino por caninos y su valor por ['🐶','🐕']
'''
lista_animales=(('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅']))
diccionario_animales=dict(lista_animales)
print(f"Diccionario de Animales:\n{diccionario_animales}")
#---Para 'a'---
eliminar_aves=diccionario_animales.pop("aves")
print(f"\nPARA 'A':\nDiccionario de Animales Sin Aves:\n{diccionario_animales}")
#---Para 'b'---
diccionario_animales.update(felino="🐈")
print(f"\nPARA 'B':\nDiccionario de Animales 'Felino' actualizado:\n{diccionario_animales}")
#---Para 'c'---
clave_canino=diccionario_animales.pop("canino")
diccionario_animales["caninos"]=['🐶','🐕']
print(f"\nPARA 'C':\nDiccionario de Animales 'Canino' actualizado:\n{diccionario_animales}")
