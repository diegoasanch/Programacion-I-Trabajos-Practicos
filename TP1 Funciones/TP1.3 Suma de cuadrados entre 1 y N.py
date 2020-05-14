'''
Para un número entero N menor de 100 recibido como parámetro, escribir
un programa que utilice una función para devolver la suma de los cuadrados 
de aquellos números entre 1 y N que están separados entre si por cuatro
unidades. (1^2 + 5^2 + 9^2 + 13^2 + …)
'''

def suma_de_cuad(N):
    suma = 0
    for i in range(1, N + 1, 4):
        suma += i ** 2
    return suma

def main():
    print('''Calcule la suma de los cuadrados de aquellos números
entre 1 y N que están separados entre si por cuatro unidades.\n''')

    N = int(input('Ingrese el valor de N: '))
    while N >= 100 or N < 1:
        print('\nDebe ingresar un numero menor a 100 y mayor o igual a 1!')
        N = int(input('Ingrese el valor de N: '))

    resultado = suma_de_cuad(N)
    print(f'\nEl resultado es {resultado}')

if __name__ == "__main__":
    main()