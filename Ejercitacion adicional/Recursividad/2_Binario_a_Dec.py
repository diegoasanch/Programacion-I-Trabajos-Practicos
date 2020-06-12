'''
Desarrollar una función recursiva que reciba un número binario y lo devuelva
convertido a base decimal. Creando una excepción o generando ValueError en
caso de recibir un número que no es binario o un número negativo con el
mensaje aclaratorio correspondiente a cada error.
Resolver de dos formas distintas:
    a) Resolver utilizando raise
    b) Resolver utilizando assert
'''

def binario_a_int(binario, i=0):
    'Convierte un numero binario a entero'
    
    assert type(binario) == int, ('No ingreso un numero')
    assert binario > 0, ('No se aceptan numeros negativos')
    
    ultimo = binario % 10

    if ultimo not in (0, 1):
        raise ValueError(f'Digito {ultimo} no es binario.')
    ultimo *= (2**i)
    if binario > 1:
        return ultimo + binario_a_int(binario // 10, i+1)
    else:
        return ultimo

def __main__():
    
    while True:
        try:
            binario = int(input('Ingrese un numero binario para convertir a base dec: '))
            ent = binario_a_int(binario)
        except (ValueError, AssertionError) as error:
            print(f'Error de conversion: {error}')
        else:
            print(f'El binario {binario} en base decimal es {ent}')
            break

if __name__ == "__main__":
    __main__()
