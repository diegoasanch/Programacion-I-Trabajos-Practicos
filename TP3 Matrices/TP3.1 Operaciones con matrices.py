'''
Desarrollar cada una de las siguientes funciones y escribir
un programa que permi-ta verificar su funcionamiento, 
imprimiendo la matriz luego de invocar a cada función'''

from matrices import *

def __main__():

    # a. Cargar numeros enteros en una matriz NxN
    print(' -a) Carga de matriz')
    Matriz = cargarMatrizCuad(5)
    print('\nMatriz Cargada:')
    imprimirMatriz(Matriz)
    continuar()


    # b. Ordenar de forma ascendente las filas de la matriz
    ordenarFilas(Matriz)
    print('\n -b) Matriz con filas ordenadas:')
    imprimirMatriz(Matriz)
    continuar()


    # c. Intercambiar dos filas, cuyos numeros se reciben como parametro
    print('\n -c) Intercambio de filas\n')

    fila1 = ingresarFila(Matriz)
    fila2 = ingresarFila(Matriz)
    intercambiarFilas(Matriz, fila1, fila2)
    print()
    imprimirMatriz(Matriz)
    continuar()

    
    # d. Intercambiar dos columnas, cuyos numeros se reciben como parametro
    print('\n -d) Intercambio de columnas\n')

    columna1 = ingresarColumna(Matriz)
    columna2 = ingresarColumna(Matriz)
    intercambiarColumnas(Matriz, columna1, columna2)
    print()
    imprimirMatriz(Matriz)
    continuar()


    # e. Intercambiar una fila por una columna, cuyos numeros de reciben como parametro
    print('\n -e) Intercambio de fila por columna\n')

    fila = ingresarFila(Matriz)
    columna = ingresarColumna(Matriz)
    intercambiarFilaCol(Matriz, fila, columna)
    print(f'\nMatriz con la fila {fila} y columna {columna} intercambiadas\n')
    imprimirMatriz(Matriz)
    continuar()


    # f. Tansponer la matriz sobre si misma (intercambiar cada elemento Aij por Aji)
    print('\n -f) Transponer la matriz\n')

    transponer(Matriz)
    imprimirMatriz(Matriz)
    continuar()


    # g. Calcular el promedio de los elementos de una fila, cuyo numero se recibe como parametro
    print('\n -g) Calculo del promedio de los elementos de una fila\n')
    
    fila = ingresarFila(Matriz)
    prom = promedioFila(Matriz, fila)
    print(f'\nEl promedio de la fila {fila} es {prom}')
    continuar()


    # h. Calcular el porcentaje de elementos con valor impar en una columna, cuyo numero se recibe como parametro
    print('\n -h) Calculo del porcentaje de los elementos impares de una columna\n')
    
    col = ingresarColumna(Matriz)
    porc = porcentajeImparCol(Matriz, col)
    print(f'\nEl porcentaje de elementos impares en la columna {col} es de {porc:.1f} %\n')
    continuar()


    # i. Determinar si la matriz es simetrica con respecto a su diagonal principal
    print(' -i) Simetria Diagonal Principal\n')
    if esSimetrica(Matriz):
        print('La matriz es simetrica respecto a su diagonal principal!!')
    else:
        print('La matriz no es simetrica respecto a su diagonal principal :(')
    print()
    continuar()


    # j. Determinar si la matriz es simetrica con respecto a su diagonal secundaria
    print(' -j) Simetria Diagonal Secundaria\n')
    if esSimetricaSec(Matriz):
        print('La matriz es simetrica respecto a su diagonal secundaria!!')
    else:
        print('La matriz no es simetrica respecto a su diagonal secundaria :(')   
    print()
    continuar()


    # k. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con los números de las mismas.
    col_palind = columnasPalindromo(Matriz)
    print(' -k) Columnas Palindromo\n')
    if col_palind != []:
        print(f'Las columnas {col_palind} de la matriz son palindromo!')
    else:
        print('La matriz no tiene ninguna columna palindromo :(')
    print()

    input('Presione enter para salir.')

if __name__ == "__main__":
    __main__()