'''
Dados dos números enteros no negativos, devolver el resultado de calcular el
Máximo Común Divisor (también llamado Divisor Común Mayor) basándose en las
siguientes propiedades:
    MCD(X, X)= X
    MCD(X, Y)= MCD(Y, X)
    Si X > Y => MCD(X, Y) = MCD(X–Y, Y)
Utilizando la función anterior calcular el MCD de todos los elementos de una
lista de números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z).
No se permite utilizar iteraciones en ninguna etapa del proceso.
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
    print('Ingrese los numeros para calcular el MCD, -1 para finalizar')
    v = []
    while True:
        num = ingreso_entero()
        if num == -1:
            break
        v.append(num)
    return v

def lista_unpack(lista):
    'Desempaca los valores de una lista para pasarlos a '
    if len(lista) == 2:
        x, y = lista[0], lista[1]
    else:
        x, y = lista[:-1], lista[-1]
    return x, y

def MCD(X, Y=None):
    '''
    Calcula el maximo comun divisor de dos o mas numeros
    Si son mas de dos numeros, recibe para X una lista e Y el ultimo numero
    '''
    if Y == None:
        X, Y = lista_unpack(X)
    if type(X) == list:
        if len(X) > 1:
            X1, X2 = lista_unpack(X)
            return MCD(MCD(X1, X2), Y)
        else:
            return MCD(X[0], Y)
    elif X == Y:
        return X
    elif X < Y:
        return MCD(Y, X)
    else:
        return MCD(X - Y, Y)

def __main__():
    
    lista = ingreso_lista()
    if len(lista) >= 2:
        try:   
            resultado = MCD(lista)
            print(f'El MCD de {lista} es = {resultado}')
        except RecursionError:
            print('Se ha alcanzado el limite de recursion de python.')
    else:
        print('Debe ingresar al menos dos numeros')

if __name__ == "__main__":
    __main__()