'''
Escribir una función que indique si dos fichas de dominó encajan o no. Las
fichas son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función
devuelve True o False. Escribir también un programa para verificar su
comportamiento.
'''
def ingreso_natural(texto='Ingrese un numero natural: ', max=6):
    'Ingresa un numero entero valido o None'
    while True:
        try:
            num = int(input(texto))
            if num == -1:
                raise KeyboardInterrupt
            if num not in range(-1, max + 1):
                raise ValueError(f'* Caracter invalido, debe ingresar un ' + \
                'numero entero positivo menor a {max} o -1 para salir.')
            break
        except ValueError as error:
            print(error)
    return num

def encajan(ficha1, ficha2):
    'Determina si las fichas de domino encajan entre ellas'
    a, b = ficha1
    return a in ficha2 or b in ficha2

def ingreso_domino():
    'Ingresa una ficha de domino valida'
    dom = ()
    for i in range(2):
        dom += ingreso_natural(texto='Ingrese un valor de domino: ', max=6),
    return dom


def __main__():

    try:
        print('Ingrese la ficha 1')
        ficha1 = ingreso_domino()
        print('Ingrese la ficha 2')
        ficha2 = ingreso_domino()
        print(f'Fichas ingresadas: {ficha1} - {ficha2}')
        if encajan(ficha1, ficha2):
            print('Las piezas encajan.')
        else:
            print('Las piezas no encajan.')
    except KeyboardInterrupt:
        print('Abandono el programa')


if __name__ == "__main__":
    __main__()