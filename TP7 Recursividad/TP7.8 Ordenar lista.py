'''
Realizar la implementación recursiva del método de selección para ordenar una
lista de números enteros. Sugerencia: Colocar el elemento más pequeño en la 
primera posición, y luego ordenar el resto de la lista con una llamada
recursiva.
'''
def ingreso_entero(texto='Ingrese un numero entero: '):
    'Ingresa un numero entero valido o None'
    while True:
        try:
            num = int(input(texto))
            if num < -1:
                raise ValueError
            break
        except ValueError:
            print('* Caracter invalido, debe ingresar un numero entero positivo. O -1')
        except KeyboardInterrupt:
            num = None
            break
    return num

def ingreso_lista():
    'Ingreso de numeros positivos a una lista'
    print('Ingrese los numeros para cargar a la lista, -1 para finalizar')
    v = []
    while True:
        num = ingreso_entero()
        if num == -1:
            break
        v.append(num)
    return v

def ordenar_lista(lista):
    'Ordena una lista de menor a mayor recursivamente'
    if len(lista) == 1:
        return lista
    else:
        return [lista.pop(lista.index(min(lista)))] + ordenar_lista(lista)

def __main__():

    lista = ingreso_lista()
    if len(lista) >= 2:
        lista = ordenar_lista(lista)
        print(f'La lista ordenada es {lista}')
    else:
        print('Debe ingresar al menos dos elementos')
if __name__ == "__main__":
    __main__()