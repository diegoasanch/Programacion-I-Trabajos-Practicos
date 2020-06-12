'''
Contar la cantidad de números de una cadena mediante una función recursiva.
'''

def nums_en_str(cadena, i=0):
    'Devuelve la cantidad de numeros en la cadena cadena'
    es_dig = int(cadena[i].isdigit())

    if i + 1 == len(cadena):
        return es_dig
    else:
        return es_dig + nums_en_str(cadena, i+1)

def __main__():
    
    cadena = input('Ingrese la cadena: ')
    nums = nums_en_str(cadena)
    print()
    if nums:
        print(f'La cadena {cadena} tiene {nums} numeros.')
    else:
        print(f'La cadena {cadena} no tiene ningun numero en ella.')

if __name__ == "__main__":
    __main__()
