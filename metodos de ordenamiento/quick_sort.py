'''Quick Sort
Elige un elemento "pivote" y divide la lista en dos sublistas:
- Menores o iguales al pivote
- Mayores al pivote
Luego ordena cada sublista recursivamente.
'''

iteraciones = 0

def quick_sort(lista):
    global iteraciones

    if len(lista) <= 1:  # caso base: listas de 0 o 1 elemento ya estan ordenadas
        return lista

    pivote = lista[len(lista) // 2]  # elegimos el elemento del medio como pivote
    menores = []
    iguales = []
    mayores = []

    for elemento in lista:
        iteraciones += 1  # contamos cada comparacion
        if elemento < pivote:
            menores.append(elemento)
        elif elemento == pivote:
            iguales.append(elemento)
        else:
            mayores.append(elemento)

    # ordenamos recursivamente y concatenamos
    return quick_sort(menores) + iguales + quick_sort(mayores)


lista = []
num = int(input("¿Cuántos números tiene tu lista? "))

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print("Lista original:", lista)

lista = quick_sort(lista)

print("Lista ordenada:", lista)
print(f"Iteraciones (Quick Sort): {iteraciones}")