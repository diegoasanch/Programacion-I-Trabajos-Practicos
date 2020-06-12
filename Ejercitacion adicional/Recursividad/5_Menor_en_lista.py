'''
Desarrollar una función recursiva para retornar el mínimo de una lista.
Resolver:
    a) Utilizando rebanadas.
    b) Utilizando índices.
'''
import random

def busqueda_min(lista, i=0):
    'Devuelve el menor valor de la lista'
    if i+1 == len(lista):
        return lista[i]
    else:
        a = lista[i]
        b = busqueda_min(lista, i+1)
        if a < b:
            return a
        else:
            return b

def busqueda_min2(lista):
    'Devuelve el menor valor de la lista'
    if len(lista) == 1:
        return lista[0]
    else:
        a, *b = lista
        b = busqueda_min2(b)
        if a < b:
            return a
        else:
            return b

def __main__():
    
    lista = [random.randint(1, 235) for _ in range(random.randint(10, 30))]
    menor = busqueda_min(lista)
    menor2 = busqueda_min2(lista)
    print(f'El menor elemento de la lista {lista} es {menor}, {menor2}')

if __name__ == "__main__":
    __main__()

