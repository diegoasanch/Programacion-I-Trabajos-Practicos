'''
Desarrollar una función que devuelva una subcadena con los últimos N
caracteres de una cadena dada. La cadena y el valor de N se pasan
como parámetros.
'''

from cadenas import ingresaNum, ultimosN

def __main__():
    
    cadena = input('Ingrese una cadena de caracteres: ')
    print('Ingrese la longitud de la subcadena a extraer: ', end='')
    N = ingresaNum()
    if N != -1:
        subcadena = ultimosN(cadena, N)
        print(f'Los ultimos {N} caracteres de su cadena son: \n{subcadena}')
    else:
        print('No ingreso una longitud valida :(')

if __name__ == "__main__":
    __main__()
