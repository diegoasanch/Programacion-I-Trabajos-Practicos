def ingresarEntero(texto, tipo):
    '''
        Valida la entrada de un numero entero
    '''
    while True:
        try:
            num = int(input(texto))
            break
        except ValueError:
            print(f'{tipo} invalido! Debe ingresar un numero')
    return str(num)

def cargarEmpleados(nombre_arch):
    '''
        Carga los datos de los empleados, 1 por linea, cada item
        esta precedido por dos digitos que indican su longitud
    '''
    try:
        arch = open(nombre_arch, 'w')
    except IOError:
        print(f'No se logro abrir el archivo "{nombre_arch}"')
        raise
    else:
        print('Ingrese los datos por empleado, para finalizar ingrese un legajo vacio.\n')
        legajo = input('Ingrese el numero de legajo: ')
        while legajo != '':
            nombre = input('Ingrese el nombre: ').title()
            cargo = input('Ingrese el cargo: ').title()
            sueldo = ingresarEntero('Ingrese el sueldo: ', 'Sueldo')
            linea = f'{len(legajo):02d}{legajo}{len(nombre):02d}{nombre}{len(cargo):02d}{cargo}{len(sueldo):02d}{sueldo}'
            arch.write(linea + '\n')
            legajo = input('\nIngrese el numero de legajo: ')

        arch.close()

def imprimirEmpleados(nombre_arch):
    '''
    Lee del archivo "nombre_arch" los datos de los empleados guardados en
    formato de columnas de tamaño variable, El archivo debe contener 4 campos por linea
    '''
    try:
        arch = open(nombre_arch, 'r')
    except IOError as error:
        print('Ocurrio un error al abrir el archivo:', error)
    else:
        linea = arch.readline().strip()
        while linea != '':
            i=0
            datos = []
            for _ in range(4): # Leemos los 4 campos
                long = int(linea[i: i+2])
                fin = i + 2 + long
                campo = linea[i+2:fin]
                datos.append(campo)
                i = fin

            leg, nom, car, sue = datos
            sue = float(sue)
            print(f'\nNombre: {nom}\n  -Legajo: {leg.zfill(7)}\n  -Cargo: {car}\n  -Sueldo: $ {sue:.2f}')

            linea = arch.readline().strip()
            

                
