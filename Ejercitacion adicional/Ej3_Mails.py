'''
Ejercicio 3: realizar un programa que lea un archivo de mails e informe:
    a)Porcentaje de mails cuyo dominio esté en país de Méjico (mx)
    b)Dominio/s más frecuente/s y frecuencia de este/os
    c)Listado de dominios que aparecen más de una vez ordenado
      alfabéticamente
    d)Cantidad de mails inválidos
'''
def masDeDosCar(sec):
    'Determina si todos los elementos de la secuencia tienen mas de dos caracteres'
    for el in sec:
        if len(el) < 2:
            valido = False
            break
    else:
        valido = True
    return valido

def extrae_info(archivo):
    '''
    Extrae la informacion del archivo csv de mails
    Retorna: invalidos, dominios, veces (que aparece cada dominio)
    '''
    invalidos = 0
    dominios = []
    veces = []
    for linea in archivo:
        try:
            assert(' ' not in linea.strip()) # No tiene espacios en el correo
            comp = linea.strip().split('@')
            assert (len(comp) == 2) # Check tiene partes a ambos lados del @
            sitio = comp[1]
            assert (sitio[-1] != '.') # Check mail no termina en .
            assert ('.' in sitio) # tiene . la direccion 
            dom, *extension = sitio.split('.')
            assert (masDeDosCar([dom] + extension)) # esas extensiones tienen dos o mas caracteres

            if sitio not in dominios:
                dominios.append(sitio)
                veces.append(1)
            else:
                veces[dominios.index(sitio)] += 1
        except AssertionError:
            invalidos += 1
    return invalidos, dominios, veces

def DatosParaReportajeDom(dominios):
    '''
    Extrae los datos: dominio mas frecuente, extensiones del dominio mas frec,
    veces que la extension .mx aparece, lista con los dominios que estan mas de una vez
    ordenada alfabeticamente

    Recibe matriz con:
        columna 0 = nombres del dominio
        columna 1 = cantidad de veces que aparece el dominio
    Retorna [mas_frec, mas_frec_ext], mex, repetidos
    '''
    sitios, veces = dominios
    mex = 0
    reps = []
    mas_frec = sitios[veces.index(max(veces))]
    for i, sitio in enumerate(sitios):
        dom = sitio.split('.')

        if sitio[-2:] == "mx":
            mex += veces[i] # sumamos la cantidad de veces que aparece ese sitio
        if veces[i] > 1 and dom[0] not in reps: 
            reps.append(dom[0])
    reps.sort()
    return mas_frec, mex, reps
    
def imprimeReportaje(porc_mex, mas_frec, reps, inv):
    'Imprime reportaje de mails'
    print(f' - El {porc_mex:.2f}% de los mails esta registrado en Mexico')
    print(f' - El dominio mas frecuente es {mas_frec}')
    print(' - Los dominios que aparecen mas de una vez son:')
    print("   > " + "\n   > ".join(reps))
    print(f' - Se detectaron un total de {inv} direcciones de correo invalidas.')
    

def __main__():

    try:
        filename = 'lista_mails.csv'
        archivo = open(filename, 'r')
    except IOError:
        print(f'No se logro abrir el archivo {filename}')
    else:
        inv, *doms = extrae_info(archivo)
        total = sum(doms[1]) # total de mails validos
        archivo.close()

        mas_frec, mex, reps = DatosParaReportajeDom(doms)
        if total != 0:
            porc = (mex / total) * 100
        else:
            porc = 0
        imprimeReportaje(porc, mas_frec, reps, inv)
        
if __name__ == "__main__":
    __main__()
