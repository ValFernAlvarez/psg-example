'''
7. Tres en Raya:
    -Crear una función que reciba una jugada en cada ejecución
    -Cuando la jugada se completa se debe mostrar el tablero
    -El tablero debe ser una lista de listas
    -El juego termina cuando un jugador gana o hay un empate
    -Si una casilla ya está ocupada, se debe pedir una nueva jugada
    -Se debe mostrar a quién le toca jugar, si a "X" o "O"
'''

#-----VERIFICACION DE TURNO------
def realizar_tablero ():
    return [["[ ]" for j in range (3)]for i in range (3)]
#---
def mostrar_tablero (tablero):
    print()
    for fila in tablero:
        print(*fila)
#---
def pedir_jugada (turno):
    print(f"Turno : {turno}")
    return input("Ingrese la coordenadas 'i' y 'j' separados por espacios: ").strip().split(" ")
#---
def verificar_casilla (tablero,i,j,simbolo,jugada):
    while True:
        if tablero[i][j] != "[ ]":
            print("La casilla no está vácia.")
            jugada=input("Ingrese la coordenadas 'i' y 'j' separados por espacios: ").strip().split(" ")
            i=int(jugada[0])-1
            j=int(jugada[1])-1
        elif i<0 or j<0:
            print("Ingrese 'i' y 'j' entre 1 y 3. ")
            jugada=input("Ingrese la coordenadas 'i' y 'j' separados por espacios: ").strip().split(" ")
            i=int(jugada[0])-1
            j=int(jugada[1])-1
        else:
            tablero [i][j] = simbolo
            break

#-----VERIFACION GANADOR------
def ganar_fila(tablero, simbolo):
    for fila in tablero:
        contador_simbolo = 0
        for celda in fila:
            if celda == simbolo:
                contador_simbolo += 1
        if contador_simbolo == 3:
            return True
    return False
#---
def ganar_columna(tablero, simbolo):
    for col in range(3):
        contador_simbolo = 0
        for fila in range(3):
            if tablero[fila][col] == simbolo:
                contador_simbolo += 1
        if contador_simbolo == 3:
            return True
    return False
#---
def ganar_diagonal_principal(tablero, simbolo):
    contador_simbolo = 0
    for i in range(3):
        if tablero[i][i] == simbolo:
            contador_simbolo += 1
    return contador_simbolo == 3
#---
def ganar_diagonal_secundaria(tablero, simbolo):
    contador_simbolo = 0
    for i in range(3):
        if tablero[i][2 - i] == simbolo:
            contador_simbolo += 1
    return contador_simbolo == 3
#---
def verificar_ganador (tablero,simbolo):
    return (
        ganar_fila(tablero, simbolo) or
        ganar_columna (tablero, simbolo) or
        ganar_diagonal_principal (tablero, simbolo) or
        ganar_diagonal_secundaria (tablero, simbolo))

#-----MECANISMO DE JUEGO------
def mecanismo_de_juego ():
    ##--Locales--
    tablero=realizar_tablero()
    contador=0
    mostrar_tablero(tablero)
    ##--Turnos--
    while contador<9:
        contador+=1
        simbolo="[X]" if contador % 2 != 0 else "[O]"
        turno="Jugador 1 -> 'X'" if simbolo == "[X]" else "Jugador 2 -> 'O'"
        jugada=pedir_jugada(turno)
        ###--Verificacion de casilla--
        verificar_casilla (tablero,int(jugada[0])-1,int(jugada[1])-1,simbolo,jugada)
        ###--Tablero--
        mostrar_tablero(tablero)
        ###--Verificacion de ganador--
        if verificar_ganador(tablero,simbolo):
            print(f"Ganador: {'Jugador 1' if simbolo == '[X]' else 'Jugador 2'}")
            contador=10
    else:
        print("Empate." if verificar_ganador(tablero,simbolo)==False else "")

#-----EJECUCION DE JUEGO------
print("TRES EN RAYA\n-------------------------------------------------------")
while True:
    mecanismo_de_juego()
    if input("Desea jugar de nuevo?: ").strip().lower()=="no":
        break