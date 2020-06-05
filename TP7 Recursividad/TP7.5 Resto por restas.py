'''
Realizar una función que devuelva el resto de dos números enteros, utilizando
restas sucesivas.
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

def resto_restas(num1, num2):
    'Calcula el resto de num1 entre num2 usando restas sucesivas recursivamente'
    if num1 < num2:
        return num1
    else:
        return resto_restas(num1 - num2, num2)

def __main__():

    num1 = ingreso_entero()
    num2 = ingreso_entero()
    if num1 != None and num2 != None:
        resto = resto_restas(num1, num2)
        print(f'\nEl resultado de {num1} % {num2} = {resto}')

if __name__ == "__main__":
    __main__()