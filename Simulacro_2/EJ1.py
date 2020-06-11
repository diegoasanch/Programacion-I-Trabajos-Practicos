'''
Se solicita leer el archivo de frases “frases.txt” y crear uno nuevo que
contenga una palabra por registro, debe ser la palabra más larga pero sin
considerar letras repetidas. Si alguna frase tiene más de una palabra más
larga, es suficiente con guardar sólo una de ellas. No se permite cargar
por completo el archivo de frases en memoria. Por ejemplo:
    Registro: “Bello es mejor que feo” Palabra más larga: mejor
    Resolver utilizando excepciones y creando al menos dos funciones.
    No se aceptan funciones que sólo cumplen una acción o instrucción,
    debe resolver correctametne un subproblema.
'''

def palabra_mas_larga(linea):
    'devuelve la palabra mas larga'
    mas_larga = ''
    for palabra in linea.split():
        if len(set(palabra)) > len(set(mas_larga)):
            mas_larga = palabra
    return mas_larga

def extrae_mas_largas(archivo1, archivo2):
    '''
    Extrae de las lineas de archivo1 la palabra mas larga de cada registro
    y la graba en archivo2
    '''
    try:
        ar1 = open(archivo1, 'r')
        ar2 = open(archivo2, 'w')
    except FileNotFoundError:
        print('No se pudo abrir el archivo')
    else:
        for linea in ar1:
            mas_larga = palabra_mas_larga(linea) # max(linea.split(), key=lambda palabra: len(set(palabra)))
            ar2.write(mas_larga + '\n')
        ar1.close()
        ar2.close()

def __main__():

    filename = 'frases.txt'
    filename2 = 'palabras.txt'
    extrae_mas_largas(filename, filename2)

if __name__ == "__main__":
    __main__()