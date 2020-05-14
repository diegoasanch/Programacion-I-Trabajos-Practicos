'''
Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
según la fecha sea correcta o no. Realizar también un programa para verificar el
comportamiento de la función.
'''
def es_bisiesto(anio):
    'Determina si un año es bisiesto o no'
    
    if anio % 4 == 0:
        if anio % 100 == 0:
            return anio % 400 == 0
        return True
    return False


def fecha_valida(dia, mes, anio):
    'Determina la validez de una fecha segun el calendario gregoriano'

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


def main():
    dia = int(input('Ingrese el dia: '))
    mes = int(input('Ingrese el mes: '))
    anio = int(input('Ingrese el año: '))
    print()

    fecha = f'{dia}/{mes}/{anio}'

    if fecha_valida(dia, mes, anio):
        print(fecha + ' es una fecha valida')
    else:
        print(fecha + ' es una fecha invalida')


if __name__ == '__main__':
    main()
    