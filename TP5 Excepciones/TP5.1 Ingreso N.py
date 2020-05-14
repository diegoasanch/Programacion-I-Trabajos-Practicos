'''
Desarrollar una función para ingresar a través del teclado un número
natural. La función rechazará cualquier ingreso inválido de datos
utilizando excepciones y mostrará la razón exacta del error. Controlar
que se ingrese un número, que ese número sea entero y que sea mayor que 0.
Devolver el valor ingresado cuando éste sea correcto. Escribir también un
programa que permita probar el correcto funcionamiento de la misma.
'''

from excepciones import ingresoNatural

def __main__():

    print('Prueba de la funcion para ingresar un numero entero, manejando excepciones')
    num = ingresoNatural()
    print()
    if num != -1:
        print(f'El numero recibido fue {num}')
    else:
        print('\nSe forzo la salida del programa, no se recibio ningun numero.')

if __name__ == "__main__":
    __main__()
