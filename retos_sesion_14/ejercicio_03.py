'''
3. Crear una función recursiva para obtener el N-esimo número de la serie de Lucas.
'''
def serie_de_lucas (termino_de_secuencia):
    if termino_de_secuencia == 0:
        return 2
    elif termino_de_secuencia == 1:
        return 1
    else:
        return serie_de_lucas(termino_de_secuencia-1) + serie_de_lucas(termino_de_secuencia-2)
#---
n_esimo=int(input("Ingrese el N-esimo número: "))
#---
numero=serie_de_lucas(n_esimo)
print(f"El término {n_esimo} de la Serie de Lucas es: {numero}")
