# -------- Defs con los conocimientos de Fundamentos de informatica ----------

def cargaRandomOG(N=10, minimo=1, maximo=100):
    '''Carga N numeros random entre minimo y maximo
    
    Acepta parametros nuevos
    '''

    lista = []
    for _ in range(N):
        lista.append(randint(minimo, maximo))
    return lista

def esCapicuaOG(lista):
    'determina si una lista cualquiera es capicua'
    capicua = True
    for i in range(len(lista)):
        if lista[i] != lista[-i -1]:
            capicua = False
    return capicua

def borraOG(item, lista):
    'Elimina las apariciones de item en la lista'

    veces = 0
    for i in range(len(lista)-1, -1, -1):
        '''comienza en el ultimo item y va en reversa para evitar el error
        list index out of range'''
        if lista[i] == item:
            lista.pop(i)
            veces += 1
    return veces

def sumaListaOG(lista):
    '''Suma los items de una lista
    
    Solo funciona con listas cargadas unicamente con enteros
    '''

    suma = 0
    for num in lista:
        suma += num
    return suma

def listaCuadradosOG(hasta):
    'Crea una lista con los cuadrados desde 1 hasta el param hasta'

    lista = []
    for i in range(1, hasta + 1):
        lista.append(potencia(i))
    return lista

def mostrarUltimosN_OG(lista, N):
    'Imprime los ultimos N elementos de una lista'

    if len(lista) > N:
        ultimos = N
    else:
        ultimos = len(lista)
    total = len(lista)

    for i in range(total - ultimos, total):
        print(lista[i], end=' ')
    print()

def borra_nombresOG(lista, elim):
    'Elimina de lista los nombres de elim'
    for eliminar in elim:
        for i in range(len(lista) -1, -1, -1):
            if lista[i] == eliminar:
                lista.pop(i)

def normalizarOG(lista):
    '''Devuelve una lista Normalizada
    
    Los valores de la nueva lista sumaran 1.0. Cada valor es
    convertido en su proporcion dentro de la lista original.
    '''
    suma = sum(lista)
    normal = []
    for item in lista:
        norm = item/suma
        # norm = round(norm, 2)
        normal.append(norm)
    return normal