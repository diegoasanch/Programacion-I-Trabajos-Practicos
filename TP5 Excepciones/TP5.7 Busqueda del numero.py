'''
Escribir un programa que juegue con el usuario a adivinar un número. El
programa debe generar un número al azar entre 1 y 500 y el usuario debe
adivinarlo. Para eso, cada vez que se introduce un valor se muestra un 
mensaje indicando si el número que tiene  que adivinar es mayor o menor
que el ingresado. Cuando consiga adivinarlo, se debe imprimir en pantalla
la cantidad de intentos que le tomó hallar el número. Si el usuario
introduce algo que no sea un número se mostrará un mensaje en pantalla y
se lo contará como un intento más.
'''

from random import randint
from excepciones import opcion

def __main__():
    while True:
        
        print(('\n'*40) + 'Bienvenido a busqueda del numero!\n')
        num = randint(1, 500)
        ganado = False
        intentos = 0
        
        while not ganado:
            try:
                intentos += 1
                guess = int(input(f'\n> Intento {intentos}: '))

                if guess == num:
                    print(f'\n\n * El numero secreto es {num}!!')
                    ganado = True
                    continue
                elif guess == -1:
                    raise KeyboardInterrupt
                elif guess > num:
                    magnitud = 'menor'
                else:
                    magnitud = 'mayor'
                print(f'El numero secreto es {magnitud} a {guess}')

            except ValueError:
                print('   * Debe ingresar un numero entero! *')
            except KeyboardInterrupt:
                if opcion('\nDesea abandonar la partida?: '):
                    break
        if ganado:
            mensaje = 'Ha ganado la partida despues de '
        else:
            mensaje = 'Ha abandonado la partida despues de '
        print('\n\n' + mensaje + f'{intentos} intentos.')

        if not opcion('\nDesea jugar una nueva partida?: '):
            break

    print('\n'*40)
    print('Gracias por jugar busqueda del numero!!!')

if __name__ == "__main__":
    __main__()
