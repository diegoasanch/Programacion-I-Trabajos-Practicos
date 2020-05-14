'''
Desarrollar cada una de las siguientes funciones y escribir un programa 
que permita verificar su funcionamiento imprimiendo la lista luego de 
invocar a cada función:
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad 
       de elementos también será un número al azar de dos dígitos.
    b. Calcular y devolver la sumatoria de todos los elementos de la lista
       anterior.
    c. Eliminar todas las apariciones de un valor en la lista anterior. 
       El valor a eliminar se ingresa desde el teclado y la función lo 
       recibe como parámetro.
    d. Determinar si el contenido de una lista cualquiera es capicúa, sin 
       usar listas auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
'''

from random import randint
from listas import cargaRandom, borra, esCapicua

def main():
   N = randint(10, 99)
   milista = cargaRandom(N, 1000, 9999)
   print(milista)

   print(f'\nItems cargados: {len(milista)}')
   suma_milista = sum(milista)
   print(f'Suma de los items de milista: {suma_milista}')

   a_borrar = int(input('> Ingrese el valor que desea eliminar de la lista: '))
   borrados = borra(a_borrar, milista)
   print(f'\nLista:\n{milista}')
   print(f'\nSe elimino el numero {a_borrar}, {borrados} veces de la lista')
    
   if esCapicua(milista):
      print('La lista es capicua')
   else:
      print('La lista no es capicua')

if __name__ == "__main__":
   main()