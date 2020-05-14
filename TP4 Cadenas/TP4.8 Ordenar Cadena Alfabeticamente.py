'''
Escribir una función que reciba como parámetro una cadena de caracteres
en la que las palabras se encuentran separadas por uno o más espacios.
Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando
un espacio entre cada una.
'''
from cadenas import ordenarAlfCadena

def __main__():

    cadena = input('Ingrese una cadena de caracteres: ')
    cadena_alf = ordenarAlfCadena(cadena)
    print(f'Su cadena de caracteres ordenada alfabeticamente es:\n{cadena_alf}')

if __name__ == "__main__":
    __main__()
