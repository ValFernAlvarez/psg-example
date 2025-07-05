'''
2. El dueño de una tienda de ropa deportiva ha comprado ropa formal y quiere abrir una nueva tienda que
    combine ambos estilos. Crea un conjunto con las prendas de ambos tipos con las listas de prendas.
'''
lista_deportiva=["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
lista_formal=["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]
#---
conjunto_de_ambos=set(lista_deportiva)|set(lista_formal)
print(f"Conjunto de ambos tipos de prendas: {conjunto_de_ambos}")