'''
Ej 2
Cree un programa que ingrese primero el apellido y a continuación el nombre,
deberá crear una cadena que contenga Apellido una coma un espacio y el Nombre
(si tiene doble apellido o doble nombre, debe quedar con un solo espacio entre
cada palabra). Luego se solicita que lo muestre por pantalla centrado
(Considerando una pantalla con 80 columnas de ancho) y alternando mayúsculas
y minúsculas por palabra. Ejemplo: Martinez, Juan Pedro
MaRtInEz, JuAn PeDrO
'''

def ingresaNombre(texto):
    'Ingresa un nombre y lo retorna con mayusc y sin dobles espacios'
    nombre = input(texto).strip()
    return eliminaDobleEspacio(nombre)

def eliminaDobleEspacio(string):
    'Retorna a "string" sin doble espacio si lo contiene'
    while '  ' in string:
        string = string.replace('  ', ' ')
    return string

def intercalaMayus(texto):
    'Intercala mayusculas con minusculas en texto'
    may = True
    nuevo = ''
    for letra in texto:
        if letra.isalpha():
            if may:
                x = letra.upper()
            else:
                x = letra.lower()
            may = not may
        else:
            x = letra
        nuevo += x
    return nuevo

def imprimeCentrado(texto, ancho=80):
    'Imprime centrado en una pantalla de ancho default= 80'
    print(texto.center(ancho))

def __main__():
    
    print('Imprime nombres centrados por pantalla.')
    print('Para salir ingrese un apellido vacio.')
    while True:
        apellido = ingresaNombre('Ingrese el apellido: ')
        if apellido != '':
            nombre = ingresaNombre('Ingrese el nombre: ')
            texto = f'{apellido.title()}, {nombre.title()}'
            texto = intercalaMayus(texto)
            print()
            imprimeCentrado(texto)
            print()
        else:
            break

if __name__ == "__main__":
    __main__()
