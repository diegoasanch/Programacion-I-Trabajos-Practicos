'''
Realizar una función recursiva para imprimir una matriz de M x N.
'''
from random import randint

def imprimir_matriz(matriz, i=0, espaciado=3):
    'Imprime una matriz recursivamente'
    if type(matriz[i]) == list:
        imprimir_matriz(matriz[i])
        print()
    else:
        print(str(matriz[i]).center(espaciado), end='')
    if i < len(matriz) - 1:
            imprimir_matriz(matriz, i + 1)

def __main__():
    x = randint(2, 20)
    matriz = [[randint(0, 20) for _ in range(x)] for _ in range(x)]
    try:
        imprimir_matriz(matriz)
    except RecursionError:
        print('La matriz no se pudo imprimir completo debido a que supero el limite de recursion de python.')

if __name__ == "__main__":
    __main__()