'''Shell Sort
Es una mejora de Insertion Sort. En lugar de comparar elementos adyacentes,
compara elementos separados por un "gap" (brecha) que va reduciéndose
hasta llegar a 1, donde se comporta como un Insertion Sort normal.
'''

iteraciones = 0

def shell_sort(lista):
    global iteraciones
    n = len(lista)
    gap = n // 2  # empezamos con un gap de la mitad del tamaño

    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]  # guardamos el elemento actual
            j = i

            # desplazamos elementos mayores a temp hacia adelante
            while j >= gap and lista[j - gap] > temp:
                iteraciones += 1
                lista[j] = lista[j - gap]
                j -= gap

            iteraciones += 1
            lista[j] = temp  # colocamos temp en su posicion correcta

        gap //= 2  # reducimos el gap a la mitad

    return lista


lista = []
num = int(input("¿Cuántos números tiene tu lista? "))

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print("Lista original:", lista)

lista = shell_sort(lista)

print("Lista ordenada:", lista)
print(f"Iteraciones (Shell Sort): {iteraciones}")