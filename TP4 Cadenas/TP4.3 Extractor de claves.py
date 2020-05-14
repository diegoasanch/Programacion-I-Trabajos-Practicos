'''
Los números de claves de dos cajas fuertes están intercalados dentro de
un número entero llamado "clave maestra", cuya longitud no se conoce.
Realizar un programa para obtener ambas claves, donde la primera se
construye con los dígitos impares de la clave maestra y la segunda con 
los dígitos pares. Los dígitos se numeran desde la izquierda. Ejemplo:
Si clave maestra = 18293, la clave 1 sería 123 y la clave 2 sería 89
'''

from cadenas import extraeClaves

def main():
    master = input('Ingrese su clave maestra: ')
    print()
    if master != '':
        clave1, clave2 = extraeClaves(master)
        print(f'Su clave1 es: {clave1} y su clave2 es: {clave2}')
    else:
        print('No ingreso ninguna clave!')

if __name__ == "__main__":
    main()
