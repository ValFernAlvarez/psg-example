'''
2. Crea una tupla con los siguientes elementos:
    'a','b','c','d','e','f','g','h','i','j'
    Imprime el primer elemento
    Imprime el último elemento
    Imprime un slice del índice 3 al 5
    Imprime un slice del 5 al 9 con pasos de 3
    Imprime un slice del 9 al 0 con pasos de -2
'''
letras=('a','b','c','d','e','f','g','h','i','j')
print(f"Primer elemento: {letras[0]}")
print(f"Último elemento: {letras[-1]}")
print(f"Slice 3 al 5: {letras[3:6]}")
print(f"Slice 5 al 9 con pasos de 3: {letras[5:10:3]}")
print(f"Slice 9 al 0 con pasos de -2: {letras[9:0:-2]}")