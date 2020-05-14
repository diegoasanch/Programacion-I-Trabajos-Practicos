'''
Intercalar los elementos de una lista entre los elementos
de otra. La intercalación deberá realizarse exclusivamente
mediante la técnica de rebanadas y no se creará una lista
nueva sino que se modificará la primera. Por ejemplo, si
lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá
quedar como [8, 5, 1, 9, 3, 7]
'''

from random import randint
from listas import intercalar, cargaRandom

def main():
    lista1 = cargaRandom(randint(3,10))
    lista2 = cargaRandom(randint(3,10))
    print(lista1)
    print(lista2)
    
    intercalar(lista1, lista2)
    print(lista1)

if __name__ == "__main__":
    main()