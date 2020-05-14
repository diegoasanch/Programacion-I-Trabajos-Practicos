from random import randint

matrizCuad = lambda orden, filler=0: [[filler]*orden for i in range(orden)]

# ------ Ej 2

def matrizDiagImpar(n):
    'crea una matriz diagonal orden n x n con numeros impares'
    
    matriz = matrizCuad(n)
    num = 1
    for i in range(n):
        matriz[i][i] = num
        num += 2
    return matriz

def matrizDiagSec(n=4):
    'crea una matriz con potencias de 3 decrecientes en la diagonal secundaria'
    
    matriz = matrizCuad(n)
    num = 3 ** (n-1)
    col = n-1
    for i in range(n):
        for j in range(n):
            if j == col:
                matriz[i][j] = num
                num //= 3
                col -= 1
    return matriz

def matrizTriangInf(n=4):
    '''Crea una matriz diagonal inferior,
    los elementos de cada fila son la cantidad de filas en orden decreciente
    '''
    matriz = matrizCuad(n)
    fila = n
    for i in range(n):
        for j in range(n):
            if j <= i:
                matriz[i][j] = fila
        fila -= 1
    return matriz

def filasPotencia2(n=4):
    '''Crea una matriz en donde los valores de cada fila son la potencia
    de 2 ^ (n-1) en orden decreciente
    '''
    fila = 2 ** (n - 1)
    matriz = matrizCuad(n)
    for i in range(n):
        for j in range(n):
            matriz[i][j] = fila
        fila //= 2
    return matriz

def matrizCadaImpar(n=4):
    'Crea una matriz con numeros naturales cada 2 posiciones'
    matriz = matrizCuad(n)
    sec, num = 0, 1
    for i in range(n):
        for j in range(n):
            if sec % 2 != 0:
                matriz[i][j] = num
                num += 1
            if j != n - 1:
                sec += 1
    return matriz

def trianInferiorInv(n=4):
    'Crea una matriz triangular inferior inversa con secuencia de numeros'

    matriz = matrizCuad(n)
    sec = 1
    col = n - 1
    for i in range(n):
        for j in range(n-1, -1, -1):
            if j >= col:
                matriz[i][j] = sec
                sec += 1
        col -= 1
    return matriz

# ------------------------- TP2.G) ------------------------------

def matrizEspiral(n=4):
    'Crea una matriz en espiral en sentido horario'

    s = 1
    i, j = 0, 0
    matriz = matrizCuad(n)
    horizontal(matriz, s, i, j, 1)
    return matriz

def horizontal(matriz, sec, x, y, direccion):
    '''Agrega el siguiente numero de la secuencia sec en la fila actual
    
    Parametros: matriz = matriz, sec = secuencia de numeros, x = columna actual,
    y = fila actual, direccion = direccion de movimiento (1 = abajo, -1 = arriba)
    '''
    # mientras sea una columna valida y esa posicion este vacia
    while x in range(len(matriz[0])) and matriz[y][x] == 0:
        matriz[y][x] = sec
        sec += 1
        x += direccion
    x -= direccion

    # check disponibilidad cambio de mov
    if y in range(len(matriz)) and matriz[y + direccion][x] == 0:
        vertical(matriz, sec, x, y + direccion, direccion)

def vertical(matriz, sec, x, y, direccion):
    'Agrega el siguiente numero de la secuencia sec en la columna actual'

    # mientras sea una fila valida y esa posicion este vacia
    while y in range(len(matriz)) and matriz[y][x] == 0:
        matriz[y][x] = sec
        sec += 1
        y += direccion
    y -= direccion

    direccion *= -1  # al final de un mov vertical se invierte la direccion

    # check disponibilidad cambio de mov
    if x in range(len(matriz[y])) and matriz[y][x + direccion] == 0:
        horizontal(matriz, sec, x + direccion, y, direccion)

# ------------------------- TP2.H) ------------------------------

def secEscalera(matriz, fila, col, sec, direc):
    '''Agrega los elementos de una matriz escalera en bajada
    
    parametros:
    matriz = matriz a modificar
    fila = fila en donde comienza la secuencia
    col = columna en donde comienza la secuencia
    sec = valor actual de la secuencia
    dir = direccion de la escalera -1 = baja, 1 = sube
    '''

    while fila in range(len(matriz)) and col in range(len(matriz[0])):
        matriz[fila][col] = sec
        sec += 1
        fila -= direc
        col += direc
    
    fila += direc
    col -= direc
    return fila, col, sec

def matrizEscalera(orden):
    '''Crea una matriz con una secuencia de numeros en donde los valores
    siguen una secuencia e incrementan siguiendo un patron de escalera
    '''
    matriz = matrizCuad(orden)

    primer_fila = 0
    primer_col = 0
    sec = 1

    while primer_fila < orden:
        foo, bar, sec = secEscalera(matriz, primer_fila, primer_col, sec, -1)
        if primer_col < len(matriz[0]) - 1:
            primer_col += 1
        else:
            primer_fila += 1
    
    return matriz

def matrizEscaleraBi(orden):
    '''Crea una matriz con una secuencia de numeros en donde los valores
    siguen una secuencia e incrementan siguiendo un patron de escalera
    bidireccional
    '''
    matriz = matrizCuad(orden)

    p_fila = 0
    p_col = 0
    sec = 1
    direc = 1

    while p_fila < orden and p_col < orden:
        p_fila, p_col, sec = secEscalera(matriz, p_fila, p_col, sec, direc)
        if p_fila == 0 or p_fila == (orden - 1):
            p_col += 1
        if (p_col == 0 or p_col == (orden - 1)) and p_fila in range(1, orden-1):
            p_fila += 1
        direc *= -1
    
    return matriz


# ------- Ej 3

def matrizRandomSinRep(orden):
    'Crea una matriz con elementos aleatorios sin repeticiones'

    matriz = matrizCuad(orden)
    disponibles = list(range(orden ** 2))

    for i in range(orden):
        for j in range(orden):
            agrega = disponibles.pop(randint(0, len(disponibles) - 1))
            matriz[i][j] = agrega

    return matriz
