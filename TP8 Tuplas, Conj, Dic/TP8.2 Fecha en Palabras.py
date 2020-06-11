'''
Escribir una función que reciba como parámetro una tupla conteniendo una
fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha
expresada en formato extendido. Por ejemplo, para (12,10,17) devuelve
"12 de Octubre de 2017". Escribir también un programa para verificar su 
comportamiento.
'''

from fechas import ingresa_fecha, fecha_valida

def fecha_a_str(fecha):
    '''
    Devuelve una fecha valida representada en str
    Si no es valida, raise ValueError
    '''
    meses = [
        'enero', 'febrero', 'marzo', 'abril',
        'mayo', 'junio', 'julio', 'agosto',
        'septiembre', 'octubre', 'noviembre', 'diciembre'
    ]
    fecha_valida(fecha)
    dia, mes, anio = fecha
    return f'{dia} de {meses[mes-1].capitalize()} de {anio}'

def __main__():

    fecha = ingresa_fecha()
    fecha_str = fecha_a_str(fecha)
    print(fecha_str)

if __name__ == "__main__":
    __main__()