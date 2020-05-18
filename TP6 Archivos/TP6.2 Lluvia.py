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

from archivos import crear_datos_lluvia, escribir_matriz, imprime_matriz

def __main__():
    
    try:
        datos_lluvia = crear_datos_lluvia()
        filename = 'rain_data.txt'
        archivo = open(filename, 'w+')
        escribir_matriz(datos_lluvia, archivo)
        archivo.close()

        archivo = open(filename, 'r')
        imprime_matriz(archivo)
        archivo.close()
        

    except FileNotFoundError:
        print(f'El archivo {filename} no esxiste en la ubicacion definida')
        print('Verifique su existencia e intente de nuevo.')
    # finally:
    #     if archivo != None:

if __name__ == "__main__":
    __main__()