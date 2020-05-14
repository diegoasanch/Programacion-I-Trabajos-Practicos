'''
Una persona desea llevar el control de los gastos realizados al viajar 
en el subterráneo dentro de un mes. Sabiendo que dicho medio de transporte 
utiliza un esquema de tarifas decrecientes (detalladas en la tabla de
abajo) se solicita desarrollar una función que reciba como parámetro la 
cantidad de viajes realizados en un determinado mes y devuelva el total
gastado en viajes. Realizar también un programa para verificar el 
comportamiento de la función.
'''

def calcula_gasto_mensual(viajes, tarifa):
    
    if viajes in range(0, 21):
        return viajes * tarifa

    elif viajes in range(21, 31):
        return ((viajes - 20) * 0.8) * tarifa + calcula_gasto_mensual(20, tarifa)

    elif viajes in range(31, 41):
        return ((viajes - 30) * 0.7) * tarifa + calcula_gasto_mensual(30, tarifa)

    else:
        return ((viajes - 40) * 0.6) * tarifa + calcula_gasto_mensual(40, tarifa)


def main():

    print('Calculador de gastos mensuales en subte!\n')
    tarifa = float(input('Ingrese la tarifa de viaje: $'))
    viajes = int(input('Ingrese la cantidad de viajes en el mes: '))

    viajes = viajes if viajes >= 0 else -viajes
    total = calcula_gasto_mensual(viajes, tarifa)

    print(f'\n\tEl total mensual es de ${total:.2f}')


if __name__ == "__main__":
    main()
