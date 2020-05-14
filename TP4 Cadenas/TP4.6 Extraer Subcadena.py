'''
Desarrollar una función que extraiga una subcadena de una cadena de
caracteres, indicando la posición y la cantidad de caracteres deseada.
Devolver la subcadena como valor de retorno. Escribir también un programa
para verificar el comportamiento de la misma. Ejemplo, dada la cadena
"El número de teléfono es 4356-7890" extraer la subcadena que comienza en
la posición 25 y tiene 9 caracteres, resultando la subcadena "4356-7890".
Escribir una función para cada uno de los siguientes casos:
    a. Utilizando rebanadas 
    b. Sin utilizar rebanadas
'''

from cadenas import extraeSubCadena, extraeSubCadena2, ingresaNum

def __main__():

    cadena = input('Ingrese una cadena de caracteres: ')
    print('Ingrese la posicion: ', end='')
    pos = ingresaNum()
    if pos != -1:
        print('Ingrese la longitud de la subcadena: ', end='')
        long = ingresaNum()
        subcadena = extraeSubCadena(cadena, pos, long)
        print(f'\nLa subcadena obtenida es: {subcadena}')
    else:
        print('\nNo ingreso una posicion valida. :(')

if __name__ == "__main__":
    __main__()
