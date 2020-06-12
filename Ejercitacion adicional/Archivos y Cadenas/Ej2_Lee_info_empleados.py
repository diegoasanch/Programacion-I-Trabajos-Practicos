'''
Ejercicio 2: mostrar datos de empleados leídos de un archivo de texto. Los
campos de los registros están están precedidos por un número de dos dígitos
que indica la longitud del campo a leer.
'''

from funciones import imprimirEmpleados

def __main__():

    filename = 'empleados.txt'
    imprimirEmpleados(filename)

if __name__ == "__main__":
    __main__()