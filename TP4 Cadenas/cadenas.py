esCapicua = lambda cadena: cadena == cadena[::-1]
'determina si una "cadena" es capicua'

esPar = lambda num: num % 2 == 0

ultimosN = lambda cadena, N: cadena[-N:]
'devuelve subcadena con los ultimos N car de cadena'

separaPalabras = lambda cadena, sep=' ': [palabra.strip(sep) for palabra in cadena.split(sep)]
'devuelve una lista con las palabras de una cadena separadas por "sep"'

def imprimirCentrado(texto, ancho=80):
    '''Imprime la cadena de caracteres "texto" centrada
    dentro de un "ancho"
    '''
    if len(texto) <= ancho:
        print(texto.center(ancho, ' '))
    else:
        print('La cadena de caracteres es muy larga para esta pantalla :(')

def extraeClaves(master):
    'Extrae las claves 1 y 2 de la clave maestra'
    clave1, clave2 = '', ''
    for i, digito in enumerate(master):
        if not esPar(i + 1):
            clave1 += digito
        else:
            clave2 += digito
    return clave1, clave2

def ingresaNum():
    '''Valida la entrada de un numero entero+ y lo devuelve como int o
    -1 si no se ingreso ningun valor'''

    escape = ['fin', 'salir', 'f', 's', '-1']
    num = input()
    while not num.isdigit() and num.lower() not in escape:
        print("Debe ingresar un numero entero positivo o 'fin' para salir\n")
        num = input('Ingrese un numero entero: ')
    if num.isdigit():
        num = int(num)
    else:
        num = -1
    return num

def ingresaNumRango(minimo, maximo):
    '''Valida la entrada de un numero entero positivo entre minimo y maximo
    y lo devuelve como int o -1 si no se ingreso ningun valor'''

    num = ingresaNum()
    while num not in range(minimo, maximo + 1) and num != -1:
        print(f'Debe ingresar un numero entre {minimo} y {maximo}')
        num = ingresaNum()
    return num

def intRomano(num):
    '''Convierte un numero entero entre 1 y 3999 a numero romano
    
    toma: int, devuelve: str'''
    letras = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    divs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ''
    for i, div in enumerate(divs):
        cant = num // div
        rom +=  (letras[i] * cant)
        num %= div

    return rom

def filtrar_palabrasCiclos(cadena, N):
    '''Recibe un str y un numero entero N
    
    Devuelve un str con las palabras de la frase original que tengan
    N o mas caracteres'''

    frase = cadena.split()
    filt = ''

    for palabra in frase:
        if len(palabra) >= N:
            filt += (palabra + ' ')
        
    return filt.rstrip()

def filtrar_palabrasComp(cadena, N):
    '''Recibe un str y un numero entero N
    
    Devuelve un str con las palabras de la frase original que tengan
    N o mas caracteres'''

    palabras = [pal for pal in cadena.split() if len(pal) >= int(N)]
    return ' '.join(palabras)

def filtrar_palabrasFilt(cadena, N):
    '''Recibe un str y un numero entero N
    
    Devuelve un str con las palabras de la frase original que tengan
    N o mas caracteres'''
    return ' '.join(list(filter(lambda x: len(x) >= N, cadena.split())))

def extraeSubCadena(cadena, pos, long):
    'Extrae de "cadena" la sub-cadena desde "pos" hasta "pos" + "long"'
    subcadena = cadena[pos: pos + long]
    return subcadena

def extraeSubCadena2(cadena, pos, long):
    'Extrae de "cadena" la sub-cadena desde "pos" hasta "pos" + "long"'
    subcadena = ''
    if pos < len(cadena):
        hasta = pos + long if pos + long < len(cadena) else len(cadena)
        for i in range(pos, hasta):
            subcadena += cadena[i]
    return subcadena

def eliminaSubCadena(cadena, pos, long):
    'Devuelve "cadena" sin los elementos de las posiciones entre "pos" y "pos + long"'
    nueva = cadena[: pos] + cadena[pos + long:]
    return nueva

def eliminaSubCadena2(cadena, pos, long):
    'Devuelve "cadena" sin los elementos de las posiciones entre "pos" y "pos + long"'
    nueva = ''
    for i in range(len(cadena)):
        if i not in range(pos, pos + long):
            nueva += cadena[i]
    return nueva

def ordenarAlfCadena(cadena):
    'Devuelve un str con las palabras de "cadena" ordenadas alfabeticamente'

    palabras = separaPalabras(cadena)
    palabras.sort()
    return ' '.join(palabras)

def cuentaCar(cadena):
    'Retorna la cantidad de letras y la cantidad de numeros en "cadena"'
    lets, nums = 0, 0
    for caracter in cadena:
        if caracter.isalpha():
            lets += 1
        elif caracter.isdigit():
            nums += 1
    return lets, nums

def mayusSinEspacio(cadena):
    '''Retorna un str con las palabras de "cadena" cada una con su
    primera letra en mayuscula y sin espacios
    '''
    palabras = [pal.strip().capitalize() for pal in separaPalabras(cadena)]
    return ''.join(palabras)

def separaPal(cadena):
    nueva = ''
    for letra in cadena:
        if letra.isupper():
            nueva += ' ' + letra
        else:
            nueva += letra
    return nueva

def reemplazaPal(cadena, vieja, nueva):
    '''Reemplaza las apariciones de "vieja" en "cadena" por "nueva"
    Devuelve nuevo str e int = cantidad de reemplazos'''
    cant = 0
    palabras = separaPalabras(cadena)
    for i, pal in enumerate(palabras):
        if pal == vieja:
            palabras[i] = nueva
            cant += 1
    return ' '.join(palabras), cant

def cuentaSubCadena(cadena, subcadena):
    'Cuenta las apariciones de subcadena dentro de cadena sin diferencia mayus'
    i_sub = 0  # subindice para recorrer la subcadena
    veces = 0
    for letra in cadena.lower():
        if letra == subcadena[i_sub].lower():
            if i_sub < (len(subcadena) - 1):
                i_sub += 1
            else:
                i_sub = 0
                veces += 1
    return veces

def creaBarajaEsp():
    'Devuelve una lista con los naipes de la baraja española'
    famil = ['oros', 'copas', 'espadas', 'bastos']
    denom = [
        'as', 'dos', 'tres', 'cuatro', 'cinco', 'seis',
        'siete', 'ocho', 'nueve', 'sota', 'caballo', 'rey']
    mazo = []
    for familia in famil:
        mazo += [numero.title() +' de '+ familia.title() for numero in denom]
    return mazo

def enteroaLetra(num):
    'Devuelve un str expresando el int "num" en palabras'
    unidades = [
        '','uno', 'dos', 'tres', 'cuatro', 'cinco',
        'seis', 'siete', 'ocho', 'nueve']
    diez = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieci']
    veint_a_nov = [
        'veinte', 'veinti','', 'trein', 'cuaren', 'cincuen',
        'sesen', 'seten', 'ochen', 'noven']
    cent_a_mil = ['cien', 'cientos']
    pass

    