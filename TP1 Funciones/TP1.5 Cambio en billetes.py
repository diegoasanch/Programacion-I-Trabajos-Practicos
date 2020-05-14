'''
Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados al cliente
como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que
existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error
si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona
con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete
de $20, 1 billete de $10 y 3 billetes de $1.
'''

def alcanza(total, pago):
    return pago >= total


def cambio(total, pago, denominaciones):

    billetes = [0, 0, 0, 0, 0, 0, 0] # corresponde a billetes de 500, 100, 50, 20, 10, 5 y 1
    resto = pago - total

    for i in range(len(billetes)):

        billetes[i] = resto // denominaciones[i]
        resto %= denominaciones[i]
    
    return billetes

    
def main():

    total = int(input('Ingrese el monto a cobrar: '))
    pago = int(input('Ingrese el monto con el que pagan: '))
    print()
    
    if alcanza(total, pago):
        
        DENOMINACIONES = [500, 100, 50, 20, 10, 5, 1]
        billetes = cambio(total, pago, DENOMINACIONES)

        print(f'Su vuelto es ${pago - total}\n')
        print('El cambio lo recibira de la siguiente manera:')
        
        for i in range(len(billetes)):

            if billetes[i] > 0:
                print(f'\t{billetes[i]} billetes de ${DENOMINACIONES[i]}')
        
    else:
        print('El monto recibido no es suficiente para realizar el pago :(')

if __name__ == "__main__":
    main()