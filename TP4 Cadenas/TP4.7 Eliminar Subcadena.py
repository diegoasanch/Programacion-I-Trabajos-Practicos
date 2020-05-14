'''
Escribir una función para eliminar una subcadena de una cadena de 
caracteres, a partir de una posición y cantidad de caracteres dadas,
devolviendo la cadena resultante. Escribir también un programa para
verificar el comportamiento de la misma. Escribir una función para cada
uno de los siguientes casos:
    a.Utilizando rebanadas 
    b.Sin utilizar rebanadas
'''

from cadenas import eliminaSubCadena, eliminaSubCadena2, ingresaNum

def __main__():

    cadena = input('Ingrese una cadena de caracteres: ')
    print('Ingrese la posicion: ', end='')
    pos = ingresaNum()
    if pos != -1:
        print('Ingrese la longitud de la subcadena a elim: ', end='')
        long = ingresaNum()
        nueva_cad = eliminaSubCadena(cadena, pos, long)
        print(f'\nLa nueva cadena obtenida es: {nueva_cad}')
    else:
        print('\nNo ingreso una posicion valida. :(')

if __name__ == "__main__":
    __main__()
