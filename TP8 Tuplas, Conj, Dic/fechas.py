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