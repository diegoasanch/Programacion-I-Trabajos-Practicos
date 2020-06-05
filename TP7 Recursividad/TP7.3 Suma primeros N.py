'''
Escribir una función que devuelva la suma de los N primeros números naturales.
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

def suma_primeros_n(num):
    'Devuelve la suma de los primeros num numeros naturales'
    if not num:
        return 0
    else:
        return num + suma_primeros_n(num - 1)

def __main__():
    
    num = ingreso_entero()
    if num != None:
        suma = suma_primeros_n(num)
        print(f'\nLa suma de los primeros {num} numeros naturales es {suma}')

if __name__ == "__main__":
    __main__()