'''
Generar una lista con números al azar entre 0 y 100, donde su cantidad de
elementos será un número par también obtenido al azar entre 10 y 50. 
Luego se solicita partir la lista por la mitad a través de la técnica de 
las rebanadas, creando dos nuevas listas. Imprimir las tres listas por
pantalla.
'''
from random import randint
from listas import cargaRandom, partirLista

def main():
    N = randint(10, 50)
    N = N if N % 2 == 0 else N - 1
    lista = cargaRandom(N=N, minimo=0)
    print('Lista completa:', lista)
    mitad1, mitad2 = partirLista(lista)
    print('Primera mitad:', mitad1)
    print('Segunda mitad:', mitad2)

if __name__ == "__main__":
    main()