'''
Escribir una función que reciba un número entero N y devuelva un diccionario
con la tabla de multiplicar de N del 1 al 12. Escribir también un programa
para probar la función
'''

def ingreso_natural(texto='Ingrese un numero natural: '):
    'Ingresa un numero natural o -1'
    while True:
        try:
            num = int(input(texto))
            if num < -1:
                raise ValueError('* Caracter invalido, debe ingresar un ' + \
                'numero entero positivo o -1 para salir.')
            break
        except ValueError as error:
            print(error)
    return num

def tabla_mult(num, hasta=12):
    'Crea un diccionario con la tabla de multiplicar de 1 a 12 de num'
    tabla = {}
    for i in range(hasta):
        tabla[i+1] = num * (i+1)
    return tabla

def imprime_tabla(dic):
    'Imprime la tabla de multiplicar recibida como diccionario'
    num = dic[1]
    for clave in sorted(dic.keys()):
        print(f'{num} * {clave} = {dic[clave]}')

def __main__():

    num = ingreso_natural('Ingrese un numero para calcular su tabla de multiplicar: ')
    if num >= 0:
        tabla = tabla_mult(num)
        imprime_tabla(tabla)
    else:
        print('No ingreso ningun numero.')


if __name__ == "__main__":
    __main__()