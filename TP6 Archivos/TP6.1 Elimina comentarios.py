'''
Desarrollar un programa para eliminar todos los comentarios de un programa
escrito en lenguaje Python. Tener en cuenta que los comentarios comienzan
con el signo # (siempre que éste no se encuentre encerrado entre comillas
simples o dobles) y que también se considera comentario a las cadenas de
documentación (docstrings).
'''

from archivos import elimina_comentarios, opcion, escribir_lista

def __main__():

    while True:
        try:
            filename = input('Ingrese el nombre del archivo a limpiar: ')

            # Abrimos el archivo para leerlo
            archivo = open(filename, mode='r')
            texto_limpio = elimina_comentarios(archivo)
            archivo.close()

            # Lo abrimos en modo escritura para escribir el texto limpio
            archivo = open(filename, 'w')
            escribir_lista(archivo, texto_limpio)
            archivo.close()
            break

        except FileNotFoundError:
            print(f'No se encontro el archivo {filename}')
            if opcion('Desea reintentar?: '):
                continue
            break

if __name__ == "__main__":
    __main__()
