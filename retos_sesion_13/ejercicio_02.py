'''
2. Imprimir los 20 primeros números que sean múltiplos de 2 y 5.
'''
contador=0
numero=0
while contador<20:
    if numero%2==0 and numero%5==0:
        contador+=1
        print(numero)
    numero+=1
