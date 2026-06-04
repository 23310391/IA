'''Insertion Sort
Toma cada elemento y lo inserta en su posición correcta
dentro de la parte ya ordenada de la lista.
'''

iteraciones = 0

def insertion_sort(lista):
    global iteraciones

    for i in range(1, len(lista)):
        temp = lista[i]   # elemento a insertar
        j = i - 1

        # desplazamos elementos mayores a temp una posición a la derecha
        while j >= 0 and lista[j] > temp:
            iteraciones += 1
            lista[j + 1] = lista[j]
            j -= 1

        iteraciones += 1
        lista[j + 1] = temp  # insertamos temp en su posición correcta

    return lista


lista = []
num = int(input("¿Cuántos números tiene tu lista? "))

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print("Lista original:", lista)

lista = insertion_sort(lista)

print("Lista ordenada:", lista)
print(f"Iteraciones (Insertion Sort): {iteraciones}")