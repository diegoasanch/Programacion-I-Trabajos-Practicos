'''
Archivo 1: todos los campos son de longitud fija

Pérez Juan       20080211 Corrientes 348
González Ana M   20080115 Juan de Garay 1111 3er piso dto A
'''

def transfiereDatosF1(origen, destino):
    '''
    Transfiere los datos de empleados del archivo escrito con el formato 1
    (longitud fija) del archivo origen al archivo destino en formato csv
    
    Recibe ambos archivos abiertos
    '''
    for linea in origen:
        datos = [linea[:16], linea[17:26], linea[26:]]
        for i, dato in enumerate(datos):
            datos[i] = dato.strip() # limpieza de espacios vacios
        destino.write(','.join(datos) + '\n')

def __main__():
    
    try:
        origen = open("archivo1.txt", "r")
        destino = open("empleados1.csv", "w")
    except IOError:
        print('Ocurrio un error al abrir los archivos.')
    else:
        transfiereDatosF1(origen, destino)
        origen.close()
        destino.close()

if __name__ == "__main__":
    __main__()
