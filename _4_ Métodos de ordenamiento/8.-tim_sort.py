'''Tim Sort
Algoritmo híbrido que combina Insertion Sort para sublistas pequeñas (runs)
y Merge Sort para fusionarlas.

este es el metodo que utiliza Python para ordenar listas, es muy eficiente para listas parcialmente ordenadas

'''

iteraciones = 0
RUN = 32  # tamaño de cada run (sublista pequeña)

def insertion_sort(lista, izq, der):
    global iteraciones

    for i in range(izq + 1, der + 1):
        temp = lista[i]
        j = i - 1

        while j >= izq and lista[j] > temp:
            iteraciones += 1
            lista[j + 1] = lista[j]
            j -= 1

        iteraciones += 1
        lista[j + 1] = temp

def merge(lista, izq, medio, der):
    global iteraciones

    izquierda = lista[izq:medio + 1]
    derecha = lista[medio + 1:der + 1]

    i = j = 0
    k = izq

    while i < len(izquierda) and j < len(derecha):
        iteraciones += 1
        if izquierda[i] <= derecha[j]:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1

def tim_sort(lista):
    n = len(lista)

    # fase 1: ordenar cada run con insertion sort
    for i in range(0, n, RUN):
        insertion_sort(lista, i, min(i + RUN - 1, n - 1))

    # fase 2: fusionar runs con merge sort
    size = RUN
    while size < n:
        for izq in range(0, n, 2 * size):
            medio = min(izq + size - 1, n - 1)
            der = min(izq + 2 * size - 1, n - 1)

            if medio < der:  # solo fusionamos si hay dos runs
                merge(lista, izq, medio, der)

        size *= 2  # duplicamos el tamaño de fusion

    return lista


lista = []
num = int(input("¿Cuántos números tiene tu lista? "))

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print("Lista original:", lista)

lista = tim_sort(lista)

print("Lista ordenada:", lista)
print(f"Iteraciones (Tim Sort): {iteraciones}")