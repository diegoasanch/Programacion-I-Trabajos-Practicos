'''
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la
raíz cuadrada de un número cualquiera ingresado a través del teclado. El
programa debe utilizar manejo de excepciones para evitar errores si se ingresa
un número negativo.
'''
from math import sqrt
from excepciones import opcion

def raizCuadrada():
    'Calcula la raiz cuadrada de un numero usando math.sqrt'

    while True:
        try:
            n = int(input('Ingrese un numero entero: '))
            if n == -1:
                print('Debe ingresar un numero positivo.\n')
                if opcion('Desea salir?: '):
                    raizcuad = -1
                    break
            raizcuad = sqrt(n)
            break
        except ValueError:
            print('Debe ingresar un numero entero positivo\n')
    if n != -1:
        print(f'\nLa raiz cuadrada de {n} es {raizcuad}')
    else:
        print('Forzo la salida del programa.')

def __main__():

    print('\nCalculo de la raiz cuadrada de un numero\n')
    raizCuadrada()

if __name__ == "__main__":
    __main__()
