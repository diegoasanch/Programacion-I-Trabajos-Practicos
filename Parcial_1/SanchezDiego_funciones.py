'''
modulo para la resolucion del Parcial 1
Diego Sánchez
'''

from random import randint

extraeDia = lambda semana, dia: [semana[fab][dia] for fab in range(len(semana))]
'Retorna una lista correspondiente a la columna "dia" de la matriz "semana"'

esPar = lambda num: num % 2 == 0

produccionImparLista = lambda lista: [prod for prod in lista if not esPar(prod)]
'Retorna una lista con los elementos impares de la lista recibida'

def imprimirSemana(matriz):
    'imprime la matriz por pantalla'
    for num, fila in enumerate(matriz):
        print(f'Fabrica {num + 1}: ', end='')
        for col in fila:
            print(str(col).center(3,' '), end='  ')
        print()

def produccionImparMatriz(matriz):
    'Retorna una lista con los elementos impares de la matriz recibida'
    lista = []
    for fila in matriz:
        lista += produccionImparLista(fila)
    return lista


def ingresoIntPositivo():
    '''Recibe y valida un numero positivo por teclado
    En caso de no recibir nada devuelve -1
    '''

    escape = ['fin', 'salir', '']
    num = input('Ingrese un numero positivo: ')
    while not num.isdigit() and num.lower() not in escape:
        print('Debe ingresar un entero positivo o "fin" para salir')
        num = input('Ingrese un numero positivo: ')
    if num.isdigit():
        num = int(num)
    else:
        num = -1
    return num

def crearSemana(cant, cap_max=150):
    '''Crea y devuelve una matriz de 6 columnas (dias de la semana) lun-sab
    y "cant" filas (fabricas). Cada item corresponde a la cantida de 
    bicicletas fabricadas ese dia/fabrica
    '''
    semana = []
    for fabrica in range(cant):
        semana.append([])
        for dia in range(6):
            prod = randint(0, cap_max)
            prod = prod // 2 if dia == 5 else prod # si es sabado
            semana[fabrica].append(prod)
    return semana

def diaMasProductivos(semana):
    'Retorna una lista con los dias mas prod'
    
    dias_productivos = []
    mayor_prod = 0
    for dia in range(len(semana[0])):
        prod_dia = sum(extraeDia(semana, dia)) #suma de la columna dia
        if prod_dia > mayor_prod:
            mayor_prod = prod_dia
            dias_productivos = [dia]
        elif prod_dia == mayor_prod:
            dias_productivos.append(dia)

    return dias_productivos
    
def reporteProductividad(semana, dias):
    'Imprime por pantalla un reporte de los mejores dias de produccion'

    dias_sem = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    mayor_prod = sum(extraeDia(semana, dias[0]))
    print(f'La mayor produccion diaria fue de {mayor_prod} bicicletas!')
    
    for dia in dias:
        print(f'Dia {dias_sem[dia].title()}:')
        for num, fabrica in enumerate(semana):
            print(f'\tFabrica {num + 1} - produjo {fabrica[dia]} bicicletas')

def listaTriangInf(matriz):
    'Devuelve una lista con los elementos de la diagonal inferior de "matriz"'
    lista = []
    if len(matriz) == len(matriz[0]): # si es cuadrada
        for i in range(len(matriz)):
            for j in range(i):
                lista.append(matriz[i][j])
    return lista
