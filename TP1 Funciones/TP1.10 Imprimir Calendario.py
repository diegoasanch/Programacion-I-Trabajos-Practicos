"""
La siguiente función permite averiguar el día de la semana para una fecha 
determinada. La fecha se suministra en forma de tres parámetros enteros y 
la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc.
Escribir un programa para imprimir por pantalla el calendario de un mes 
completo, correspondiente a un mes y año cualquiera basándose en la función 
suministrada. Considerar que la semana comienza en domingo.
"""

from fechas import fecha_valida, ingreso_fecha, diadelasemana, diasiguiente

def imprimir_mes(mes, anio):
    'Imprime el calendario correspondiente a un mes y año recibidos'
    mes_og = mes
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    print(f'\t{meses[mes - 1]} de {anio}')

    dia = 1
    print('   Dom |  Lun |  Mar |  Mie |  Jue |  Vie |  Sab ')
    print('+===============================================+')
    while mes == mes_og:
        print('|', end='')
        for i in range(7):
            if diadelasemana(dia, mes, anio) == i and mes == mes_og:
                print(f'  {dia:02d}  |', end='')
                dia, mes, anio = diasiguiente(dia, mes, anio)
            else:
                print('      |', end='')
        print()
        print('+------+------+------+------+------+------+------+')
        
def main():

    print('Ingrese una fecha para mostrar su mes calendario correspondiente\n\n\n')

    dia, mes, anio = ingreso_fecha()
    while not fecha_valida(dia, mes, anio):
        print('\nFecha invalida!!\n')
        dia, mes, anio = ingreso_fecha()
    
    print()
    imprimir_mes(mes, anio)
    print()
    input('Presione enter para salir.')
    
    
if __name__ == "__main__":
    main()