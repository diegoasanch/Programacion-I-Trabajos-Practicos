'''
Contraseñas! En general las contraseñas a crear deben cumplir reglas por
seguridad para que sean válidas. Desarrolle un programa que ingrese
contraseñas hasta ingresar una contraseña vacía. A medida que se ingresan
verifique e informe si cumple con las reglas:
    a. No puede comenzar con número.
    b. Debe contener al menos dos números. Contar la cantidad de numeros
      de una cadena mediante una función recursiva.
Resolver utilizando exclusivamente manejo de excepciones y estructura While-True,
creando una nueva excepción o generando una existente (ValueError) cuando no
cumpla alguno de las dos reglas, mostrar mensaje aclaratorio correspondiente en
cada caso
'''

def cantidad_digitos(cadena, i=0):
    'Devuelve cantidad de digitos en una cadena'
    if cadena[i:][0].isdigit():
        empieza_numero = 1
    else:
        empieza_numero = 0
    if len(cadena[i:]) == 1:
        return empieza_numero
    else:
        return empieza_numero + cantidad_digitos(cadena, i+1)

def es_valida(cont):
    'Si cont no es una contraseña valida, raise ValueError'
    if cont[0].isdigit():
        raise ValueError('La contraseña no debe comenzar con un numero.')
    if cantidad_digitos(cont) < 2:
        raise ValueError('La contraseña debe tener al menos dos numeros.')

def __main__():
    
    while True:
        try:
            cont = input('Ingrese una contraseña: ')
            if not cont:
                raise KeyboardInterrupt
            es_valida(cont)
            print('Es una buena contraseña')

        except ValueError as error:
            print(f'Contraseña invalida: {error}')
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    __main__()