'''
Definir una función superposición() que reciba como parámetros
dos listas de cualquier tipo y devuelva True si tienen al menos
un elemento en común, o False en caso contrario. Desarrollar un
programa para verificar su comportamiento.
'''
from random import randint
from listas import cargaRandom, superposicion

def main():
    cant = int(input('Ingrese la cantidad de elementos: '))
    lista1 = cargaRandom(cant)
    lista2 = cargaRandom(cant)
    print(f'lista 1: {lista1}')
    print(f'lista 2: {lista2}')
    if superposicion(lista1, lista2):
        print('Las listas tienen elementos en comun')
    else:
        print('Las listas no comparten ningun item en comun')

if __name__ == "__main__":
    main()
