'''
Escribir dos funciones para imprimir por pantalla cada uno de los siguientes
patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
**********      **
**********      ****
**********      ******
**********      ********
**********      **********
'''

def asteriscos(filas):
    for _ in range(filas):
        for _ in range(filas * 2):
            print('*', end='')
        print() # salto de linea
    
    print()
    print()

    i = 0
    for _ in range(filas):
        i += 2
        for _ in range(i):
            print('*', end='')
        print() # salto de linea

def main():
    filas = int(input('Ingrese la cantidad de filas a imprimir: '))
    print()
    asteriscos(filas)

if __name__ == "__main__":
    main()
