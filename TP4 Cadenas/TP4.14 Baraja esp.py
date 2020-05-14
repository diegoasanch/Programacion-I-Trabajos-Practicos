'''
Escribir un programa para crear una lista por comprensión con los naipes de
la baraja española. La lista debe contener cadenas de caracteres. Ejemplo:
["1 Oros", "2 Oros"... ]. Imprimir la lista por pantalla.
'''

from cadenas import creaBarajaEsp

def __main__():
    print('Baraja española:')
    mazo = creaBarajaEsp()
    for carta in mazo:
        print('\t' + carta)

if __name__ == "__main__":
    __main__()
