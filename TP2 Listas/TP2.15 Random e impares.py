'''
Generar una lista con números al azar entre 1 y 100 y crear
una nueva lista con los elementos de la primera que sean
impares. El proceso deberá realizarse utilizando listas por
comprensión. Imprimir las dos listas por pantalla. 
'''

from random import randint
from listas import cargaRandom, soloimpares
    
def main():
    n = randint(1, 100)
    listarand = cargaRandom(N=n)
    listarandimp = soloimpares(listarand)
    # listarandimp =  list(filter(lambda x: x % 2 != 0, listarand))  # Just for fun
    print('\nLista original:', listarand)
    print('\nElementos impares de la lista original:', listarandimp)

if __name__ == "__main__":
    main()