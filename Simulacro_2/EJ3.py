'''
Desarrollar una función que reciba una cadena e informe para cada palabra
sus repeticiones, teniendo en cuenta: 
    1. Todas las claves deben estar en minúsuculas (es decir, ‘Hola’ y ‘hola’
      deberían sumar al mismo contador). 
    2. Se deben ignorar los signos de puntuación y los números (es decir, 
      “ ‘(),.;:?¡¿[]{}-’ ”). 
Desarrollar un programa principal para ingresar una frase y luego mostrar por
pantalla el listado de palabras y sus repeticiones ordenado alfabeticamente.
'''
limpia_palabra = lambda pal: ''.join(filter(lambda letra: letra.isalpha(), pal))
'Filtra los elementos no alfabeticos'

def repeticiones_palabras(frase):
    'Devuelve diccionario con cuantas veces esta cada palabra'
    dic = {}
    for palabra in frase.lower().split():
        palabra_limpia = limpia_palabra(palabra)
        if palabra_limpia != '':
            if palabra_limpia in dic:
                dic[palabra_limpia] += 1
            else:
                dic[palabra_limpia] = 1
    return dic

def imprimir_diccionario(diccionario):
    'Imprime los valores del diccionario en orden alfabetico'
    claves = list(diccionario.keys())
    claves.sort()
    for key in claves:
        print(f'La palabra {key} aparece {diccionario[key]} veces.')

def __main__():

    frase = input('Ingrese una frase: ')
    cantidad_de_reps = repeticiones_palabras(frase)
    imprimir_diccionario(cantidad_de_reps)

if __name__ == "__main__":
    __main__()
