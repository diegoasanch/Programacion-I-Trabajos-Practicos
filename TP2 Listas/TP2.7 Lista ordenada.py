'''
Escribir una función que reciba una lista como parámetro y devuelva
True si la lista está ordenada en forma ascendente o False en caso
contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y 
ordenada(['b', 'a']) retorna False. Desarrollar además un programa 
para verificar el comportamiento de la función. 
'''

from listas import cargaRandom, ordenada

def main():
    lista = cargaRandom()
    print('Lista random:', lista)
    if ordenada(lista):
        print('La lista esta ordenada! :)')
    else:
        print('La lista no esta ordenada :(')

if __name__ == "__main__":
    main()