'''
Desarrollar una función que devuelva una cadena de caracteres con el nombre
del mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la
función. Devolver una cadena vacía si el número de mes es inválido. La
detección de meses inválidos deberá realizarse a través de excepciones.
'''

from excepciones import strmes, ingresoNatural

def __main__():

    numero = ingresoNatural(texto='Ingrese el numero del mes: ')
    if numero != -1:
        mes = strmes(numero)
        print()
        if mes != '':
            print(f'El mes {numero} es {mes}')
        else:
            print('No se ingreso un numero de mes valido!')
    else:
        print('\n\n\nSe forzo la salida del programa!')

if __name__ == "__main__":
    __main__()
