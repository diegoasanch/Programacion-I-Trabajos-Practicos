'''
Crear una función contarvocales(), que reciba una palabra y cuente cuántas
letras "a" contiene, cuántas "e", cuántas "i", etc. Devolver un diccionario
con los resultados. Desarrollar un programa para leer una frase e invocar
a la función por cada palabra que contenga la misma. Imprimir cada palabra
y la cantidad de vocales hallada.
'''

# def contarvocales(palabra):
#     'Devuelve diccionario con la cantidad de vocales en palabra'
#     vocales = 'aeiou'
#     cant = {}
#     for vocal in vocales:
#         cant[vocal] = palabra.lower().count(vocal)
#     return cant

contarvocales = lambda palabra: {voc: palabra.lower().count(voc) for voc in 'aeiou'}
# Vocales en palabra en una sola linea ¯\_(ツ)_/¯

def vocales_por_palabra(frase):
    'Imprime la cantidad de vocales por cada palabra en frase'
    for palabra in frase.split():
        cant = contarvocales(palabra)
        print(f'Palabra: {palabra}, cantidad de vocales: {string_dic(cant)}')

def string_dic(dic):
    'devuelve str con clave y valor de diccionario en orden ascendente en una sola linea'
    texto = ''
    for clave in sorted(dic.keys()):
        if dic[clave] > 0:
            texto += f' {clave}={dic[clave]},'
    return texto[:-1]

def __main__():
    
    frase = input('Ingrese una frase para contar las vocales de cada palabra: ')
    vocales_por_palabra(frase)

if __name__ == "__main__":
    __main__()