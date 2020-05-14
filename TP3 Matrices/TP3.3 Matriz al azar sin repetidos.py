'''
Desarrollar un programa para rellenar una matriz de N x N con
números enteros al azar comprendidos en el intervalo [0,N2), de
tal forma que ningún número se repita. Imprimir la matriz por
pantalla.
'''

from crear_matrices import matrizCuad, matrizRandomSinRep
from matrices import imprimirMatriz

def __main__():
    print('Rellenar una matriz de NxN con numeros enteros al azar [0, n^2) sin repetidos')
    N = int(input('Ingrese el valor de N: '))
    matriz = matrizRandomSinRep(N)
    print('\n\n- Matriz generada:\n')
    imprimirMatriz(matriz)
    input('\n   >Presione Enter para salir.')

if __name__ == "__main__":
    __main__()
