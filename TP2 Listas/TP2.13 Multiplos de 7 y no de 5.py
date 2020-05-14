'''
Escribir un programa para generar una lista con los múltiplos
de 7 que no sean múltiplos de 5, entre 2000 y 3500. Imprimir
la lista obtenida.
'''

def multde7no5(minimo=2000, maximo=3500):
    '''
    Devuelve una lista con los multiplos de 7 que no sean
    multiplos de 5 entre minimo y maximo
    '''
    lista = []
    for num in range(minimo, maximo + 1):
        if num % 7 == 0 and num % 5 != 0:
            lista.append(num)
    
    return lista

def main():
    print('Los multiplos de 7 que no son multiplos de 5 entre 2000 y 3500 son:')
    print(multde7no5())

if __name__ == "__main__":
    main()