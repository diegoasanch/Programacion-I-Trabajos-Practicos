'''
Generar dos listas con M y N números al azar entre 1 y 50 y
construir una tercera lista cuyos elementos sean el resultado
de la intersección de las dos listas dadas. Los valores de M
y N se obtienen al azar. Imprimir las tres listas por pantalla.
'''

from random import randint
from listas import cargaRandom, intersec


def main():
    M = randint(1, 50)
    N = randint(1, 50)
    listaM = cargaRandom(M, 1, 50)
    listaN = cargaRandom(N, 1, 50)
    print('Lista M:', listaM)
    print('Lista N:', listaN)
    MyN = intersec(listaM, listaN)
    print('Interseccion de las listas M y N:', MyN)

if __name__ == "__main__":
    main()
    