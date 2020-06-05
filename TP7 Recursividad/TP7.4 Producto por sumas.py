'''
Desarrollar una función que devuelva el producto de dos números enteros
por sumas sucesivas
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

def producto_sumas(num1, num2):
    'Calcula la multiplicacion de dos numeros por medio de sumas consecutivas'
    if num2 == 1:
        return num1
    else:
        return num1 + producto_sumas(num1, num2 - 1)

def __main__():
    num1 = ingreso_entero()
    num2 = ingreso_entero()
    if num1 != None and num2 != None:
        producto = producto_sumas(num1, num2)
        print(f'\nEl resultado de {num1} * {num2} = {producto}')

if __name__ == "__main__":
    __main__()