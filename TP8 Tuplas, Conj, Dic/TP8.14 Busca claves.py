'''
Escribir una función buscarclave() que reciba como parámetros un diccionario
y un valor, y devuelva una lista de claves que apunten ("mapeen") a ese
valor en el diccionario. Comprobar el comportamiento de la función mediante
un programa apropiado.
'''
import random

buscarclave = lambda dic, buscar: [clave for clave, valor in dic.items() if valor == buscar]
'Retorna lista con las claves que resultan en valor dentro de dic'

dic_random = lambda cant=20: {str(i+1): random.randint(1, 20) for i in range(cant)}
'Devuelve un diccionario con claves y valores random'

def ingreso_entero(texto='Ingrese un numero: ', tipo='numero entero'):
    'Ingresa un numero entero positivo'
    while True:
        try:
            num = int(input(texto))
            if num <= 0:
                raise ValueError
            break
        except ValueError:
            print(f'\n* Debe ingresar un {tipo} valido mayor a 0!')
    return num

def __main__():

    mi_dic = dic_random()
    print('Diccionario:', mi_dic)
    a_buscar = ingreso_entero()
    claves = buscarclave(mi_dic, a_buscar)
    if claves:
        print(f"Las claves cuyo valor es {a_buscar} son: {', '.join(claves)}")
    else:
        print(f'Ninguna clave lleva al valor {a_buscar}')

if __name__ == "__main__":
    __main__()