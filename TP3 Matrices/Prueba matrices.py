def creaMatriz(m=3, n=3):
    '''crea dos matrices de orden mxn con la condicion del TP2.4 de algebra
    aij = 2i – j, bij = -3 + i + j'''
    A, B = [], []
    for i in range(1, m+1):
        A.append([])
        B.append([])
        for j in range(1, n+1):
            A[i-1].append(2 * i - j)
            B[i-1].append(-3 + i + j)
    return A, B

def imprimirMatriz(Matriz):
    for fila in Matriz:
        print(fila)

A, B = creaMatriz()
imprimirMatriz(A)
imprimirMatriz(B)
