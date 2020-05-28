'''
Archivo 2: Los campos estan separados por el signo #

Pérez Juan#20080211#Corrientes 348
González Ana M#20080115#Juan de Garay 1111 3er piso Dto A
'''

def transfiereDatosF2(origen, destino):
    '''
    Transfiere los datos de empleados del archivo escrito con el formato 2
    (separado por #) del archivo origen al archivo destino en formato csv
    
    Recibe ambos archivos abiertos
    '''
    for linea in origen:
        datos = linea.strip().split("#")
        destino.write(','.join(datos) + '\n')

def __main__():
    
    try:
        origen = open("archivo2.txt", "r")
        destino = open("empleados2.csv", "w")
    except IOError:
        print('Ocurrio un error al abrir los archivos.')
    else:
        transfiereDatosF2(origen, destino)
        origen.close()
        destino.close()

if __name__ == "__main__":
    __main__()
