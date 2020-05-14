'''
Crear una lista con los cuadrados de los números entre 1 y N
(ambos incluidos), donde N se ingresa desde el teclado. Luego 
se solicita imprimir los últimos 10 valores de la lista
'''
from listas import listaCuadrados


def main():

    print('Crear una lista con los cuadrados de los números entre 1 y N\n')

    N = int(input('Ingrese el valor de N: '))

    lista = listaCuadrados(N)
    print('Ultimos elementos de la lista:')
    print(lista[-10:])

if __name__ == "__main__":
    main()