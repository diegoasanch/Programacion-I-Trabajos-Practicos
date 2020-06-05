'''
Desarrollar una función que reciba un número binario y lo devuelva convertido a base decimal.
'''

def ingreso_entero(texto='Ingrese un numero entero: '):
    'Ingresa un numero entero valido o None'
    while True:
        try:
            num = int(input(texto))
            if num < 0:
                raise ValueError
            break
        except ValueError:
            print('* Caracter invalido, debe ingresar un numero entero positivo.')
        except KeyboardInterrupt:
            num = None
            break
    return num

def bin_a_int(binario, pos=0):
    'Convierte un numero binario a entero recursivamente'
    if binario == 0:
        return 0
    else:
        return ((binario % 10) * (2**pos)) + bin_a_int(binario // 10, pos + 1)

def __main__():

    binario = ingreso_entero()
    if binario != None:
        entero = bin_a_int(binario)
        print(f'El numero binario {binario} es {entero} en base 10.')

if __name__ == "__main__":
    __main__()
