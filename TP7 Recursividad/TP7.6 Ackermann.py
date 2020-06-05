'''
La función de Ackermann A(m,n) se define de la siguiente forma:

    n+1 si m = 0
    A(m-1,1) si n = 0
    A(m-1,A(m,n-1)) de otro modo

Imprimir un cuadro con los valores que adopta la función para valores de m
entre 0 y 3 y de n entre 0 y 7.
'''

def ackermann(m, n):
    'Funcion de ackermann'
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m-1, ackermann(m, n - 1))

def __main__():
    
    M, N = 4, 8
    space = 6

    print('Eje x = N, eje y = M\n')
    print(' '*space, end='|')

    try:
        for x in range(N):
            print(str(x).center(space), end='')
        print(f"\n{'-' * ((N + 1) * space)}")
        for m in range(M):
            print(str(m).center(space), end='|')
            for n in range(N):
                print(str(ackermann(m, n)).center(space), end='')
            print()
    except RecursionError:
        print(f'{"x".center(space)}\nSe ha alcanzado el limite de recursion de python.')


if __name__ == "__main__":
    __main__()