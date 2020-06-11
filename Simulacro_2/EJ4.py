'''
Desarrollar un programa principal para ingresar dos palabras por teclado e
informar las letras poseen en común. Permitir ingresar varias veces dos
palabras hasta que la primera que se ingrese sea vacía. Para el ingreso de
palabras, generar y gestionar una excepcion si se ingresan numeros, espacios
o símbolos, aceptar solo palabras con caractgeres alfabeticos.
'''

def ingreso_palabra(texto):
    'Valida el ingreso de una palabra solo alfabetica'
    while True:
        try:
            palabra = input(texto)
            for letra in palabra:
                if letra.isdigit():
                    raise ValueError('No se permiten digitos')
                elif not letra.isalpha():
                    raise ValueError('Solo se permiten caracteres alfabeticos.')
            break
        except ValueError as error:
            print(f'\nPalabra invalida {error}')
    return palabra

letras_comunes = lambda cad1, cad2: list(set(cad1.lower()) & set(cad2.lower()))
'Devuelve una lista con las letras comunes entre las cadenas'


def __main__():
    while True:
        try:
            palabra1 = ingreso_palabra('Ingrese la palabra 1: ')
            if not palabra1:
                raise KeyboardInterrupt
            palabra2 = ingreso_palabra('Ingrese la palabra 2: ')
            comunes = letras_comunes(palabra1, palabra2)
            if comunes:
                print(f"Las letras comunes entre {palabra1} y {palabra2} son: {', '.join(comunes)}")
            else:
                print('Las palabras no comparten ninguna letra')
        except KeyboardInterrupt:
            print('\nHa abandonado el programa.')
            break

if __name__ == "__main__":
    __main__()