'''
Programacion I, Parcial 1
Diego Sánchez, legajo: 1121456
'''

from SanchezDiego_funciones import *

def __main__():

    fabricas = ingresoIntPositivo()
    if fabricas > 0:
        semana = crearSemana(fabricas)
        print('Produccion de la semana:')
        imprimirSemana(semana)
        print()
        mejores_dias = diaMasProductivos(semana)
        print()
        reporteProductividad(semana, mejores_dias)
        print()

        elem_trian = listaTriangInf(semana)
        if elem_trian != []:
            print('La matriz semana tiene triangular inferior, los impares se buscaran ahi')
            prod_impar = produccionImparLista(elem_trian)
        else:
            print('La matriz no tiene matriz triangular inferior, se buscaran los'\
            '\nelementos impares en toda la semana')
            prod_impar = produccionImparMatriz(semana)

        if prod_impar == []:
            print('Todos los dias se fabricaron una cantidad par de bicicletas.')
        else:
            print(f'\nSe fabricaron una cantidad impar de bicicletas {len(prod_impar)} veces')
    else:
        print('\nSin fabricas no hay produccion :(')

if __name__ == "__main__":
    __main__()
