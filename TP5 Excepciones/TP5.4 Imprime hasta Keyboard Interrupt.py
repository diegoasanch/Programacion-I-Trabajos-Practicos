'''
Todo programa Python es susceptible de ser interrumpido mediante la pulsación
de las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt.
Realizar un programa para imprimir los números enteros entre 1 y 100000, y
que solicite confirmación al usuario antes de detenerse cuando se presione
Ctrl-C.
'''

from excepciones import imprimeNums, ingresoNatural

def __main__():

    print('\nImprime los numeros enteros entre 1 y N')
    N = ingresoNatural('Ingrese un numero entero: ')
    if N != -1:
        print(f'\nA continuacion se imprimiran todos los numeros enteros\
entre 1 y {N}, para detener la impresion presione Ctrl-C')
        input('\n > Presione enter para comenzar.\n')
        imprimeNums(N)
    else:
        print('No ingreso ningun numero.')

if __name__ == "__main__":
    __main__()
