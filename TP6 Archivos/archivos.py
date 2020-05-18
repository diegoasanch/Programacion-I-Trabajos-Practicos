from random import randint, sample

suma_matriz = lambda matriz: sum([sum([int(x) for x in fila]) for fila in matriz])
'Devuelve la suma de todos los elementos de una matriz'

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
                        n_linea += '\n'
                        break
                    n_linea += car
            else:
                n_linea = linea
        else: 
            n_linea = '\n'
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

def crear_datos_lluvia():
    '''Retorna una matriz con datos de lluvia simulados
    en formato fila = dia, mes, lluvia en mm
    '''
    matriz = []
    for _ in range(randint(50, 200)):
        mes = randint(1, 12)
        if mes == 2:
            max_dia = 28
        elif mes in [4, 6, 9, 11]:
            max_dia = 30
        else:
            max_dia = 31
        dia = randint(1, max_dia)
        lluvia = randint(0, 45)
        matriz.append([str(dia), str(mes), str(lluvia)])
    return sorted(matriz, key=lambda x: int(x[1])) # ordenada por mes

def escribir_matriz(data, archivo):
    '''Escribe los datos de una matriz en un archivo abierto pasado, cada
    fila es una linea y cada columna se separa por ";"
    '''
    for fila in data:
        archivo.write(';'.join(fila) + '\n')

def extrae_matriz(archivo, sep=';'):
    '''Extrae una matriz de un archivo, cada linea es una fila
    cada columna se separa con "sep"'''
    matriz = []
    for linea in archivo:
        matriz.append(linea.strip('\n').split(sep))
    return matriz

def ordena_matriz_mes(matriz):
    'Ordena la matriz para que cada columna sea un mes, y cada fila sean los dias'
    matriz_mes = [[0] * 12 for _ in range(31)]
    for fila in matriz:
        dia, mes, lluvia = map(int, fila)
        matriz_mes[dia - 1][mes - 1] = lluvia
    return matriz_mes

def imprime_matriz(archivo, missing='.', sep=5, screen=100):
    '''Imprime por pantalla una matriz extraida de un archivo
    
    Recibe Archivo para sacar la info
    opcional = missing (repr de dato faltante)
            separacion entre columnas, ancho de pantalla
    '''
    matriz = extrae_matriz(archivo)
    matriz_ord = ordena_matriz_mes(matriz)
    cols = len(matriz_ord[0])

    print('\n\n' + 'Reportaje de lluvias del año.'.center(screen))
    print('Columnas = mes, filas = dias, cada celda representa lluvia en mm.'.center(screen))
    print(f'"{missing}" representa 0 lluvia registrada.'.center(screen) + '\n')
    
    output = ''
    linea = ' '.center(sep)
    for i in range(cols): # Etiquetas de columnas (meses)
        linea += str(i + 1).center(sep)
    output += linea.center(screen) + '\n'
    output += ((' ' * sep) + ('-' * (sep * (cols)))).center(screen) + '\n'
    # Separador

    for i, fila in enumerate(matriz_ord):
        linea = ''
        linea += str(i + 1).center(sep-1) + '|' # Etiqueta de dia

        for item in fila:
            it = item
            if it == 0: # dia sin lluvia
                it = missing
            linea += str(it).center(sep) # Dato de lluvia
        output += linea.center(screen) + '\n'
    print(output)
    
    lluvia = suma_matriz(matriz_ord)
    print(f'La lluvia total del año fue de {lluvia}mm'.center(screen))
    
def clasifica_nombres(nombres):
    '''Retorna 3 listas con los nombres que pertenecen a los archivos ARMENIA,
    ITALIA Y ESPANIA respectivamente

    Recibe: nombre del archivo con nombres
    Retorna: 3 listas
    '''
    arm, ita, esp = [], [], []
    for nombre in nombres:
        termina = nombre.split(',')[0][-3:].lower() # Ultimas letras de apellido
        nomb = nombre.strip('\n')
        if  termina == 'ian':
            arm.append(nomb)
        elif termina == 'ini':
            ita.append(nomb)
        elif termina[-2:] == 'ez':
            esp.append(nomb)
    return arm, ita, esp

def escribir_lista(archivo, lista):
    'Escribe el contenido de lista representado como str en filename'        
    for nombre in lista:
        archivo.write(nombre + '\n')