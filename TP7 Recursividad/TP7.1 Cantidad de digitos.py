'''
Escribir una función que devuelva la cantidad de dígitos de un número
entero, sin utilizar cadenas de caracteres
'''

def ingreso_entero(texto='Ingrese un numero entero: '):
    'Ingresa un numero entero valido o None'
    while True:
        try:
            num = int(input(texto))               
            break
        except ValueError:
            print('* Caracter invalido, debe ingresar un numero entero.')
        except KeyboardInterrupt:
            num = None
            break
    return num

def cant_digitos(num):
    'Cuenta la cantidad de digitos en numero recursivamente'
    if num in [0, -1]:
        return 0
    else:
        return 1 + cant_digitos(num // 10)

def __main__():
    
    num = ingreso_entero()
    if num != None:
        digs = cant_digitos(num)
        print(f'\nEl numero {num} tiene {digs} digitos.')

if __name__ == "__main__":
    __main__()
