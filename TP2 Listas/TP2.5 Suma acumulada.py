"""Escribir un programa que calcule la suma acumulada a partir 
de una lista de números. El programa debe generar una nueva lista 
donde el primer elemento es el mismo de la lista original, el 
segundo elemento es la suma del primero más el segundo, el tercer
elemento es la suma del primero más el segundo más el tercero y 
así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es 
[1,3,6].
"""

from listas import cargaRandom, sumaAcumulada

def main():
    milista = cargaRandom(10)
    print('Lista generada al azar:', milista)
    milistaAcum = sumaAcumulada(milista)
    print('\nLista acumulada:', milistaAcum)

if __name__ == "__main__":
    main()