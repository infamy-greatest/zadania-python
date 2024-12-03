def bubble_sort_max(lista):
    for _ in range(len(lista)):
        for __ in range(len(lista) - 1):
            if lista[__] > lista[__ + 1]:
                lista[__], lista[__ + 1] = lista[__ + 1], lista[__]


def bubble_sort_min(lista):
    for _ in range(len(lista)):
        for __ in range(len(lista) - 1):
            if lista[__] < lista[__ + 1]:
                lista[__], lista[__ + 1] = lista[__ + 1], lista[__]


moja_lista = [5, 3, 6, 7, 2, 1]
bubble_sort_max(moja_lista)
print(moja_lista)
bubble_sort_min(moja_lista)
print(moja_lista)