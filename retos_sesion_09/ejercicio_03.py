'''
3. Crear una lista de personas con 10 nombres de personas:
    3.1. Obtener una sub lista de 5 a 9 con saltos de 2 en 2
    3.2. Buscar si existe el nombre "José" en la lista original
    3.3. Ordenar la sub lista alfabéticamente a-z
    3.4. Ordenar la lista original alfabéticamente descendente z-a
'''
lst_nombres=["Pim", "Charlie", "Glep", "Alan", "Mr. Frog", "Shrimp", "Boss", "Desmond", "Smormu", "Dj Spit"]
#---
sub_lista=lst_nombres[5:10:2]
#---
verificacion_jose="José" in lst_nombres
#---
ordenar_sub_lista_az=sorted(sub_lista)
#---
ordenar_lst_nombres_za=sorted(lst_nombres, reverse=True)
#---
print(f"Sub lista de 5 a 9 con saltos de 2 en 2: {sub_lista}\n¿Existe el nombre 'José' en la lista original?: {verificacion_jose}\nSub lista ordenada alfabéticamente a-z: {ordenar_sub_lista_az}\nLista original ordenada alfabéticamente descendente z-a: {ordenar_lst_nombres_za}")
