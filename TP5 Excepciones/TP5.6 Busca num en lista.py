'''
El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando
con -1) y permita que el usuario ingrese el valor de algunos elementos para
visualizar la posición que ocupan, utilizando el método index. Si el número
no pertenece a la lista se imprimirá un mensaje de error y se solicitará otro
para buscar. Abortar el proceso al tercer error detectado. No utilizar el
operador in durante la búsqueda.
'''

from excepciones import ingresaEntero, cargaLista, buscaNum, opcion

def __main__():
    print('A continuacion cargue una lista con numeros enteros.\n')
    lista = cargaLista()
    if lista != []:
        print('\nA continuacion ingrese numeros para buscar su posicion\n')
        while True:
            pos, n = buscaNum(lista)
            if pos != -1:
                print(f'El elemento {n} se encuentra en la posicion {pos} de la lista.')
            else:
                print('No se pudo concretar la busqueda.')

            if not opcion('Desea buscar otro numero?: '):
                break
            print()

    else:
        print('No se cargo ningun elemento!')

if __name__ == "__main__":
    __main__()
