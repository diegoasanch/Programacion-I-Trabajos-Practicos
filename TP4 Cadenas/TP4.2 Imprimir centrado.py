'''
Leer una cadena de caracteres e imprimirla centrada en pantalla.
Suponer que la misma tiene 80 columnas.
'''

from cadenas import imprimirCentrado

def main():
    texto = input('Ingrese un texto para imprimir centrado: ')
    print()
    imprimirCentrado(texto)

if __name__ == "__main__":
    main()