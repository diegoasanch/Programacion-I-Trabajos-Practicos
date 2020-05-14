'''
Eliminar de una lista de palabras las palabras que se encuentren en
una segunda lista. Imprimir la lista original, la lista de palabras
a eliminar y la lista resultante.
'''
from listas import borra_nombres

def cargaStr():
    'Carga y devuelve una lista con strings'
    lista = []
    print('Ingrese un campo vacio para finalizar\n')
    nombre = input('Ingrese un nombre: ')
    while nombre != '':
        lista.append(nombre)
        nombre = input('Ingrese un nombre: ')
    return lista


def main():
    print('Ingrese los nombres de la lista!')
    lista = cargaStr()
    print('\nCarga exitosa!\n')
    print('Ingrese los nombres a eliminar de la lista')
    elim = cargaStr()
    print('\nCarga exitosa!\n')
    print('Lista original:', lista)
    print('Nombres a eliminar:', elim)
    borra_nombres(lista, elim)
    print('Lista limpia:', lista)

if __name__ == "__main__":
    main()