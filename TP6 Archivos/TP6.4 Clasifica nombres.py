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
        archivos = ['ARMENIA.TXT', 'ITALIA.TXT', 'ESPANA.TXT']
        finales = ['ian', 'ini', 'ez']

        filename = 'nombres.txt'
        nombres = open(filename, 'r')
        
        for i, pais in enumerate(archivos):
            nombres.seek(0) # reseteamos  el archivo abierto a la primera linea
            clasif = clasifica_nombres(nombres, finales[i])
            nombres_pais = open(pais, 'w')
            escribir_lista(nombres_pais, clasif)
            nombres_pais.close()

        nombres.close()

    except FileNotFoundError:
        print(f'No se consiguio el archivo {filename}')
    finally:
        if nombres != None:
            nombres.close()
        if nombres_pais != None:
            nombres_pais.close()

if __name__ == "__main__":
    __main__()
