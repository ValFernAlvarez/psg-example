'''
4. Crea un ciclo infinito que reciba una frase por teclado y verifique si la frase es palíndromo.
    La ejecución termina si la frase ingresada contiene la palabra salir
'''
while True:
    frase=input("Ingrese frase: ").lower()
    if frase==(frase[::-1]):
        print(f"{frase}: Es palíndromo.")
    elif frase=="salir":
        break
    else:
        print(f"{frase}: No es palíndromo.")