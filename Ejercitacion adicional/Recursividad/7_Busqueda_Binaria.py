'''
Búsqueda Binaria: desarrollar un algoritmo para realizar un algoritmo de
búsqueda binaria en forma recursiva.
'''

import random

def busqueda(lista, elem, i=0, j=None):
    'Realiza busqueda binaria en una lista (ordenada obvio)'

    if j == None:
        j = len(lista) - 1
    medio = (i + j) // 2

    if lista[medio] == elem:
        return medio
    elif i == j:
        return -1

    if elem < lista[medio]:
        j = medio - 1
    else:
        i = medio + 1

    return busqueda(lista, elem, i, j)

def __main__():
    
    lista = sorted([random.randint(1, 235) for _ in range(random.randint(10, 30))])
    while True:
        try:
            print(lista)
            a_buscar = int(input('Ingrese un numero para buscar en la lista: '))
            pos = busqueda(lista, a_buscar)
            print()
            if pos != -1:
                print(f'El numero {a_buscar} se encuentra en la posicion {pos} de la lista.')
                break
            else:
                print(f'El numero {a_buscar} no se encuentra en la lista.')
        except ValueError:
            print('\nIngrese un numero valido.\n')


if __name__ == "__main__":
    __main__()
