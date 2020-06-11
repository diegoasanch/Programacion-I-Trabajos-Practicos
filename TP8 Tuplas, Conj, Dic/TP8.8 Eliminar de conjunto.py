'''
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores
al usuario y eliminarlos del conjunto mediante el método remove, mostrando
el contenido del conjunto luego de cada eliminación. Finalizar el proceso al
ingresar -1. Utilizar manejo de excepciones para evitar errores al intentar
quitar elementos inexistentes.
'''

def ingreso_natural(texto='Ingrese un numero natural: '):
    'Ingresa un numero natural o -1'
    while True:
        try:
            num = int(input(texto))
            if num < -1:
                raise ValueError('* Caracter invalido, debe ingresar un ' + \
                'numero entero positivo o -1 para salir.')
            break
        except ValueError as error:
            print(error)
    return num

def quitar(conj, elem):
    'elimina el elemento elem del conj si existe'
    try:
        conj.remove(elem)
    except KeyError:
        print(f'\n ** El elemento {elem} no es parte del conjunto.')

def __main__():
    
    conj = set(range(10))
    while True:

        print(f'\nConjunto: {conj}')
        elim = ingreso_natural('Ingrese el item a eliminar del conjunto: ')
        if elim == -1:
            break
        quitar(conj, elim)

    
if __name__ == "__main__":
    __main__()