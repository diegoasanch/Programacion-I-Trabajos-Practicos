'''
TP3. Ejercicio 4. Juego 2048
'''
from crear_matrices import matrizCuad
from random import randint

def imprimirTablero(matriz):
    '''muestra una matriz por pantalla.'''

    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%4d" %matriz[f][c], end=" ")
        print('\n')

def nueva_pantalla(n=30):
    'Imprime n lineas para limpiar la pantalla del terminal'
    print('\n' * n)

def generarBaldosa():
    'Devuelve un numero para baldosa nueva al azar'
    opciones = [2, 4]
    return opciones[randint(0, len(opciones) - 1)]

def iniciarTablero(n=4):
    'Inicializa el tablero nxn del juego'
    orden = n
    matriz = matrizCuad(orden)
    
    for fil in range(orden):
        for col in range(orden):
            matriz[fil][col] = generarBaldosa()
    return matriz

def posicionValida(pos, rango):
    '''Valida una posicion dentro de una matriz
    
    param: rango, puede ser la matriz dentro de la cual se ingresa una fila
    o la fila dentro de la cual se escogera una columna'''
    pos_valida = pos in range(len(rango))
    return pos_valida

def ingresoPos(matriz, tipo):
    '''Ingresa y valida una fila o una columna dentro de matriz
    
    param: matriz = matriz en la cual se opera
    tipo = str con fila o columna
    '''
    print(f'Ingrese la {tipo} de la baldosa: ', end='')
    pos = int(input())
    while not posicionValida(pos, matriz):
        print(f'\n{tipo} invalida!! Intente de nuevo.')
        print(f'Ingrese la {tipo} de la baldosa: ', end='')
        pos = int(input())
    return pos

def ingresoDireccion():
    'Ingresa y valida la direccion del movimiento de la baldosa'

    movimientos = [2, 4, 6, 8]
    mov = int(input('Ingrese la direccion a mover la baldosa: ')) 
    while mov not in movimientos:
        print('Movimiento invalido!! Intente de nuevo')
        mov = int(input('Ingrese la direccion a mover la baldosa: '))
    return mov

def ingresoMovimiento(matriz, fila, columna):
    '''Valida el movimiento a realizar sobre la baldosa matriz[fila][columna]
    
    Devuelve la nueva fila y la nueva columna a la cual mover la baldosa'''
    
    movValido = False
    while not movValido:
        nuevaFila = fila
        nuevaCol = columna

        direccion = ingresoDireccion()
        if direccion == 2:
            nuevaFila += 1
        elif direccion == 4:
            nuevaCol -= 1
        elif direccion == 6:
            nuevaCol += 1
        else:
            nuevaFila -= 1
        movValido = posicionValida(nuevaFila, matriz) and posicionValida(nuevaCol, matriz[0])
        if not movValido:
            print('\nMovimiento no permitido! Intente de nuevo.\n')
    return nuevaFila, nuevaCol      

def moverBaldosa(matriz, fila, columna, nFila, nColumna):
    '''
    Realiza el movimiento de baldosa dentro de la matriz y genera nueva baldosa
    Devuelve 1 si se realizo un movimiento valido, de lo contrario retorna 0
    '''

    if matriz[nFila][nColumna] == matriz[fila][columna]:
        matriz[nFila][nColumna] *= 2

        matriz[fila][columna] = generarBaldosa()
        return 1
    else:
        return 0  

def hacerJugada(matriz):
    '''Mueve una posicion en una matriz a otra, validando las 
    coordenadas ingresadas por el usuario
    
    Devuelve 1 si se realizo un movimiento valido, de lo contrario retorna 0
    '''
    fila = ingresoPos(matriz, 'fila')
    columna = ingresoPos(matriz, 'columna')
    nFila, nCol = ingresoMovimiento(matriz, fila, columna)
    jug = moverBaldosa(matriz, fila, columna, nFila, nCol)
    return jug

def juegoGanado(matriz):
    'Determina si se alcanzo el numero 2048 en el tablero'

    ganado = False
    for fila in matriz:
        if 2048 in fila:
            ganado = True
    return ganado

def movDisponibles(matriz):
    'Determina si quedan jugadas posibles en el tablero'

    jugable = False
    fi = 0
    while fi < len(matriz) and not jugable:
        co = 0
        while co < len(matriz[0]) and not jugable:
            baldosa = matriz[fi][co]
            mov1, mov2, mov3, mov4 = False, False, False, False
            if fi > 0:
                mov1 = baldosa == matriz[fi - 1][co]
            if fi < len(matriz) - 1:
                mov2 = baldosa == matriz[fi + 1][co]
            if co > 0:
                mov3 = baldosa == matriz[fi][co - 1]
            if co < len(matriz) - 1:
                mov4 = baldosa == matriz[fi][co + 1]
            jugable = (mov1 or mov2 or mov3 or mov4)
            co += 1
        fi += 1
    return jugable


def __main__():
    print('\n\nJuego 2048!\n\n\n')
    tablero = iniciarTablero()
    ganado = False
    jugable = True
    movimientos = 0

    while not ganado and jugable:
        print(f'Movimientos: {movimientos}\n\n')
        print('Tablero:\n')
        imprimirTablero(tablero)
        jugada = hacerJugada(tablero)
        movimientos += jugada
        ganado = juegoGanado(tablero)
        jugable = movDisponibles(tablero)
        nueva_pantalla()
    
    if ganado:
        print(f'Felicidades!! Has terminado el juego en {movimientos} jugadas!\n\n\n')
    else:
        print(f'El juego se ha atascado despues de {movimientos} movimientos :( Mejor suerte en la proxima partida!!')
    
    print('\n\nTablero final:')
    imprimirTablero(tablero)

if __name__ == "__main__":
    __main__()
