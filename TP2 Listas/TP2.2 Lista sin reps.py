'''
Escribir funciones para:
    a.Generar una lista de 50 números aleatorios del 1 al 100.
    b.Recibir una lista como parámetro y devolver True si la misma
       contiene algún elemento repetido. La función no debe modificar la lista.
    c.Recibir una lista como parámetro y devolver una nueva lista con los 
       elementos únicos de la lista original, sin importar el orden. 
Combinar estas tres funciones en un mismo programa.
'''
from random import randint
from listas import cargaRandom, listasinReps, repetidos


def main():

    lista = cargaRandom(N=50)
    print(f'Lista original: {lista}\n')
    if repetidos(lista):
        new = listasinReps(lista)
        print(f'Lista sin reps: \n{new}')
    else:
        print('La lista original no contiene repetidos!')

if __name__ == "__main__":
    main()