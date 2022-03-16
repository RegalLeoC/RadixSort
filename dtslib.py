def counting_sort(list, unidad):
    size = len(list)
    # Crea una lista de apoyo hasta el indice 9
    nlist = [0] * 10

    # Crea una lista en donde se pondran las unidades ordenadas
    aux = [0] * size

    # Guarda en la lista de apoyo la cantidad de veces que una unidad se repite
    for i in range(0, size):
        val = list[i] // unidad
        nlist[int(val % 10)] += 1

    # Se realiza una sumatoria
    for i in range(1, 10):
        nlist[i] = nlist[i] + nlist[i - 1]


    i = size - 1
    while i >= 0:
        val = list[i] // unidad
        aux[nlist[val % 10] - 1] = list[i]
        nlist[val % 10] -= 1
        i -= 1

    # print(f"{aux}")

    #Se transfiere el arreglo ordenada de aux a list, actualizando list en caso que se necesite otra iteración
    for i in range(0, len(list)):
        list[i] = aux[i]


def radix_sort(list):
    max = list[0]
    for i in range(0, len(list)):

        if list[i] > max:
            max = list[i]

    unidad = 1

    while max / unidad > 1:
        counting_sort(list, unidad)
        unidad = unidad * 10

    return list
