'''
Desarrollar una función recursiva que devuelva la cantidad de dígitos de un
número entero, sin utilizar cadenas de caracteres:
    a) Modificar el algoritmo visto en clase para que logre contar dígitos
      en forma recursiva tanto para valores positivos y negativos.
    b) Resolver con cadenas de caracteres
'''

cant_dig2 = lambda num: len(str(num).strip('-'))

def cant_dig(num):
    'Devuelve la cantidad de numeros de un numero entero'
    if num < 0:
        num *= -1
    if num > 0:
        return 1 + cant_dig(num // 10)
    else:
        return 0

def __main__():
    
    num = int(input('Ingrese un numero entero: '))
    cant = cant_dig(num)
    cant2 = cant_dig2(num)
    print(f'La cantidad de digitos de {num} es {cant}')
    print(f'La cantidad de digitos de {num} es {cant2}')

if __name__ == "__main__":
    __main__()
