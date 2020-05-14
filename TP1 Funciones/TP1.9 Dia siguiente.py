'''
Escribir una función diasiguiente(…) que reciba como parámetro una 
fecha cualquiera expresada por tres enteros (correspondientes al día,
mes y año) y calcule y devuelva tres enteros correspondientes el día
siguiente al dado. Utilizando esta función, desarrollar programas
que permitan:
    a. Sumar N días a una fecha.
    b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
'''

def es_bisiesto(anio):
    'Determina si un año es bisiesto o no'

    if anio % 4 == 0:
        if anio % 100 == 0:
            return anio % 400 == 0
        return True
    return False


def diasiguiente(dia, mes, anio):
    '''Calcula el dia siguiente
    pre = dia, mes, anio correspondientes a una fecha valida
    '''

    m_30 = [4, 6, 9, 11]

    if mes == 2:
        dias = 28
        if es_bisiesto(anio):
            dias = 29
    elif mes in m_30:
        dias = 30
    else:
        dias = 31

    if dia < dias:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            anio += 1
        else: 
            mes += 1

    return dia, mes, anio


def suma_dias():
    'Suma dias a una fecha ingresada'

    dia, mes, anio = [int(x) for x in input('Ingrese la fecha en el formato dd,mm,aaaa: ').split(',')]
    a_sumar = int(input('Ingrese la cantidad de dias a sumar: '))

    while a_sumar < 0 and a_sumar != -1:
        print('\nCantidad a sumar invalida! Ingrese un numero positivo')
        a_sumar = int(input('Ingrese la cantidad de dias a sumar: '))

    for _ in range(a_sumar):
        dia, mes, anio = diasiguiente(dia, mes, anio)

    print(f'\nNueva fecha: {dia}/{mes}/{anio}')


def dias_entre(d1, m1, y1, d2, m2, y2):
    'Calcula la diferencia de dias entre dos fechas'
    
    dias = 0
    while (d1 != d2) or (m1 != m2) or (y1 != y2):
        dias += 1
        d1, m1, y1 = diasiguiente(d1, m1, y1)
    return dias


def diferencia_fechas():
    dia, mes, anio = [int(x) for x in input('Ingrese la fecha1 en el formato dd,mm,aaaa: ').split(',')]
    dia2, mes2, anio2 = [int(x) for x in input('Ingrese la fecha2 en el formato dd,mm,aaaa: ').split(',')]

    print(f'\nFecha1: {dia}/{mes}/{anio}')
    print(f'Fecha2: {dia2}/{mes2}/{anio2}\n')

    diferencia = dias_entre(dia, mes, anio, dia2, mes2, anio2)
    print(f'Hay {diferencia} dias entre fecha1 y fecha2')


def new_screen():
    print('\n' * 30)


def reintentar():
    try:
        op = int(input('Menu 1, salir 0: '))
    except:
        return reintentar()
    return op


def main():

    while True:
        new_screen()
        print('Calculos con fechas\n')
        print('\n- 1. Sumar dias a una fecha\n- 2. Calcular diferencia entre fechas\n')
        op = int(input('> Ingrese una opcion: '))

        while op not in range(1,3) and op != -1:
            new_screen()
            print('\nOpcion invalida!\n')
            print('\n- 1. Sumar dias a una fecha\n- 2. Calcular diferencia entre fechas\n')
            op = int(input('> Ingrese una opcion: '))

        new_screen()
        if op == 1:
            print('Suma de dias a una fecha\n\n\n')
            suma_dias()
        elif op == 2:
            print('Diferencia entre fechas\n\n\n')
            diferencia_fechas()
        
        print()
        if reintentar():
            continue
        break


if __name__ == "__main__":
    main()