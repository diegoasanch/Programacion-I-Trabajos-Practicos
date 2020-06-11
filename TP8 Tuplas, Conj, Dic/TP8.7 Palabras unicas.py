'''
Ingresar una frase desde el teclado y eliminar las palabras repetidas,
dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. La eliminación de las palabras duplicadas
debe realizarse a través de un conjunto.
'''

palabra_limpia = lambda palabra: ''.join(filter(lambda letra: letra.isalnum(), palabra))
'Devuelve la palabra recibida con solo caracteres alfanumericos'

def palabras_sin_reps(frase):
    'Devuelve lista con palabras unicas ordenadas alfabeticamente'
    palabras = list(set(map(palabra_limpia, frase.lower().split())))
    palabras.sort(key=len)
    return palabras

def __main__():
    
    frase = input('Ingrese una frase: ')
    if frase:
        unicas = palabras_sin_reps(frase)
        print('Las palabras unicas son:')
        for palabra in unicas:
            print(f' - {palabra}')
    else:
        print('No se ingreso ninguna palabra')

if __name__ == "__main__":
    __main__()