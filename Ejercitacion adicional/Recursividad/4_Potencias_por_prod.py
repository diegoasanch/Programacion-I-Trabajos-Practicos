'''
Desarrollar una función recursiva para resolver exponente con
multiplicaciones sucesivas.
'''

def potencia(a, b):
    'Retorna a ** b'
    if b < 0:
        raise ValueError('No se aceptan numeros negativos.')
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * potencia(a, b-1)

def __main__():
    
    while True:

        print('\n\nCalcule a ^ b por multiplicaciones sucesivas.\n')

        try:
            num1 = int(input('Ingrese el valor de a: '))
            num2 = int(input('Ingrese el valor de b: '))
            pot = potencia(num1, num2)
        except ValueError as error:
            print(f'Error: {error}')
        else:
            print(f'{num1} elevado a la {num2} = {pot}')
            break

if __name__ == "__main__":
    __main__()

