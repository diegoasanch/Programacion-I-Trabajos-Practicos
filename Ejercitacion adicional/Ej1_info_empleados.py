'''
Ejercicio 1: grabar un archivo de texto con datos de empleados. Los campos de
los registros están precedidos por un número de dos dígitos que indica la
longitud del campo a leer
'''
from funciones import cargarEmpleados

def __main__():
    
    filename = 'empleados.txt'
    cargarEmpleados(filename)

if __name__ == "__main__":
    __main__()
