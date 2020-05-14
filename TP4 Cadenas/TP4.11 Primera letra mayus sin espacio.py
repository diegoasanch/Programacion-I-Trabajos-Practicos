'''
Escribir un programa que permita ingresar una cadena de caracteres y
coloque en mayúscula la primera letra posterior a un espacio, eliminando
todos los espacios que contenga. Imprimir por pantalla la cadena
obtenida.
'''

from cadenas import mayusSinEspacio

def __main__():

    print('Coloca mayuscula a la primera letra de cada palabra y retira los espacios')
    cadena = input('Ingrese su cadena: ')
    nueva_cad = mayusSinEspacio(cadena)
    print(f'\nLa nueva cadena es: \n{nueva_cad}')

if __name__ == "__main__":
    __main__()
