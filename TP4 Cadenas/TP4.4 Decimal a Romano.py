'''
Escribir una función que reciba como parámetro un número entero entre 0
y 3999 y lo convierta en un número romano, devolviéndolo en una cadena
de caracteres. ¿En qué cambiaría la función si el rango de valores fuese
diferente?
'''

from cadenas import ingresaNumRango, intRomano

def __main__():

    print('Convierte numeros entre 1 y 3999 a Romano')
    minimo, maximo = 1, 3999
    num = ingresaNumRango(minimo, maximo)
    print()
    if num != -1:
        rom = intRomano(num)
        print(f'El numero {num} en romano es: {rom}')
    else:
        print(r'Hasta la próxima ¯\_(ツ)_/¯')

if __name__ == "__main__":
    __main__()
