'''
Desarrollar las siguientes funciones utilizando tuplas para representar fechas
y horarios, y luego escribir un programa para verificar su comportamiento:

    a.Ingresar una fecha desde el teclado, verificando que corresponda a 
      una fecha válida.
    b.Sumar N días a una fecha.
    c.Ingresar un horario desde teclado, verificando que sea correcto.
    d.Calcular la diferencia entre dos horarios. Si el primer horario
      fuera mayor al segundo se considerará que el primero corresponde al
      día anterior. En ningún caso la diferencia en horas puede superar 
      las 24 horas.
'''
tuple_str = lambda cont, sep: sep.join(map(str, cont))
'Imprime un tuple separado por sep'

min_total = lambda hora: (hora[0] * 60) + hora[1]
'Devuelve el valor absoluto en minutos de una tupla (hh, mm)'

min_a_hora = lambda mins: ((mins // 60), (mins % 60))
'Convierte minutos a tupla (hh, mm)'

def ingreso_natural(texto='Ingrese un numero natural: '):
    'Ingresa un numero entero valido o None'
    while True:
        try:
            num = int(input(texto))
            if num == -1:
                raise KeyboardInterrupt
            if num < -1:
                raise ValueError('* Caracter invalido, debe ingresar un ' + \
                'numero entero positivo 0 -1 para salir.')
            break
        except ValueError as error:
            print(error)
    return num

def ingresa_separados(texto, cant, separador):
    '''
    Devuelve los valores numericos de un ingreso separado por separador
    ej: ingreso= 20/4/2020 separador= "/" --> 20, 4, 2020
        ingreso= 04:20 separador= ":" --> 4, 20
    '''
    try:
        fecha = tuple(map(int, input(texto).split(separador)))
        if len(fecha) != cant:
            raise ValueError
    except ValueError:
        raise ValueError(f'Debe ingresar {cant} valores numericos separados por "{separador}"')
    return fecha

def es_bisiesto(anio):
    'Determina si un año es bisiesto'
    es_bi = False
    if not anio % 4:
        if not anio % 100:
            if not anio % 400:
                es_bi = True
        else:
            es_bi = True
    return es_bi

def dias_en_mes(mes, anio):
    'Devuelve cuantos dias tiene el mes valido "mes"'
    if mes == 2:
        if es_bisiesto(anio):
            dias = 29
        else:
            dias = 28
    elif mes in (4, 6, 9, 11):
        dias = 30
    else:
        dias = 31
    return dias

def fecha_valida(fecha):
    'Determina si una fecha es valida, de no serlo : raise ValueError'
    dia, mes, anio = fecha
    if mes in range(1, 13):
        dias = dias_en_mes(mes, anio)
        if dia not in range(1, dias + 1):
            raise ValueError(f'Dia {dia} invalido en un mes de {dias} dias.\n')
    else:
        raise ValueError(f'Mes invalido "{mes}".')

def ingresa_fecha():
    'Devuelve una tupla en formato (Dia, Mes, Año) validados'
    while True:
        try:
            fecha = ingresa_separados('Ingresa la fecha en formato d/m/a: ', 3, r'/')
            fecha_valida(fecha)
            break
        except ValueError as error:
            print(f'\n\nFecha invalida: {error}')
    return fecha

def hora_valida(horario):
    'Determina si una hora es valida, de no serlo : raise ValueError'
    hora, minuto = horario
    if hora not in range(24) or minuto not in range(60):
        raise ValueError(f'Hora invalida {hora}:{minuto}')

def ingresa_hora():
    'Devuelve una tupla en formato (hora, minuto) validada'
    while True:
        try:
            hora = ingresa_separados('Ingresa la hora en formato hh:mm : ', 2, r':')
            hora_valida(hora)
            break
        except ValueError as error:
            print(f'\n\nHora invalida: {error}')
    return hora

def suma_dias(fecha, dias):
    'Devuelve tupla (dia, mes, año) con la fecha fecha + dias'
    dia, mes, anio = fecha
    dias_m = dias_en_mes(mes, anio)
    for _ in range(dias):
        if dia < dias_m:
            dia += 1
        else:
            if mes < 12:
                mes += 1
                dia = 1
            else:
                dia, mes = 1, 1
                anio += 1
            dias_m = dias_en_mes(mes, anio)
    return (dia, mes, anio)

def diferencia_horas(hora1, hora2):
    'Calcula la diferencia entre dos horas'

    abs_1, abs_2 = min_total(hora1), min_total(hora2)
    # abs_n = tiempo absoluto en minutos
    if abs_1 < abs_2:
        dif = abs_2 - abs_1
    else:
        dif = (24 * 60) - abs_1 + abs_2
    return min_a_hora(dif)

def __main__():
    try:
        fecha = ingresa_fecha()
        print(f"Ingreso la fecha {tuple_str(fecha, sep='/')}")

        a_sumar = ingreso_natural('\nIngrese la cantidad de dias a sumar: ')
        if a_sumar:
            nueva_fecha = suma_dias(fecha, a_sumar)
            print(f"Nueva fecha fecha {tuple_str(nueva_fecha, sep='/')}")
        
        print('A continuacion ingrese dos horas para calcular su diferencia.')
        hora1 = ingresa_hora()
        hora2 = ingresa_hora()
        horas, minutos = diferencia_horas(hora1, hora2)
        print(f'La diferencia de horario es de {horas}hs y {minutos}min')


    except KeyboardInterrupt:
        print('Ha abandonado el programa.')

if __name__ == "__main__":
    __main__()
