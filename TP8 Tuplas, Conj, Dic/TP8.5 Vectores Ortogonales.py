'''
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un
valor de verdad indicando si son ortogonales o no. Desarrollar también un
programa que permita verificar el comportamiento de la función. 
'''

# son_ortogononales = lambda vec1, vec2: not sum([vec1[i] * vec2[i] for i in range(len(vec1))]) if len(vec1) == len(vec2) else False
# 'Determina si dos vectores en R^n son ortogonales pero en una linea'
# ¯\_(ツ)_/¯

def son_ortogononales(vec1, vec2):
    'Determina si dos vectores en R^n son ortogonales'
    if len(vec1) != len(vec2):
        raise ValueError('Los vectores estan en distintos espacios.')
    prod = 0
    for i in range(len(vec1)):
        prod += vec1[i] * vec2[i]
    return not prod

def ingresa_vector():
    'Ingresa un vector en R^n y lo devuelve como tupla'
    while True:
        try:
            params = input('Ingrese el vector (x,y): ')
            if not params:
                vec = ()
                break
            vec = tuple(map(float, params.strip('()').split(',')))
            break
        except ValueError:
            print('\n*Solo se permiten numeros.')
    return vec

def __main__():
    
    vec1 = ingresa_vector()
    vec2 = ingresa_vector()
    if vec1 and vec2:
        try:
            if son_ortogononales(vec1, vec2):
                print(f'Los vectores {vec1} y {vec2} son ortogonales.')
            else:
                print(f'Los vectores {vec1} y {vec2} no son ortogonales.')
        except ValueError as error:
            print(f'Error: {error}')
    else:
        print('No se recibieron los datos suficientes.')


if __name__ == "__main__":
    __main__()