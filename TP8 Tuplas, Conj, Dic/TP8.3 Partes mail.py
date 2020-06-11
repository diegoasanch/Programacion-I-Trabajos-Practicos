'''
Desarrollar un programa que utilice una función que reciba como parámetro
una cadena de caracteres conteniendo una dirección de correo electrónico y
devuelva una tupla con las distintas partes que componen dicha dirección.
Ejemplo: alguien@uade.edu.ar -> (alguien, uade, edu, ar).
'''

def partes_mail(mail):
    '''
    Devuelve tupla con las partes mail si es valida, de no ser raise: ValueError
    '''
    valido = False
    if mail.count('@') == 1:
        nombre, direccion = mail.split('@')
        partes = (nombre,)
        if '.' in direccion:
            valido = True
            partes += tuple(direccion.split('.'))
    if not valido:
        raise ValueError(f'Direccion de mail invalida "{mail}"')
    return partes

def __main__():
    
    while True:
        try:
            mail = input('Ingrese una direccion de correo: ')
            if not mail:
                raise KeyboardInterrupt
            partes = partes_mail(mail)
            print(f'Partes del mail: {partes}')
            print('\nIngrese otra direccion o un campo vacio para salir')

        except ValueError as error:
            print(error)
        except KeyboardInterrupt:
            break
    print('Ha abandonado el programa.')
    
if __name__ == "__main__":
    __main__()