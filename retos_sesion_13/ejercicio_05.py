'''
5. Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
'''
tablero=[[("#" if (i+j)%2==0 else "*")for j in range (8)]for i in range (8)]
#---
for fila in tablero:
    for columna in fila:
        print(columna, end=" ")
    print()