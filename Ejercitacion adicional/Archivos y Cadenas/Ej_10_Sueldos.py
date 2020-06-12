digCentralPar = lambda num: not int(num[len(num)//2]) % 2
'Retorna si el digito central de un str de numero es par'

def __main__():

    try:
        sueldos = 'sueldos.csv'
        permanentes = 'permanentes.csv'
        temporales = 'temporales.csv'
        suel = open(sueldos, 'r')
        perm = open(permanentes, 'w')
        temp = open(temporales, 'w')
    except IOError as error:
        print(f'Ocurrio un error abriendo los archivos: {error}')
    else:
        for linea in suel:
            leg = linea.strip().split(';')[0]
            if digCentralPar(leg):
                perm.write(linea)
            else:
                temp.write(linea)
        temp.close()
        perm.close()

if __name__ == "__main__":
    __main__()
