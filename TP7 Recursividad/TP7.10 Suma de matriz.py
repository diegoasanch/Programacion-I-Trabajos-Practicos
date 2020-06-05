'''
Escribir una función que sume todos los elementos de una matriz de M x N y
devuelva el resultado.
'''
from TP7_9_Imprimir_Matriz import imprimir_matriz
from random import randint

def suma_matriz(matriz, i=0):
    'Devuelve la suma total de una matriz recursivamente'
    if i > len(matriz) - 1:
        return 0
    elif type(matriz[i]) == list:
        return suma_matriz(matriz[i]) + suma_matriz(matriz, i + 1)
    else:
        return matriz[i] + suma_matriz(matriz, i + 1)

def __main__():
    x = randint(2, 20)
    matriz = [[randint(0, 20) for _ in range(x)] for _ in range(x)]
    try:
        print('Matriz: ')
        imprimir_matriz(matriz)
        suma = suma_matriz(matriz)
        print(f'\nSuma total de la matriz: {suma}')
    except RecursionError:
        print('La matriz no se pudo imprimir completo debido a que supero el limite de recursion de python.')

if __name__ == "__main__":
    __main__()