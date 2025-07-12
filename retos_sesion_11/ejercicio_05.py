'''
5. Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies:
    a. Añade al arca 3 especies más usando update()
    b. Toma lista de los animales en el arca iterando el diccionario
    c. Existe en el arca la especie 'dragon' 🐲?
    d. Elimina la especie unicornio del arca
    e. Modifica el valor de la especie jirafa por 2
    f. Vacía el arca después del diluvio
'''
arca={"🐶" : 2,
      "🐱" : 2,
      "🐯" : 2,
      "🐵" : 2,
      "🦄" : 0,
      "🦒" : 1}
print(f"\nArca Original:\n{arca}")
#---para 'a'---
arca.update({"🐘":2, "🦓": 2, "🐧": 2})
print(f"\nPARA 'A':\nArca +3 especies:\n{arca}")
#---Para 'b'---
print(f"\nPARA 'B':")
iterador=iter(arca.items())
siguiente=next(iterador)
print(siguiente)
siguiente=next(iterador)
print(siguiente)
siguiente=next(iterador)
print(siguiente)
siguiente=next(iterador)
print(siguiente)
siguiente=next(iterador)
print(siguiente)
siguiente=next(iterador)
print(siguiente)
siguiente=next(iterador)
print(siguiente)
siguiente=next(iterador)
print(siguiente)
siguiente=next(iterador)
print(siguiente)
#---Para 'c'---
existe_dragon="🐲" in arca
print(f"\nPARA 'C':\n¿Existe '🐲'?: {existe_dragon}")
#---Para 'd'---
del arca ["🦄"]
print(f"\nPARA 'D':\nArca sin '🦄':\n{arca}")
#---Para 'e'---
arca["🦒"]=2
print(f"\nPARA 'E':\nArca cambio de '🦒':\n{arca}")
#---Para 'f'---
arca.clear()
print(f"\nPARA 'F':\nArca después del diluvio':\n{arca}")
