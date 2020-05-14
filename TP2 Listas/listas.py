"""Funciones para el manejo de listas

a ser usado en el TP2 de Programacion I
"""

from random import randint

def cargaRandom(N=10, minimo=1, maximo=100):
    'Carga lista con N numeros random entre minimo y maximo'

    lista = [randint(minimo, maximo) for _ in range(N)]
    return lista

# def superposicion(v1, v2):
#     'Determina si las listas v1 y v2 comparten al menos un item'

#     comun = False
#     for item in v1:
#         if item in v2:
#             comun = True
#     return comun

def superposicion(v1, v2):
    comun = False
    i, j = 0, 0
    while i < len(v1) and not comun:
        j = 0
        while j < len(v2) and not comun:
            if v1[i] == v2[j]:
                comun = True
            j += 1
        i += 1
    return comun

def repetidos(lista):
    'Determina si existen elementos repetidos en una lista'

    repetido = False
    i = 0
    while i < len(lista) and not repetido:
        if lista[i] in lista[i:]:
            repetido = True
        i += 1
    return repetido

def listasinReps(lista):
    'Devuelve una nueva lista sin los elementos repetidos de la OG'

    nueva_lista = []
    for item in lista:
        if item not in nueva_lista:
            nueva_lista.append(item)
    return nueva_lista


def borra(item, lista):
    'Elimina las apariciones de item en la lista'

    veces = 0
    while item in lista:
        lista.remove(item)
        veces += 1
    return veces

potencia = lambda x, exp = 2: x ** exp

def listaCuadrados(hasta):
    'Crea una lista con los cuadrados desde 1 hasta el param hasta'
    
    lista = [potencia(x) for x in range(1, hasta + 1)]
    return lista

def esCapicua(lista):
    'determina si una lista cualquiera es capicua'
    capicua = lista == lista[::-1]
    return capicua

def sumaAcumulada(lista):
    'Devuelve lista con la suma acumulada de items de una lista'
    acum = 0
    nueva = []
    for numero in lista:
        acum += numero
        nueva.append(acum)
    return nueva

def borra_nombres(lista, elim):
    'Elimina de lista los nombres de elim'
    for name in elim:
        while name in lista:
            lista.remove(name)

def intersec(M, N):
    'Devuelve una lista con la interseccion de M y N'
    MyN = []
    for item in M:
        if item in N and item not in MyN: # Evitamos duplicados
            MyN.append(item)
    return MyN

def ordenada(lista):
    'Determina si una lista esta ordenada de forma ascendente'
    ordenada = True
    i = 0
    while i < (len(lista) - 1) and ordenada:
        if lista[i] > lista[i + 1]:
            ordenada = False
        i += 1
    return ordenada

def normalizar(lista):
    '''Devuelve una lista Normalizada
    
    Los valores de la nueva lista sumaran 1.0. Cada valor es
    convertido en su proporcion dentro de la lista original.
    '''
    suma = sum(lista)
    for i, num in enumerate(lista):
        lista[i] = num/suma

def partirLista(lista):
    '''Parte una lista a la mitad
    
    Retorna dos listas correspondientes a: primera mitad de la lista,
    segunda mitad de la lista    
    '''

    mitad = len(lista) // 2
    return lista[:mitad], lista[mitad:]

def intercalar(lista1, lista2):
    '''Intercala lista1 con lista2 mediante rebanadas
    
    MODIFICA A LA LISTA 1'''
    for i in range(len(lista2) -1, -1, -1):
        lista1[i+1:i+1] = [lista2[i]]

# def intercalar(lista1, lista2):
#     '''Intercala lista1 con lista2 mediante rebanadas
    
#     MODIFICA A LA LISTA 1'''
#     for i in range(len(lista2)):
#         lista1[(i*2)+1:(i*2)+1] = lista2[i:i+1]

def cargaImpar(minimo=100, maximo=200):
    'Carga los Naturales impares entre minimo y maximo'

    minimo = minimo if minimo % 2 != 0 else minimo + 1
    lista = [x for x in range(minimo, maximo + 1, 2)]

    return lista

def multde7no5(minimo=2000, maximo=3500):
    '''
    Devuelve una lista con los multiplos de 7 que no sean
    multiplos de 5 entre minimo y maximo
    '''
    lista = [x for x in range(minimo, maximo + 1) if x % 7 == 0 and x % 5 != 0]
    
    return lista

def soloimpares(lista):
    'Devuelve los elementos impares de lista'
    imp = [num for num in lista if num % 2 != 0]

    return imp