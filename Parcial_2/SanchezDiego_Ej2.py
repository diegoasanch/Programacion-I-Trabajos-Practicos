'''
Ejercicio 2)

Leer las frases del archivo frases.txt y crear un nuevo archivo con las frases
seguido de dos puntos (:) y la cantidad de letras mayúsculas que posee. Contar
las letras mayúsculas de una cadena mediante una función recursiva.
'''

# Aclaracion: corriendo el programa con Python 3.8.2 y sin especificar la
# codificacion del archivoo, el metodo isupper() cuenta como mayuscula a las
# letras con tilde o dieresis, lo probe quitandole las tildes y funciona como 
# deberia asi que el problema esta ahi.


def cuenta_mayus(frase, i=0):
    'Retorna la cantidad de mayusculas en una frase'

    if i == len(frase):
        return 0
    else:
        es_mayus = int(frase[i].isupper())

        return es_mayus + cuenta_mayus(frase, i+1) 

        # if frase[i].isupper():
        #     return 1 + cuenta_mayus(frase, i+1)
        # else:
        #     return 0 + cuenta_mayus(frase, i+1)
        
        # de ambas maneras toma las letras con tilde y direresis como upper


def mayus_en_frases(nombre_arch1, nombre_arch2):
    '''
    Cuenta las letras mayusculas de cada registro del arch1 y en arch2
    copia el registro con la cantidad de letras mayusculas que posee el mismo
    '''
    ejecuctado = False
    try:
        arch1 = open(nombre_arch1, 'r')
        arch2 = open(nombre_arch2, 'w')

        for frase in arch1:
            frase = frase.rstrip()
            mayus = cuenta_mayus(frase)
            arch2.write(frase + f': {mayus}\n')

    except IOError:
        print('Ocurrio un error al abrir los archivos.')
    except Exception as error:
        print(f'Ocurrio un error inesperado {error}')
    
    finally:
        try:
            arch1.close()
            arch2.close()
        except:
            pass
        else:
            ejecuctado = True

    return ejecuctado


def __main__():
    
    archivo = 'frases.txt'
    nuevo_archivo = 'cant_mayusculas.txt'

    ejecuctado = mayus_en_frases(archivo, nuevo_archivo)

    if ejecuctado:
        print('El programa se ejecuto con exito.')
    else:
        print('Ocurrio un proble durante la ejecucion.')


if __name__ == "__main__":
    __main__()
