def contrasenaValida(password, min_nums=2, min_long=8):
    'Levanta Value error si una contraseña pasada es invalida'
    if len(password) < min_long:
        raise ValueError(f'La contraseña debe tener al menos {min_long} caracteres')
    if password[0].isdigit():
        raise ValueError('La contraseña no puede comenzar con un numero')
    if len(list(filter(lambda x: x.isdigit(), password))) < min_nums:
        raise ValueError(f'La contraseña debe tener al menos {min_nums} numeros')

def __main__():

    print('Ingrese contraseñas para verificar su validez.\n\
para salir ingrese un campo vacio.')    
    while True:
        try:
            contr = input('\nIngrese una contraseña: ')
            if contr == '':
                raise KeyboardInterrupt
            contrasenaValida(contr)
            print(' - La contraseña ingresada es valida!')
        except ValueError as error:
            print(f'   Contraseña invalida!: {error}')
        except KeyboardInterrupt:
            break
    print('\n\nFin del programa')

if __name__ == "__main__":
    __main__()
