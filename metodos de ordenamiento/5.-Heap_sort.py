'''Heap Sort
Utiliza una estructura de datos llamada "heap" (montículo) max-heap,
donde el elemento padre siempre es mayor que sus hijos.
Primero construye el heap, luego extrae el máximo repetidamente
para ordenar la lista.
'''

iteraciones = 0

def heapify(lista, n, i):
    '''
    Mantiene la propiedad del max-heap en un subárbol
    i = índice del nodo raíz del subárbol
    n = tamaño del heap
    '''
    global iteraciones
    mayor = i        # asumimos que la raíz es el mayor
    izq = 2 * i + 1  # hijo izquierdo
    der = 2 * i + 2  # hijo derecho

    iteraciones += 1

    # verificamos si el hijo izquierdo es mayor que la raíz
    if izq < n and lista[izq] > lista[mayor]:
        mayor = izq

    # verificamos si el hijo derecho es mayor que el actual mayor
    if der < n and lista[der] > lista[mayor]:
        mayor = der

    # si el mayor no es la raíz, intercambiamos y continuamos
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)  # aplicamos recursivamente al subárbol afectado


def heap_sort(lista):
    n = len(lista)

    # fase 1: construir el max-heap
    # empezamos desde el último nodo padre hasta la raíz
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # fase 2: extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]  # movemos la raíz (máximo) al final
        heapify(lista, i, 0)  # restauramos el heap con un elemento menos

    return lista


lista = []
num = int(input("¿Cuántos números tiene tu lista? "))

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print("Lista original:", lista)

lista = heap_sort(lista)

print("Lista ordenada:", lista)
print(f"Iteraciones (Heap Sort): {iteraciones}")