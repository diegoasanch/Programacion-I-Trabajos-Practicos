from random import randint, sample

suma_matriz = lambda matriz: sum([sum([int(x) for x in fila]) for fila in matriz])
'Devuelve la suma de todos los elementos de una matriz'

promedio = lambda lista: sum(lista) / len(lista)
'Devuelve el promedio de una lista de numeros'

def elimina_comentarios(archivo):
    'Elimina los comentarios de un archivo .py'
    com = '#'
    comillas = '"'+"'"
    nuevo = []

    for linea in archivo:
        n_linea = ''
        l_stripped = linea.strip()

        if l_stripped != '':
            if l_stripped[0] in com + comillas:
                continue
            if com in linea:
                str_abierto = False
                for car in linea:
                    if car in comillas:
                        str_abierto = not str_abierto
                    if car == com and not str_abierto:
                        break
                    n_linea += car
            else:
                n_linea = linea
        nuevo.append(n_linea)
    return nuevo
                
def opcion(texto='Si o no?: '):
    'Pregunta opcion, devuelve 1 para positivo, 0 para negativo'
    si = ['si', 's', '1']
    no = ['no', 'n', '0']
    while True:
        op = input(texto).lower()
        if op in si:
            x = 1
            break
        elif op in no:
            x = 0
            break
        print('Opcion invalida! si, no o salir?\n')
    return x 

def escribe_csv(archivo, linea):
    '''Escribe en formato csv (separado con coma) los elementos de la
    lista linea como una linea unica en archivo
    '''
    archivo.write(','.join(linea) + '\n')

def clasifica_nombres(nombres, final):
    '''Clasifica los nombres del archivo nombres que terminen con el str final
    Recibe: nombres = archivo con nombres abierto ,final: letras finales del
            grupo de nombres a seleccionar
    Retorna: lista con nombres filtrados
    '''
    ult = len(final) * (-1)
    clasf = []
    for nombre in nombres:
        termina = nombre.split(',')[0][ult:].lower() # Ultimas letras de apellido
        nomb = nombre.strip('\n')
        if  termina == final:
            clasf.append(nomb)
    return clasf

def escribir_lista(archivo, lista):
    'Escribe el contenido de lista representado como str en filename'        
    for nombre in lista:
        linea = nombre
        if linea[-1:] != '\n':
            linea += '\n'
        archivo.write(linea)

def isFloat(n):
    'Determina si el numero n puede convertirse a float'
    esflo = True
    try:
        float(n)
    except ValueError:
        esflo = False
    return esflo

def GrabarRangoAlturas(archivo, fin=''):
    '''Graba en un archivo las distintas disciplinas deportivas
    y la altura de cada uno de sus atletas
    
    Recibe: archivo a escribir abierto en modo "w"
    '''
    cargando = True
    datos = []
    while cargando:
        deporte = input('Ingrese el nombre del deporte: ')
        datos.append(deporte)
        print('\n - Ingrese las estaturas de los atletas para finalizar ingrese un campo vacio.\n')
        while True:
            atleta = input('Ingrese la estatura del atleta: ').replace(',','.')
            if atleta == fin:
                break
            if not isFloat(atleta):
                print('Estatura invalida!')
                continue
            datos.append(atleta)
        cargando = opcion('\nDesea cargar otro deporte?: ')
    
    escribir_lista(archivo, datos)

def IntercalaDepPromedio(deportes, estaturas):
    '''Retorna una lista con los deportes y el promedio de las estaturas
    
    Recibe: 
        - deportes = lista con nombres de deportes
        - estaturas = matriz con las estaturas de los atletas, cada posicion
          de fila corresponde con un deporte en la lista deportes
    '''
    lista = []
    for i, estatura in enumerate(estaturas):
        lista.append(deportes[i])
        lista.append(str(round(promedio(estatura), 2)))
    return lista

def GrabarPromedio(datos, archivo):
    '''Extrae la altura promedio por diciplina del archivo datos
    y la graba en el archivo archivo
    
    Recibe: datos = archivo de datos de deportes abierto en modo "r"
            archivo = archivo a escribir los promedios abierto en modo "w"
    '''
    deportes = []
    estaturas = []
    i = -1
    for linea in datos:
        reg = linea.strip('\n')
        if not isFloat(reg):
            deportes.append(reg)
            estaturas.append([])
            i += 1
        else:
            estaturas[i].append(float(reg))
    proms = IntercalaDepPromedio(deportes, estaturas)
    escribir_lista(archivo, proms)

def MostrarMasAltos(promedios):
    '''Imprime por pantalla las disciplinas que tienen una estatura promedio
    por encima del promedio general
    
    Recibe: promedios = archivo con los promedios de estatura por deporte
            abierto en modo "r"
    '''
    proms = []
    deps = []
    for linea in promedios:
        reg = linea.strip('\n')
        if isFloat(reg):
            proms.append(float(reg))
        else:
            deps.append(reg)
    promedio_general = promedio(proms)
    print(f'El promedio general de altura es de {round(promedio_general, 2)} m\n')

    for i, prom in enumerate(proms):
        if prom > promedio_general:
            print(f' - El deporte {deps[i]} sobrepasa el promedio general con un promedio de {prom} m')


            