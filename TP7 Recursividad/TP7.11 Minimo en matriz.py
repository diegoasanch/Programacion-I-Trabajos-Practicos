'''
Desarrollar una función que devuelva el elemento de valor mínimo de una
matriz de M x N.
'''
from TP7_9_Imprimir_Matriz import imprimir_matriz
from random import randint

def menor_en_matriz(matriz, i=0):
    'Devuelve el menor valor de una matriz recursivamente'
    if type(matriz[0]) == list:
        if i < len(matriz) - 1:
            return min(menor_en_matriz(matriz[i]), menor_en_matriz(matriz, i + 1))
        else:
            return menor_en_matriz(matriz[i])
    else:
        return min(matriz)

def __main__():
    x = randint(2, 20)
    matriz = [[randint(1, 99) for _ in range(x)] for _ in range(x)]
    try:
        print('Matriz: ')
        imprimir_matriz(matriz)
        menor = menor_en_matriz(matriz)
        print(f'\nMenor elemento de la matriz: {menor}')
    except RecursionError:
        print('La matriz no se pudo imprimir completo debido a que supero el limite de recursion de python.')

if __name__ == "__main__":
    __main__()
