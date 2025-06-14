'''
Ingresa una pregunta por teclado y almacena el valor en una tupla
    Concatena las tupla
    ('¿', ) + pregunta + ('?', )
    Imprime el resultado concatenado
    Repite la tupla concatenada 2 veces e imprime el nuevo resultado
'''
pregunta_usr=input("Ingrese una pregunta (sin signos): ")
pregunta=(pregunta_usr,)
concatenado_1=('¿', ) + pregunta + ('?', )
print(f"Primer concatenado: {concatenado_1}")
concatenado_2=concatenado_1*2
print(f"Segundo concatenado: {concatenado_2}")
