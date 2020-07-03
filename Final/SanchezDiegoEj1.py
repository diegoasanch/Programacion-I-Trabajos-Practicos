"""
Realice una función para mostrar las posiciones que ocupa un carácter en una
cadena. Deberá informar TODAS las posiciones en las cuales aparece el caracter.
Resolver utilizando rebanadas y funciones de cadenas.
"""


def encuentra_caracter(cadena, caracter):
    """
    Devuelve lista con las posiciones que ocupa 'caracter' dentro de 'cadena'
    De no pertenecer a la cadena -->  raise KeyError
    """
    if caracter not in cadena:
        raise KeyError(f'El caracter "{caracter}" no pertenece a la cadena recibida')
    
    else:
        posiciones = []
        pos = 0
        while caracter in cadena[pos:]:

            pos = cadena.find(caracter, pos)
            posiciones.append(pos)
            pos += 1

    return posiciones


def imprime_posiciones(posiciones):
    """
    Imprime las posiciones los items de la lista 'posiciones'
    """
    for posicion in posiciones:
        print(f' - {posicion}')


def __main__():
    
    cadena = input('Ingrese una cadena de caracteres: ')

    while True:
        try:
            caracter = input('\nIngrese un caracter para buscar sus posiciones dentro de la cadena: ')
            if not caracter:
                raise KeyboardInterrupt

            posiciones = encuentra_caracter(cadena, caracter)

            print(f'\nEl caracter "{caracter}" se encuentra en la cadena en las posiciones:')
            imprime_posiciones(posiciones)
        
        except KeyError as error:
            print(f'\n** Error: {error}.')
        
        except KeyboardInterrupt:
            print('\n\nHa abandonado el programa.')
            break


if __name__ == "__main__":
    __main__()
