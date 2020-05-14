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

ejs = {
    'a': matrizDiagImpar, 'b': matrizDiagSec, 'c': matrizTriangInf, 'd': filasPotencia2,
    'e': matrizCadaImpar, 'f': trianInferiorInv, 'g': matrizEspiral, 'h': matrizEscalera,
    'i': matrizEscaleraBi
    }
    
items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

def __main__():
    print('TP3 Matrices, Ejercicio 2')
    N = int(input('Ingrese el tamaño de orden de las matrices: '))
    
    for item in items:
        print(f'\n\titem {item})\n')
        mat = ejs[item](N)
        imprimirMatriz(mat)
        continuar()

if __name__ == "__main__":
    __main__()