'''
Una librería almacena su lista de precios en un diccionario. Diseñar un
programa para crearlo, incrementar los precios de los cuadernos en un
15%, imprimir un listado con todos los elementos de la lista de precios
e indicar cuál es el ítem más costoso que venden en el comercio
'''
def opcion(texto='Si o no?: '):
    'Pregunta opcion, devuelve 1 para positivo, 0 para negativo, -1 para ninguna'
    si = ['si', 's', '1']
    no = ['no', 'n', '0']
    while True:
        op = input(texto).lower().strip()
        if op in si:
            x = True
            break
        elif op in no:
            x = False
            break
        print('Opcion invalida! si o no?\n')
    return x

def ingreso_float(texto='Ingrese un numero: ', tipo='numero'):
    'Ingresa un numero real positivo'
    while True:
        try:
            num = float(input(texto))
            if num <= 0:
                raise ValueError
            break
        except ValueError:
            print(f'\n* Debe ingresar un {tipo} valido!')
    return num

def crea_lista_precios(categoria='Base/'):
    ''''
    Crea lista de precios por categoria recursivamente
    
    Al ingresar campo vacio pregunta opcion nueva categoria o terminar la carga
    '''
    dic = {}
    nueva = 'Nueva Categoria'
    while True:
        print(f'Categoria: {categoria} ', end='')
        clave = input('Ingrese un producto o "cat" para nueva categoria: ').strip().title()

        if clave and clave not in nueva:
            if clave not in dic or opcion('Este producto ya se encuentra en esta categoria. Desea Sobreescribirlo?: '):
                precio = ingreso_float(texto=f'Ingrese el precio de {clave}: ', tipo='precio')
                dic[clave] = precio
        
        elif clave and clave in nueva:
            if opcion('Desea crear una nueva categoria?: '):
                nueva_cat = input('Ingrese el nombre de la categoria: ').strip().title()
                dic[nueva_cat] = crea_lista_precios(categoria + nueva_cat + r'/')
        else:
            break
    return dic

def aumenta_precio(diccionario, porcentaje):
    'Aumenta el precio de una categoria de productos en dict lista de precios'
    for clave in diccionario.keys():
        if isinstance(diccionario[clave], dict):
            aumenta_precio(diccionario[clave], porcentaje)
        else:
            diccionario[clave] *= (1 + (porcentaje / 100))

def aumenta_categoria(dic, cat, porc):
    'Busca una la categoria recibida en dic recursivamente y le aumenta porc % a todos sus items'
    
    aumento = False
    if cat in ['Todos', 'Base', 'Libreria', 'Total']: # Aumenta todos los productos de la lista
        aumenta_precio(dic, porc)
        aumento = True

    elif cat in dic.keys() and isinstance(dic[cat], dict): # Va directo al solicitado
        aumenta_precio(dic[cat], porc)
        aumento = True

    else: # Lo busca en las sub-categorias
        for clave in dic.keys():
            if isinstance(dic[clave], dict):
                aumento = aumenta_categoria(dic[clave], cat, porc)
                if aumento:
                    break
    return aumento
            
def imprime_dic(diccionario, nivel=0):
    'Imprime recursivamente un diccionario, maneja indentacion para mejor org'
    indent = 3 * nivel
    for item in sorted(diccionario.keys()):
        print(f"{' ' * indent}", end="")

        if isinstance(diccionario[item], dict):
            print(f"> {item}:")
            imprime_dic(diccionario[item], nivel+1)
        
        else:
            print(f"- {item}: ".ljust((40 - indent), '-') + ' $ ' + \
                  f"{diccionario[item]:,.02f}".rjust(6))

def mayor_valor(diccionario, mayor=(None, 0)):
    'Devuelve tupla (clave, valor) con el item de mayor valor en el diccionario'
    for clave, valor in diccionario.items():
        if isinstance(valor, dict):
            mayor = mayor_valor(valor, mayor)
        elif valor > mayor[1]:
            mayor = clave, valor
    return mayor

def __main__():
    
    # Diccionario de prueba
    lista_precios ={
        'Cuadernos': {
            'Cuadernos': {
                'Linea Simple': 100,
                'Cuadriculado': 120,
                'Sin Lineas': 90
            },
            'Libretas': {
                'Carton': 100,
                'Espiral': 130,
                'Perforada': 150
            },
        },
        'Escritura': {
            'Lapices': {
                'Hb': 15,
                'Caja Lapices': 100,
                'Numero 2': 10,
                'De Color': 15,
                'Sacapuntas': 20
            },
            'Marcadores': {
                'De Color': 17,
                'Sharpie': 25,
                'De Acrilico': 20,
            },
            'Borradores': {
                'Liquid Paper': 30,
                'Blanco': 10,
                'Rosado': 10,
                'De Tinta': 15,
                'Cinta Liquidpaper': 50
            }
        },
        'Libros': {
            'Ciencia': {
                'A Brief History of Time': 500,
                'The meaning of it All': 600,
                'Theory of Everything': 550
            },
            'Utilidad': {
                'Guia Telefonica': 100,
                'Clean Code': 420,
                'Automate the Boring Stuff': 300
            }
        }
    }
    try:
        # lista_precios = crea_lista_precios(r'Libreria/')
        
        print('Lista de precios:\n')
        imprime_dic(lista_precios)
        mayor = mayor_valor(lista_precios)
        print(f'\nEl item de mayor valor es {mayor[0]} en ${mayor[1]:.02f}')
        while True:
            if opcion('\nDesea aumentar el precio de alguna categoria?: '):
                categoria = input('Ingrese la categoria/producto a aumentar: ').strip().title()
                porcentaje = ingreso_float(texto='Ingrese el porcentaje de aumento sin el %: ', tipo='porcentaje')
                se_aumento = aumenta_categoria(lista_precios, categoria, porcentaje)
                print()
                if se_aumento:
                    print(f'Se aumentaron los precios de {categoria} con exito!\nNuevos precios:\n')
                    imprime_dic(lista_precios)
                    mayor = mayor_valor(lista_precios)
                    print(f'\nEl item de mayor valor es {mayor[0]} en ${mayor[1]:.02f}')
                else:
                    print(f'No se consiguio la categoria {categoria}')
            else:
                break
    except KeyboardInterrupt:
        print('\n\nHa interrumpido el programa.')
    except Exception as error:
        print(f'Error inesperado :// {error}')

if __name__ == "__main__":
    __main__()
