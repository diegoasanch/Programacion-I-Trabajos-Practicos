'''
Escribir una función filtrar_palabras() que reciba una cadena de caracteres
conteniendo una frase y un entero N, y devuelva otra cadena con las palabras
que tengan N o más caracteres de la cadena original. Escribir también un
programa para verificar el comportamiento de la misma. Hacer tres versiones
de la función, para cada uno de los siguientes casos:
    a.Utilizando sólo ciclos normales
    b.Utilizando listas por comprensión
    c.Utilizando la función filter
'''

from cadenas import ingresaNum, filtrar_palabrasCiclos, filtrar_palabrasComp, filtrar_palabrasFilt

def __main__():

    print('Filtrar palabras, a continuacion ingrese una frase y separado con un espacio'\
        '\ningrese la longitud para filtrar las palabras.\n')
    frase = input('Ingrese su frase: ')
    print('Ingrese la longitud: ', end='')
    N = ingresaNum()
    filt1 = filtrar_palabrasCiclos(frase, N)
    filt2 = filtrar_palabrasComp(frase, N)
    filt3 = filtrar_palabrasFilt(frase, N)

    if filt1 != '':
        print('\nPor medio de ciclos comunes.')
        print(filt1)
        print('\nPor comprension de listas.')
        print(filt2)
        print('\nPor filter().')
        print(filt3)
        
    else:
        print('No se pudo filtrar ninguna palabra')

if __name__ == "__main__":
    __main__()
