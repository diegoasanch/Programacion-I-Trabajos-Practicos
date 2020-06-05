'''
Escribir un programa que permita grabar un archivo los datos de lluvia
caída durante un año. Cada línea del archivo se grabará con el siguiente
formato:<dia>;<mes>;<lluvia caída en mm>  por ejemplo  25;5;319
Los datos se generarán mediante números al azar, asegurándose que las fechas
sean válidas. La cantidad de registros también será un número al azar entre
50 y 200. Por último se solicita leer el archivo generado e imprimir un
informe en formato matricial donde cada columna represente a un mes y cada
fila corresponda a los días del mes. Imprimir además el total de lluvia
caída en todo el año.
'''
from random import randint

suma_matriz = lambda matriz: sum([sum([int(x) for x in fila]) for fila in matriz])
'Devuelve la suma de todos los elementos de una matriz'

def fechaRandom():
    'Retorna dia y mes validos'
    mes = randint(1, 12)
    if mes == 2:
        max_dia = 28
    elif mes in [4, 6, 9, 11]:
        max_dia = 30
    else:
        max_dia = 31
    dia = randint(1, max_dia)
    return dia, mes

def crear_datos_lluvia():
    '''Retorna una matriz con datos de lluvia simulados
    en formato fila = dia, mes, lluvia en mm
    '''
    matriz = []
    for _ in range(randint(50, 200)):
        dia, mes = fechaRandom()
        lluvia = randint(0, 300)
        matriz.append([str(dia), str(mes), str(lluvia)])
    return sorted(matriz, key=lambda x: int(x[1])) # ordenada por mes

def escribir_matriz(data, filename):
    '''Escribe los datos de una matriz en un archivo pasado, cada
    fila es una linea y cada columna se separa por ";"
    '''
    try:
        archivo = open(filename, 'w')
    except FileNotFoundError:
        raise IOError(f'El archivo {filename} no esxiste en la ubicacion definida')
    else:
        for fila in data:
            archivo.write(';'.join(fila) + '\n')
        archivo.close()

def extrae_matriz(filename, sep=';'):
    '''Extrae una matriz de un archivo, cada linea es una fila
    cada columna se separa con "sep"'''
    try:
        archivo = open(filename, 'r')
    except FileNotFoundError:
        raise IOError(f'El archivo {filename} no esxiste en la ubicacion definida')
    else:
        matriz = []
        for linea in archivo:
            matriz.append(linea.strip('\n').split(sep))
        archivo.close()
    return matriz

def ordena_matriz_mes(matriz):
    'Ordena la matriz para que cada columna sea un mes, y cada fila sean los dias'
    matriz_mes = [[0] * 12 for _ in range(31)]
    for fila in matriz:
        dia, mes, lluvia = map(int, fila)
        matriz_mes[dia - 1][mes - 1] += lluvia
    return matriz_mes

def imprime_matriz(matriz_ord, missing='.', sep=5, screen=100):
    '''Imprime por pantalla una matriz extraida de un archivo
    
    Recibe Archivo para sacar la info
    opcional = missing (repr de dato faltante)
            separacion entre columnas, ancho de pantalla
    '''
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

def __main__():
    
    try:
        filename = 'rain_data.txt'
        
        datos_lluvia = crear_datos_lluvia()
        escribir_matriz(datos_lluvia, filename)
        matriz = extrae_matriz(filename)
        matriz_ord = ordena_matriz_mes(matriz)
        imprime_matriz(matriz_ord)

    except IOError as error:
        print(f'Ocurrio un error: {error}')
        print('Verifique su existencia e intente de nuevo.')

if __name__ == "__main__":
    __main__()
