'''
Escribir un programa que cuente cuántas veces se encuentra una subcadena
dentro de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en
cuenta que los caracteres de la subcadena no necesariamente deben estar en
forma consecutiva dentro de la cadena, pero sí respetando el orden de los
mismos.
'''

from cadenas import cuentaSubCadena

def __main__():
    print('Cuenta las apariciones de una subcadena dentro de una cadena de caracteres')
    cadena = input('Ingrese la cadena original: ')
    
    if cadena != '':
        subcadena = input('Ingrese la subcadena a buscar: ')
        if subcadena != '':
            apariciones =  cuentaSubCadena(cadena, subcadena)
            if apariciones:
                print(f'La subcadena {subcadena} se encuentra'\
                    f'\n{apariciones} veces dentro de la cadena original')
            else:
                print('La subcadena no aparece ninguna vez dentro de la cadena original :(')
        else:
            print('No se ingreso ninguna cadena a buscar.')
    else:
        print('No se puede buscar dentro de una cadena vacia.')

if __name__ == "__main__":
    __main__()
