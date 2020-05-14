'''
Escribir un programa que permita ingresar una cadena de caracteres e imprima
un mensaje indicando cuántas letras y cuántos números contiene. Por ejemplo,
si se ingresa "Hola Mundo 123" debe indicar que se ingresaron 9 letras y 3
números.
'''

from cadenas import cuentaCar

def __main__():
    cadena = input('Ingrese su cadena para contar letras y numeros: ')
    letras, nums = cuentaCar(cadena)
    print(f'Su cadena contiene {letras} letras y {nums} numeros.')

if __name__ == "__main__":
    __main__()
    