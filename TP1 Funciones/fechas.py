'Funciones para los ejercicos de del TP1 de Programacion I'

def es_bisiesto(anio):
    'Determina si un año es bisiesto o no'
    
    if anio % 4 == 0:
        if anio % 100 == 0:
            return anio % 400 == 0
        return True
    return False


def fecha_valida(dia, mes, anio):
    '''
    Determina la validez de una fecha segun el calendario gregoriano
    
    recibe: dia, mes, año
    '''

    m_30 = [4, 6, 9, 11]
    valida = True
    if mes > 12:
        valida = False
    elif  mes == 2 and not (dia <= 28 or (es_bisiesto(anio) and dia == 29)):
        valida = False
    elif mes in m_30 and dia > 30:
        valida = False
    elif dia > 31:
        valida = False
    
    return valida

def mesSiguiente(mes, anio, mov=1):
    '''
    Calcula el mes siguiente/anterior a una fecha dada

    recibe = mes, anio correspondientes a una fecha valida
    mov = movimiento. mes siguiente = 1, mes anterior = -1
    '''

    if mes in range(2,12):
        mes += mov

    elif mes == 12:
        if mov == 1:
            mes = 1
            anio += 1
        else:
            mes += mov
    elif mes == 1:
        if mov == 1:
            mes += mov
        else:
            mes = 12
            anio -= 1

    return mes, anio

def diasiguiente(dia, mes, anio):
    '''
    Calcula el dia siguiente a una fecha dada

    recibe = dia, mes, anio correspondientes a una fecha valida
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

def suma_dias(dia, mes, anio, diasaSumar):
    '''
    Suma dias a una fecha ingresada

    recibe: dia, mes, anio de una fecha previamente verificada
    
    diasaSumar: numero entero positivo
    '''

    for _ in range(diasaSumar):
        dia, mes, anio = diasiguiente(dia, mes, anio)

    return dia, mes, anio


def dias_entre(d1, m1, y1, d2, m2, y2):
    '''
    Calcula la diferencia de dias entre dos fechas

    recibe: 
        fecha uno = d1, m1, y1
        fecha dos = d2, m2, y2

    IMPORTANTE: enviar fecha 1 <= fecha 2
    '''
    
    dias = 0
    while (d1 != d2) or (m1 != m2) or (y1 != y2):
        dias += 1
        d1, m1, y1 = diasiguiente(d1, m1, y1)
    return dias

def ingreso_fecha():
    '''
    Ingresa por teclado una fecha en formato dd,mm,aaaa

    devuelve: dia, mes, anio
    '''
    dia, mes, anio = [int(x) for x in input('Ingrese la fecha en el formato dd,mm,aaaa: ').split(',')]
    return dia, mes, anio


def diadelasemana(dia,mes,anio):
    '''
    Determina el dia de la semana de una fecha Valida

    recibe: dia, mes, año VALIDOS

    devuelve: 0 = dom, 1 = lun, 2 = mar, 3 = mie, 4 = jue, 5 = vie, 6 = sab
    '''
    
    if mes < 3:
        mes += 10
        anio -= 1
    else:
        mes -= 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = ((( 26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + ( siglo // 4) - (2 * siglo)) % 7
    
    if diasem < 0:
        diasem += 7
    
    return diasem

def armarCalendario(mes, anio):
    'Devuelve un string con el calendario correspondiente a un mes y año recibidos'
    dia = 1
    mes_og = mes
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    text = f'  {meses[mes - 1]} de {anio}\n\n'
    text += '   Dom |  Lun |  Mar |  Mie |  Jue |  Vie |  Sab \n' 
    text += '+================================================+\n'

    while mes == mes_og:
        text += '|'
        for i in range(7):
            if diadelasemana(dia, mes, anio) == i and mes == mes_og:
                text += f'  {dia:02d}  |'
                dia, mes, anio = diasiguiente(dia, mes, anio)
            else:
                text += '      |'
        text += '\n+------+------+------+------+------+------+------+\n'
    
    return text