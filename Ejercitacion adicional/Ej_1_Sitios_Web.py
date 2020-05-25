sitiosAR = lambda sitios: len(list(filter(lambda url: url[-2:] == 'ar', sitios)))
'Devuelve la cantidad de sitios web registrados en argentina'

eliminaGuionMedio = lambda sitios: list(filter(lambda url: '-' not in url, sitios))
'Elimina de la lista "sitios" aquellos sitios que tienen "-" en su url'

def esSitioValido(url):
    'Determina si una direccion web es valida'
    extensiones =  ['com', 'org', 'net', 'edu']
    valido = False
    if url.count('.') >= 2:
        prefijo, sitio, *extension = url.split('.') 
        if prefijo == 'www':
            if extension[0] in extensiones:
                if len(sitio) >= 1 and sitio[0] not in '-_ ':
                    for letra in sitio:
                        if not letra.isalnum() and letra not in '-_':
                            break
                    else:
                        valido = True
    return valido

def cargaSitiosWeb():
    'Devuelve una lista con sitios web validos'
    sitios = []
    while True:
        url = input('Ingrese una direccion web: ').strip().lower()
        if url == '':
            break
        if esSitioValido(url) and url not in sitios:
            sitios.append(url)
        else:
            print(f'"{url}" no es una direccion valida')
    return sorted(sitios)

def imprimeListado(sitios):
    'Imprime un listado de los sitios web cargados'
    for sitio in sitios:
        print(f' - {sitio}')

def imprimeListadoPais(sitios):
    'Imprime un listado de sitios registrados por pais'
    paises = []
    cant = []
    for sitio in sitios:
        pais = sitio.split('.')[-1]
        if pais == 'com':
            pais = 'us'
        if pais not in paises:
            paises.append(pais)
            cant.append(1)
        else:
            cant[paises.index(pais)] += 1
    for i, pais in enumerate(paises):
        print(f' - Hay {cant[i]} sitios registrados en {pais.upper()}')

def ingresaExt(texto='\nIngrese una extension para eliminar: '):
    'Retorna una extension valida'
    while True:
        ext = input(texto).lstrip('.')
        if len(ext) == 3 and ext.isalpha():
            break
        else:
            print('Extension invalida, debe tener 3 caracteres y ser alfabetica.')
    return ext

def eliminaExtension(sitios, ext):
    'Elimina los sitios que terminan en la extension recibida'
    elims = 0
    for i in range(len(sitios)-1, -1, -1): # reversa para evitar index out of range
        if sitios[i].split('.')[2] == ext:
            del sitios[i]
            elims += 1
    return elims

def __main__():

    print('Carga de sitios web.')
    print('Ingrese un campo vacio para finalizar la carga.\n')
    sitios = cargaSitiosWeb()
    arg = sitiosAR(sitios)

    print('Sitios cargados')
    imprimeListado(sitios)
    print(f'Hay {arg} sitios registrados en argentina')

    print('\nDirecciones registradas por pais.')
    imprimeListadoPais(sitios)

    sitios = eliminaGuionMedio(sitios)
    print('\nSitios sin guion medio "-":')
    imprimeListado(sitios)

    extension = ingresaExt()
    elims = eliminaExtension(sitios, extension)
    print(f'Sitios sin extension {extension}:')
    imprimeListado(sitios)
    print(f'Se eliminaron {elims} sitios con la extension .{extension}')

if __name__ == "__main__":
    __main__()
