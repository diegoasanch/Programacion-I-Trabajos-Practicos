'''
Desarrollar una función para reemplazar todas las apariciones de una
palabra por otra en una cadena de caracteres y devolver la cadena
obtenida y un entero con la cantidad de reemplazos realizados. Escribir
también un programa para verificar el comportamiento de la función.
'''

from cadenas import reemplazaPal

def __main__():

    print('Reemplazo de palabras en una cadena de caracteres.')
    cadena = input('Ingrese la cadena: ')
    print()
    if cadena != '':
        print('Ingrese la palabra original y la nueva palabra separada por un espacio:', end='')
        vieja, nueva = input().split()
        print()
        if vieja != '':
            nueva_cad, veces = reemplazaPal(cadena, vieja, nueva)
            print(f'\nSe reemplazo la palabra "{vieja}" por "{nueva}", {veces} veces dentro del str.')
            print(f'\nNuevo str: {nueva_cad}')
        else:
            print('No se puede reemplazar una palabra vacia :(')
    else:
        print('No se ingreso ningun texto :(')

if __name__ == "__main__":
    __main__()
