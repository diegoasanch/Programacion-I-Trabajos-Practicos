'''
Desarrollar una función eliminarclaves() que reciba como parámetros un
diccionario y una lista de claves. La función debe eliminar del diccionario
todas las claves contenidas en la lista, devolviendo el diccionario modificado
y un valor de verdad que indique si la operación fue exitosa. Desarrollar
también un programa para verificar su comportamiento.
'''

def ingreso_entero(texto='Ingrese un numero entero: '):
    'Ingresa un numero entero valido o None'
    while True:
        try:
            num = input(texto)
            if not num:
                break
            num = int(num)
            break
        except ValueError:
            print('* Caracter invalido, debe ingresar un numero entero.')
    return num

def ingreso_lista(texto='Ingrese valores a la lista'):
    'Ingreso de numeros positivos a una lista'
    v = []
    print(texto)
    while True:
        num = ingreso_entero()
        if not num:
            break
        v.append(num)
    return v

def eliminarclaves(diccionario, claves):
    'Elimina de diccionario las claves de lista claves'
    exitoso = False
    try:
        for clave in claves:
            if clave in diccionario.keys():
                del diccionario[clave]
    except Exception as error:
        print(f'Error inesperado: {error}')
    else:
        exitoso = True
    return exitoso

def imprime_dic(dic):
    'Imprime clave y valor de diccionario en orden ascendente'
    for clave in sorted(dic.keys()):
        print(f'{clave} = {dic[clave]}')

def __main__():

    
    diccionario = {num: str(num) for num in range(15)} # diccionario por comprension para ejemplo
    imprime_dic(diccionario)

    a_borrar = ingreso_lista('Ingrese las claves a borrar del diccionario, vacio para finalizar.')
    
    exito = eliminarclaves(diccionario, a_borrar)
    print()

    if exito:
        print('Se eliminaron las claves con exito.\nDiccionario resultante:\n')
        imprime_dic(diccionario)
    else:
        print('No se logro operar')

if __name__ == "__main__":
    __main__()