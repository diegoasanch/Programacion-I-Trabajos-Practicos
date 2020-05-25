def extraeNotas(archivo):
    '''Extra una lista con la cantidad de notas por nota

    Recibe archivo de notas abierto, deben estar en el formato de 
    longitud de columna fijo, nota entre las posiciones 6 y 7
    '''
    notas = [0] * 11
    for reg in archivo:
        nota = int(reg[6:8].strip())
        notas[nota] += 1
    return notas

def imprimeNotas(notas):
    'Imprime un listado de cuantos alumnos sacaron cada nota'
    print('Nota    Cant. Alumnos')
    for i, cant in enumerate(notas):
        print(str(i).center(6) + str(cant).center(14))

def __main__():

    try:
        filename = 'alumnos.csv'
        archivo = open(filename, 'r')
    except FileNotFoundError:
        print(f'No se logro abrir el archivo "{filename}"')
    else:
        notas = extraeNotas(archivo)
        archivo.close()
        imprimeNotas(notas)

if __name__ == "__main__":
    __main__()
