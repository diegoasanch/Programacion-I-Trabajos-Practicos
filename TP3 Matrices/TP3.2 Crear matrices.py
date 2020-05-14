'''
Para cada una de las siguientes matrices, desarrollar una
función que la genere y escribir un programa que invoque a
cada una de ellas y muestre por pantalla la matriz obtenida.
El tamaño de las matrices debe establecerse como N x N, y
las funciones deben servir aunque este valor se modifique.
'''

from crear_matrices import matrizDiagImpar, matrizDiagSec, matrizTriangInf, filasPotencia2
from crear_matrices import matrizCadaImpar, trianInferiorInv, matrizEspiral, matrizEscalera, matrizEscaleraBi
from matrices import imprimirMatriz, continuar

def __main__():
    print('TP3 Matrices, Ejercicio 2')
    N = int(input('Ingrese el tamaño de orden de las matrices: '))
    
    # a.
    print('\n\titem a)\n')
    a = matrizDiagImpar(N)
    imprimirMatriz(a)
    continuar()

    # b.
    print('\n\titem b)\n')
    b = matrizDiagSec(N)
    imprimirMatriz(b)
    continuar()

    # c.
    print('\n\titem c)\n')
    c = matrizTriangInf(N)
    imprimirMatriz(c)
    continuar()

    # d.
    print('\n\titem d)\n')
    d = filasPotencia2(N)
    imprimirMatriz(d)
    continuar()

    # e.
    print('\n\titem e)\n')
    e = matrizCadaImpar(N)
    imprimirMatriz(e)
    continuar()

    # f.
    print('\n\titem f)\n')
    f = trianInferiorInv(N)
    imprimirMatriz(f)
    continuar()

    # g.
    print('\n\titem g)\n')
    g = matrizEspiral(N)
    imprimirMatriz(g)
    continuar()

    # h.
    print('\n\titem h)\n')
    h = matrizEscalera(N)
    imprimirMatriz(h)
    continuar()

    # i.
    print('\n\titem i)\n')
    i = matrizEscaleraBi(N)
    imprimirMatriz(i)
    input('Presione enter para salir...')


if __name__ == "__main__":
    __main__()