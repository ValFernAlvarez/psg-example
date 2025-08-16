'''
2. Tienes un juego de adivinanzas en el que el jugador tiene que adivinar un
    número entre 1 y 100. El juego tiene bugs, arréglalos!
'''
def obtener_aleatorio():
    numeros = set(str(numero)for numero in range(1, 101)) # Cambiar 'list' por 'set' ya que salía de manera consistente '100' como número secreto.
    secreto = int(numeros.pop()) 
    return secreto
#---
def adivina(secreto):
        intentos = 0
        print ("Que número estoy pensando? (1-100)")
        while True:
            try:
                intento = int(input(f"Intento N°: {intentos+1}: "))
                if intento == secreto:
                    print ("Felicidades! Has adivinado el número!")
                    break
                elif intento < secreto:
                    print ("El número es mayor.")
                else:
                    print ("El número es menor.")
                intentos += 1 # Para que solo cuente en intentos válidos.
            except ValueError:
                print ("Por favor, ingresa un número válido.")
            #finally:
                #intentos += 1 
        print (f"Has adivinado el número en {intentos} intentos.\n") # Eliminar '*10' por expresar una cantidad de intentos errónea.

nombre_jugador = "Guest"


def jugar():
    ciclo=0
    while True:
        if ciclo==0:
            print ("Bienvenido al juego de adivinanzas! del Python Study Group 2025")
            print ("="*63)
            nombre_jugador = input("¿Cuál es tu nombre?: ")
            print (f"Bienvenido, {nombre_jugador}!")
            print ("="*63)
            print ()
        opcion = input("Quieres jugar? (s/n): ")
        if opcion.lower() != 's': # Corrección a minúscula para iniciar juego.
            break
        secreto = obtener_aleatorio()
        adivina(secreto)
        ciclo=+1
    print ("Gracias por participar!")
    print (f"🐍 Gracias {nombre_jugador.upper()} por ser parte del Python Study Group 2025! 🐍")

jugar()