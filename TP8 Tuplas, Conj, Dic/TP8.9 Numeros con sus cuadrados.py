'''
Generar e imprimir un diccionario donde las claves sean números
enteros entre 1 y 20 (ambos incluidos) y los valores asociados
sean el cuadrado de las claves.
'''

def numero_cuadrado(hasta):
    'Devuelve un diccionario con numeros naturales hasta hasta con su cuadrado'
    nums = {}
    for i in range(hasta):
        nums[i+1] = (i+1) ** 2
    return nums

def imprime_dic(dic):
    'Imprime clave y valor de diccionario en orden ascendente'
    for clave in sorted(dic.keys()):
        print(f'{clave} = {dic[clave]}')

def __main__():
    
    nums = numero_cuadrado(20)
    imprime_dic(nums)

if __name__ == "__main__":
    __main__()