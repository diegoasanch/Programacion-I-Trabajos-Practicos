'''
Desarrollar una función que determine si una cadena de caracteres es
capicúa, sin utilizar cadenas auxiliares. Escribir además un programa
que permita verificar su funcionamiento.
'''

from cadenas import esCapicua

def main():
    texto = input('Ingrese un texto para verificar si es capicua: ')
    print()
    if esCapicua(texto):
        print(f'"{texto}" es una cadena de texto capicua!')
    else:
        print(f'"{texto}" no es capicua! :(')
    
if __name__ == "__main__":
    main()