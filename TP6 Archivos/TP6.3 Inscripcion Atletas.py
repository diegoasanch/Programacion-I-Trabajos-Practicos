'''
Una institución deportiva necesita clasificar a sus atletas para inscribirlos
en los próximos Juegos Panamericanos. Para eso encargó la realización de un
programa que incluya las siguientes funciones:

GrabarRangoAlturas() Graba en un archivo las alturas de los atletas de
distintas disciplinas, los que se ingresan desde el teclado. Cada dato se debe
grabar en una línea distinta.
Ejemplo:
    <Deporte 1>
    <altura del atleta 1>
    <altura del atleta 2>
    < . . . >
    <Deporte 2>
    <altura del atleta 1>
    <altura del atleta 2>
    < . . . >
    
GrabarPromedio() Graba en un archivo los promedios de las alturas de los
atletas presentes en el archivo generado en el paso anterior. La disciplina
y el promedio deben grabarse en líneas diferentes.
Ejemplo:
    <Deporte 1>
    <Promedio de alturas deporte 1>
    <Deporte 2>
    <Promedio de alturas deporte 2>
    < . . . >

MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos
atletas superan la estatura promedio general. Obtener los datos del segundo
archivo.
'''

from archivos import GrabarRangoAlturas, GrabarPromedio, MostrarMasAltos, escribir_lista

def __main__():
    try:
        arch_deportes, arch_promedios = None, None

        deportes = 'deportes.txt'
        promedios = 'promedios.txt'

        arch_deportes = open(deportes, 'w')
        GrabarRangoAlturas(arch_deportes)
        arch_deportes.close()

        arch_deportes = open(deportes, 'r')
        arch_promedios = open(promedios, 'w')
        GrabarPromedio(arch_deportes, arch_promedios)
        arch_promedios.close()

        arch_promedios = open(promedios, 'r')
        MostrarMasAltos(arch_promedios)
        arch_promedios.close()


    except IOError:
        print('Error, no se logro abrir alguno de los archivos')
    finally:
        for arch in [arch_deportes, arch_promedios]:
            if arch != None:
                arch.close()

if __name__ == "__main__":
    __main__()
