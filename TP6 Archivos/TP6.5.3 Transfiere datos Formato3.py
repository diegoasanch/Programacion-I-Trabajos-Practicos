'''
Archivo 3:Todos los campos de este archivo están precedidos por un número
de dos dígitos que indica la longitud del campo a leer.

10Pérez Juan082008021114Corrientes 348
14González Ana M082008011533Juande Garay 1111 3er piso dto A
'''

def transfiereDatosF3(orig, dest, campos_p_linea=3):
    '''
    Transfiere los datos de empleados del archivo escrito con el formato 3
    (cada campo es precedido por dos digitos indicando la longitud del campo
    a leer) del archivo origen al archivo destino en formato csv
    
    Recibe path de origen y destino
    '''
    try:
        origen = open(orig, "r")
        destino = open(dest, "w")
    except IOError:
        print('Ocurrio un error al abrir los archivos.')
    else:
        for linea in origen:
            datos = []
            ini, fin = 0, 0
            for _ in range(campos_p_linea):
                long = int(linea[fin:fin+2])
                ini = fin + 2
                fin = ini + long
                datos.append(linea[ini:fin].strip())

            destino.write(','.join(datos) + '\n')
        origen.close()
        destino.close()

def __main__():
    
    origen = "archivo3.txt"
    destino = "empleados3.csv"
    transfiereDatosF3(origen, destino)

if __name__ == "__main__":
    __main__()
