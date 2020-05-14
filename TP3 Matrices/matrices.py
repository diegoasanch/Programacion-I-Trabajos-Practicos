from random import randint

def imprimirMatriz(matriz):
    '''muestra una matriz por pantalla.'''

    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end=" ")
        print()

def cargarMatrizCuad(N=3):
    'Carga una matriz de NxN con numeros ingresados por teclado'

    M = []
    for fila in range(N):
        M.append([])
        for col in range(N):
            # num = int(input('Ingrese un numero: '))
            num = randint(1, 99)
            M[fila].append(num)
    return M

def mayor_en(matriz):
    'Devuelve el valor maximo dentro de la matriz'

    mayor = 0
    for row in matriz:
        mayor_local = max(row)
        if mayor_local > mayor:
            mayor = mayor_local
    return mayor

def ordenarFilas(matriz):
    'Ordena en forma ascendente cada una de las filas de una matriz'
    for fila in matriz:
        fila.sort()

def ingresarFila(matriz):
    'Solicita por teclado y valida un numero de fila dentro de una matriz'

    filas = len(matriz)
    fila = int(input('Ingrese el numero de la fila: '))

    while fila not in range(filas):
        print('Numero de fila invalido! :(')
        fila = int(input('Ingrese el numero de la fila: '))
    return fila

def intercambiarFilas(matriz, fila1, fila2):
    'Intercambia en matriz la fila1 con la fila2'

    aux = matriz[fila1]
    matriz[fila1] = matriz[fila2]
    matriz[fila2] = aux

def ingresarColumna(matriz):
    'Solicita por teclado y valida un numero de columna dentro de una matriz'

    columnas = len(matriz[0])
    columna = int(input('Ingrese el numero de la columna: '))

    while columna not in range(columnas):
        print('Numero de columna invalido! :(')
        columna = int(input('Ingrese el numero de la columna: '))
    return columna

def intercambiarColumnas(matriz, col1, col2):
    'Intercambia en matriz la columna1 con la columna2'
    for fila in matriz:
        aux = fila[col1]
        fila[col1] = fila[col2]
        fila[col2] = aux

def intercambiarFilaCol(matriz, fila, columna):
    'Intercambia en matriz fila por columna'

    for i in range(len(matriz[fila])):
        aux = matriz[fila][i]
        matriz[fila][i] = matriz[i][columna]
        matriz[i][columna] = aux

def transponer(matriz):
    'Transpone una matriz sobre si misma'
    
    for i in range(len(matriz)):
        for j in range(i, len(matriz[0])):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux

def promedioFila(matriz, fila):
    'Calcula el promedio de la fila numero fila de la matriz'

    promedio = sum(matriz[fila]) / len(matriz[fila])
    return promedio

def porcentajeImparCol(matriz, col):
    'Calcula el porcentaje de elementos con valor impar en una columna'

    total = 0
    for fila in matriz:
        if fila[col] % 2 != 0:
            total += 1
    
    porcentaje = (total / len(matriz)) * 100
    return porcentaje

def esSimetrica(matriz):
    'Determina si una matriz cuadrada es simetrica respecto a su Diagonal principal'

    simetrica = True
    i = 0
    n = len(matriz)
    while i < n and simetrica:
        j = i
        while j < n and simetrica:
            if matriz[i][j] != matriz [j][i]:
                simetrica = False
            j += 1
        i += 1
    return simetrica

def esSimetricaSec(matriz):
    'Determina si una matriz es simetrica respecto a su Diagonal secundaria'
    
    matriz_rev = [fila[::-1] for fila in matriz]
    return esSimetrica(matriz_rev)

def esCapicua(lista):
    'determina si una lista cualquiera es capicua'
    capicua = lista == lista[::-1]
    return capicua

def columnasPalindromo(matriz):
    '''Determina que columnas de matriz son capicua
    
    Devuelve lista con los numeros de las columnas
    '''
    palinds = []
    for col in range(len(matriz[0])):
        columna = [matriz[x][col] for x in range(len(matriz))]

        if esCapicua(columna):
            palinds.append(col)

    return palinds

def continuar():
    input('\n\t>Presione enter para continuar\n')
    print('\n' * 4)
