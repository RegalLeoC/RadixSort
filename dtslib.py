def counting_sort(list, unidad):
    size = len(list)
    print(f"Lista {list}")
    # Crea una lista de apoyo hasta el indice 9
    nlist = [0] * 10

    # Crea una lista en donde se pondran las unidades ordenadas
    aux = [0] * size

    # Guarda en la lista de apoyo la cantidad de veces que una unidad se repite
    for i in range(0, size):
        val = list[i] // unidad
        nlist[int(val % 10)] += 1

    for i in range(1, 10):
        nlist[i] = nlist[i] + nlist[i - 1]


    # i = size - 1
    # while i >= 1:
    #     nlist[i] = nlist[i - 1]
    #     i = i - 1

    # for i in range(size-1, 0, -1):
    #     val = list[i] // unidad
    #     nlist[int(val % 10)] = nlist[int(val % 10) - 1]

    # nlist[0] = 0
    # print(nlist)

    # for i in range(size - 1, 0, -1):
    #     val = list[i] // unidad
    #     aux[nlist[int(val % 10)] - 1] = list[i]
    #     nlist[int(val % 10)] = nlist[int(val % 10)] + 1
    i = 0
    while i < size:
        val = list[i] // unidad
        print(f"{aux}")
        print(nlist[val % 10]-1)
        aux[nlist[val % 10] - 1] = list[i]
        nlist[val % 10] -= 1
        i += 1

    # for i in range(0, size):
    #     for f in range(0, size):
    #         val = list[i] // unidad
    #         if list[i] == f:
    #             aux[nlist[f]] = list[i]
    #             nlist[f] = nlist[f] + 1

    # # for i in range(0, size):
    #     val = list[i] // unidad
    #     print(nlist[val % 10] - 1)
    #     print(f"{aux}")
    #     aux[nlist[val % 10] - 1] = list[i]
    #     nlist[val % 10] += 1

    # print(f"{nlist}")
    print(f"{aux}")

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
