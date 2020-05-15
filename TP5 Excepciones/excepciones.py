'Funciones para la resolucion del TP5 de Programacion I'

import math

def ingresoNatural(texto='Ingrese un numero natural: '):
    '''Valida el ingreso de un numero natural
    
    Controla las entradas invalidas utilizando manejo de excepciones
    '''
    while True:
        try:
            num = int(input(texto))
            1 / num

            if num == -1:
                raise KeyboardInterrupt
            elif num < 0:
                print('Debe ingresar un numero positivo!')
                continue  
            break

        except ValueError:
            print('Debe ingresar un numero entero!')
        except ZeroDivisionError:
            print('Debe ingresar un numero mayor a cero!')
        except KeyboardInterrupt:
            num = -1
            print()
            break
        except:
            print('Error no esperado!!')
            raise
    return num

def ingresaEntero(text='Ingrese un numero entero: ', errMsg='Debe ingrear un int.', escape=-1):
    'Valida el ingreso de un numero natural'

    while True:
        try:
            x = int(input(text))
            if x == escape:
                raise KeyboardInterrupt
            break
        except ValueError:
            print(f'\n{errMsg}')
        except KeyboardInterrupt:
            x = None
            break
    return x

def sumaCadenasNum(cad1, cad2):
    '''Recibe dos cadenas con numeros reales

    Si alguna de las cadenas tiene un caracter invalido, retorna -1
    '''
    try:
        a = float(cad1)
        b = float(cad2)
        num = a + b
    except ValueError:
        num = -1
    
    return num

def strmes(n):
    '''Devuelve un str del mes correspondiente a n
    en caso de no existir retorna cadena vacia
    '''
    meses = [
        'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
        'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
    ]

    try:
        mes = meses[n-1]
    except IndexError:
        mes = ''
    return mes

def opcion(texto='Si o no?: '):
    'Pregunta opcion, devuelve 1 para positivo, 0 para negativo, -1 para ninguna'
    si = ['si', 's', '1']
    no = ['no', 'n', '0']
    salir = ['salir', 'terminar', '-1']
    while True:
        op = input(texto).lower()
        if op in si:
            x = 1
            break
        elif op in no:
            x = 0
            break
        elif op in salir:
            x = -1
            break
        print('Opcion invalida! si, no o salir?\n')
    return x


def imprimeNums(N):
    'Imprime uno por uno los numeros enteros entre 1 y N'
    
    x = 1
    while True:
        try:
            for i in range(x, N+1):
                x = i
                print(i)
            else:
                print(f'Se imprimieron todos los numeros entre 1 y {N}')
                break
        except KeyboardInterrupt:
            print()
            salir = opcion('Desea abandonar la partida?: ')
            if salir:
                print('\n\nListado de numeros interrumpido!')
                break
            continue
    
def raizCuadrada(n):
    '''Calcula la raiz cuadrada de un numero usando math.sqrt
    
    Retorna -1 si n es negativo (invalido)
    '''
    try:
        raizcuad = math.sqrt(n)
    except ValueError:
        raizcuad = -1
    return raizcuad

def cargaLista(final=-1):
    'Carga una lista hasta que se ingrese el valor "final"'
    v = []
    while True:
        x = ingresaEntero(text='Ingrese un numero para cargar a la lista: ',
        errMsg=f'Debe ingresar un numero entero o {final} para salir.')
        if x == -1:
            break
        v.append(x)
    return v

def buscaNum(v, intentos=3):
    'Busca y devuelve la posicion de un numero en una lista, -1 si no esta'
    while True:
        try:
            n = ingresaEntero(text='Ingrese un numero para buscar: ')
            if n == -1:
                raise KeyboardInterrupt                
            pos = v.index(n)
            break
        except ValueError:
            if not intentos:
                print('No tiene mas intentos de busqueda.')
                break
            print(f'El elemento no esta en la lista. Quedan {intentos} intentos.')
            intentos -= 1
        except KeyboardInterrupt:
            print('Se interrumpio la busqueda!')
            pos = -1
            n = None
            break
    return pos, n
