"""
Se requiere hacer un programa para obtener información de locales gastronómicos.
Para ello se cuenta con el archivo “oferta_gastronomica.csv”. 
Las consultas requeridas son:
    - Cantidad de locales por categoría.
    - Listar nombre, barrio y teléfono de locales de una categoría dada.

Nota:realizar al menos una función recursiva.

Formato del archivo: 
    1.Los datos del local se informan por línea, separados por punto y coma( ; ).
    2.Los datos por empresa son: id, nombre, categoría, cocina, ambientación, 
        teléfono, horario, dirección y barrio.
    3.La primera línea del archivo corresponde alencabezado.
"""

def extrae_datos(nombre_archivo):
    '''
    Retorna un diccionario con listas de tuplas de restaurantes agrupados por
    categorias
    '''
    categorias = {}
    try:
        archivo = open(nombre_archivo, 'r')
        
        primera_linea = True
        for registro in archivo:
            if primera_linea:
                primera_linea = False
                continue

            rest = registro.rstrip().split(';')
            nombre, cat, tel, barrio = rest[1], rest[2], rest[5], rest[-1]
            info = (nombre, barrio, tel)
            
            if cat:
                cat = cat.upper()
            else:
                cat = 'DESCONOCIDA'
                
            if cat in categorias:
                categorias[cat] += (info,)
            else:
                categorias[cat] = [info]
    
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no existe!.')
        raise
    
    finally:
        try:
            archivo.close()
        except:
            pass

    return categorias

        
def imprime_cant(categorias):
    '''
    Imprime en orden descendente las categorias pasadas en el diccionario
    categorias junto a la cantidad de restaurantes que esta tiene
    '''

    assert (isinstance(categorias, dict)),'El archivo recibido debe ser un diccionario.'
    assert (categorias != {}), 'El diccionario recibido no tiene ningun elemento.'

    cate, canti = 15, 10

    print('Categoria'.center(cate) + 'Cantidad'.center(canti) + '\n' + ('-' * (cate + canti))) # encabezado

    for cat, cant in sorted(categorias.items(), key= lambda item: item[1]): # ordenamos por valor
        print(cat.center(cate) + str(len(cant)).center(canti))


def consulta_dict(categorias, consulta):
    '''
    Retorna una lista con las tuplas correspondientes a los locales pertenecientes
    a la categoria consulta, de no pertenecer --> raise ValueError
    '''
    assert (isinstance(categorias, dict)), 'El objeto categorias debe ser de la clase diccionario'
    assert (isinstance(consulta, str)), 'El objeto consulta debe ser de la clase string'

    if consulta in categorias:
        return categorias[consulta]
    else:
        raise ValueError


def imprime_locales(locales, consulta):
    '''
    Imprime listado de restaurantes recibidos como tuplas en una lista.
    '''

    nomb, barr, tele = 30, 15, 15 # longitud para centrar columnas

    print(f'Locales de categoria: {consulta} - Cantidad de locales: {len(locales)}')
    print('Nombre'.center(nomb) + 'Barrio'.center(barr) + 'Telefono'.center(tele) + '\n' + ('-' * sum([nomb, barr, tele])))

    for nombre, barrio, tel in sorted(locales, key= lambda rest: rest[0]): # ordenamos alfabeticamente
        print(nombre.center(nomb) + barrio.center(barr) + tel.center(tele))


def __main__():

    try:
        nombre_archivo = "oferta_gastronomica_ORIGINAL.csv"    
        categorias = extrae_datos(nombre_archivo)
        imprime_cant(categorias)

    except IOError:
        print('No se pudo extraer la informacion.')
    
    else:
        while True:
            try:
                cat_consulta = input('\nIngrese una categoria para buscar sus locales: ').upper()
                if not cat_consulta:
                    break

                locales = consulta_dict(categorias, cat_consulta)
                imprime_locales(locales, cat_consulta)
                print()

            except ValueError:
                print(f'\nNo hay regitros de restaurantes pertenecientes a la categoria {cat_consulta}.')
            
            except AssertionError as error:
                print(f'\nError de ejecucion: {error}')
                break

            except KeyboardInterrupt:
                print('\n\nHa abandonado el programa.')
                break


if __name__ == "__main__":
    __main__()
