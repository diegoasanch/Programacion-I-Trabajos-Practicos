# from excepciones import *

# numero = ingresoNatural()
# print(numero)

def imprimeMatriz(matriz, c=6, row='Fila', col='Col'):
    
    titulo = ' '*c
    for i in range(len(matriz[0])):
        titulo += f"{col} {i}".center(c)
    print(titulo)
    for i, fila in enumerate(matriz):
        print(f'{row} {i}'.center(c), end='')
        for item in fila:
            print(str(item).center(c), end='')
        print()

if __name__ == "__main__":    
    col = 4
    fil = 5
    m = [[0] * col for _ in range(fil)]
    imprimeMatriz(m, c=10, row="Fabrica", col='Dia')
