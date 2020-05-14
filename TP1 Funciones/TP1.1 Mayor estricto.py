''' 
Desarrollar una función que reciba tres números positivos
y devuelva el mayor de los tres, sólo si éste es único (mayor
estricto). En caso de no existir el mayor estricto devolver -1.
No utilizar operadores lógicos (and, or, not). Desarrollar también
un programa para ingresar los tres valores, invocar a la función y
mostrar el máximo hallado, o un mensaje informativo si éste no existe. 
'''

from random import randint


def mayor_estricto(x, y, z):
    if x > y:
        if x > z:
            return x
    if y > x:
        if y > z:
            return y
    if z > y:
        if z > x:
            return z
    return -1
    

def main():
    nums = []
    for i in range(3):
        nums.append(randint(0, 10))
        
    x, y, z = nums
    mayor = mayor_estricto(x, y, z)
    
    print()
    print(nums)
    if mayor != -1:
        print(f'El mayor numero ingresado es {mayor}')
    else:
        print('No existe ningun mayor estricto :(')
    
    
if __name__ == '__main__':
    main()
        