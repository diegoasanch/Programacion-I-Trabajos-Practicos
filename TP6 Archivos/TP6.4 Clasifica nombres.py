'''
Escribir un programa que lea un archivo de texto conteniendo un conjunto de
apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la
cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el
archivo ESPAÑA.TXT los terminados en "EZ". Descartar el resto.
Ejemplo:
    Arslanian, Gustavo–> ARMENIA.TXT
    Rossini, Giuseppe–> ITALIA.TXT
    Pérez, Juan–> ESPAÑA.TXT
    Smith, John–> descartar
El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE.
No escribir un programa para generarlo.
'''

from archivos import clasifica_nombres, escribir_lista

def __main__():
    
    try:
        filename = 'nombres.txt'
        archivo = open(filename, 'r')
        arm, ita, esp = clasifica_nombres(archivo)
        archivo.close()
        
        archivos = ['ARMENIA.TXT', 'ITALIA.TXT', 'ESPANA.TXT']
        listas = [arm, ita, esp]
    except FileNotFoundError:
        print(f'No se consiguio el archivo {filename}')
    else:
        for i, nombre in enumerate(archivos):
            try:
                archivo = open(nombre, 'w+')
                escribir_lista(archivo, listas[i])
                archivo.close()
            except IOError:
                print(f'No se pudo escribir el archivo {nombre}')
                continue

if __name__ == "__main__":
    __main__()
