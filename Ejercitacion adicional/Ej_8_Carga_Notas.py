def validaNum(num, valor_max):
    'Valida si un ingreso del usuario cumple con ser numero y menos a valor_max'
    valido = False
    if num.isdigit():
        if int(num) in range(0, valor_max+1):
            valido = True
    return valido

def ingreso(texto, valor_max, escape = '-1'):
    '''Ingresa un numero menor o igual a valor max, al ingresar el valor
    escape se dispara un KeyboardInterrupt
    '''
    while True:
        num = input(texto)
        if num == escape:
            raise KeyboardInterrupt('Ingreso de valor de escape')
        if validaNum(num, valor_max):
            break
        print(f'  > Dato invalido! debe ingresar un entero entre 1 y {valor_max}')
    return int(num)

def __main__():
    
    try:
        filename = 'alumnos.csv'
        notas = open(filename, 'w')
    except IOError:
        print(f'No se logro abrir el archivo "{filename}"')
    else:
        while True:
            try:
                leg = ingreso('Ingrese el numero de legajo: ', valor_max=9999)
                nota = ingreso('Ingrese la nota: ', valor_max=10)
                if nota in range(4, 7):
                    estado = 'Aprobado'
                elif nota >= 7:
                    estado = 'Promocionado'
                else:
                    estado = 'Desaprobado'
                print(estado)
                reg = f'{str(leg).ljust(6)}{str(nota).ljust(2)}{estado.ljust(12)}\n'
                notas.write(reg)
            except KeyboardInterrupt:
                print('\n\nFin de la carga de datos')
                break
        notas.close()

if __name__ == "__main__":
    __main__()
