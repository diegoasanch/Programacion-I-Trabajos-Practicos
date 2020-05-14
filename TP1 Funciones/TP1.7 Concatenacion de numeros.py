'''
Desarrollar una función que reciba como parámetros dos números 
enteros y devuelva el número que resulte de concatenar ambos valores.
Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se
permite utilizar facilidades de Python no vistas en clase.
'''

def invertido(N):

    new = 0
    while N > 0:
        new *= 10
        new += (N % 10)
        N //= 10
    return new


def concatenador(A, B):

    A = A if A >= 0 else -A
    B = B if B >= 0 else -B
    
    B = invertido(B)
    while B > 0:
        A *= 10
        A += (B % 10)
        B //= 10
    return A

def main():

    A = int(input('Ingrese el numero A: '))
    B = int(input('Ingrese el numero B: '))

    C = concatenador(A, B)

    print(f'A + B concatenados es {C}')

if __name__ == "__main__":
    main()