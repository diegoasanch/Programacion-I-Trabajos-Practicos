'''
Realizar una función que reciba como parámetros dos cadenas de caracteres
conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
'''

from excepciones import sumaCadenasNum

def __main__():

    cad1 = input('Ingrese un numero: ')
    cad2 = input('Ingrese otro numero: ')
    suma = sumaCadenasNum(cad1, cad2)
    if suma != -1:
        print(f'{cad1} + {cad2} = {suma}')
    else:
        print('Alguno de los parametros recibidos no es un numero real!')

if __name__ == "__main__":
    __main__()
