'''
Idem anterior, pero determinando si los vectores son paralelos. Cuando dos
vectores son paralelos los cocientes de sus coordenadas correspondientes son
iguales entre sí. Ejemplo: U = (3,-1) y V = (-9,3)
'''

# son_paralelos = lambda vec1, vec2: len(set([vec1[i] / vec2[i] for i in range(len(vec1))])) == 1 if len(vec1) == len(vec2) else False
# 'Determina si dos vectores en R^n son ortogonales pero en una linea y chocha si hay 0'
# ¯\_(ツ)_/¯

def son_paralelos(vec1, vec2, i=0):
    'Determina si dos vectores en R^n son ortogonales'
    if len(vec1) != len(vec2):
        raise ValueError('Los vectores estan en distintos espacios.')
    try:
        div = vec1[i] / vec2[i]
    except ZeroDivisionError:
        div = 0
    if (i + 1) == len(vec1):
        return div
    else:
        return div == son_paralelos(vec1, vec2, i+1)

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
            if son_paralelos(vec1, vec2):
                print(f'Los vectores {vec1} y {vec2} son paralelos.')
            else:
                print(f'Los vectores {vec1} y {vec2} no son paralelos.')
        except ValueError as error:
            print(f'Error: {error}')
    else:
        print('No se recibieron los datos suficientes.')


if __name__ == "__main__":
    __main__()