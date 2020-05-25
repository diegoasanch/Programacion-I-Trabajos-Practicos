from Ej_1_Sitios_Web import imprimeListado

def existeEnlista(lista, valor):
    'Determina si un valor existe en la lista sin tomar en cuenta mayusculas'
    existe = False
    for item in lista:
        if item.lower() == valor.lower():
            existe = True
            break
    return existe

def agregarUnicos(lista, valor):
    '''Agrega valor a lista si este no existe en la lista
    En caso de ya existit levanta ValueError
    '''
    if not existeEnlista(lista, valor):
        lista.append(valor)
    else:
        raise ValueError(f'Imposible agregar elementos duplicados => "{valor}"')

def __main__():

    print('Carga elementos unicos en una lista.')
    print('Para finalizar ingrese un campo vacio.')
    lista = []
    while True:
        try:
            valor = input('Ingrese un item para la lista: ')
            if valor == '':
                raise KeyboardInterrupt

            agregarUnicos(lista, valor)

        except ValueError as error:
            print(f'Error: {error}')
        except KeyboardInterrupt:
            print('Ha finalizado la carga.')
            break
    
    print('Valores agregados:')
    imprimeListado(lista)

if __name__ == "__main__":
    __main__()
