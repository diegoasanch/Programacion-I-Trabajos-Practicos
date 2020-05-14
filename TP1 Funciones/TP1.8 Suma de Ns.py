'''
Escribir una función que reciba como parámetro número del 1 al 9 y devuelva el
resultado de sumar n + nn + nnn + nnnn, donde n corresponde al número recibido. 
Por ejemplo, si se ingresa 3 debe devolver 3702 (3+33+333+3333). Escribir
también un programa para verificar el comportamiento de la función. No se
permite utilizar facilidades de Python no vistas en clase.
'''

def suma_n(n):
    i = 0
    suma = 0
    while i < 4:
        a_sumar = n
        for _ in range(i):
            a_sumar = (a_sumar * 10) + n
        suma += a_sumar
        i += 1

    return suma

def main():

    print('Calcule el valor de n + nn + nnn + nnnn')
    n = int(input('Ingrese un valor para n: '))

    while n < 1 or n > 9:
        print('\nDebe ingresar un numero entre 1 y 9')
        n = int(input('Ingrese un valor para n: '))
    
    suma = suma_n(n)
    print(f'{n} + {n}{n} + {n}{n}{n} + {n}{n}{n}{n} = {suma}')

if __name__ == "__main__":
    main()