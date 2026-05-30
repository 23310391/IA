'''Merge Sort
Divide la lista en mitades recursivamente hasta tener sublistas de 1 elemento,
luego las fusiona en orden.
'''

iteraciones = 0

def merge_sort(lista):
    global iteraciones

    if len(lista) <= 1:  # caso base
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])   # ordenamos mitad izquierda
    derecha = merge_sort(lista[medio:])     # ordenamos mitad derecha

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    global iteraciones
    resultado = []
    i = j = 0

    # fusionamos comparando elemento por elemento
    while i < len(izquierda) and j < len(derecha):
        iteraciones += 1
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])  # agregamos los elementos restantes
    resultado.extend(derecha[j:])
    return resultado


lista = []
num = int(input("¿Cuántos números tiene tu lista? "))

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print("Lista original:", lista)

lista = merge_sort(lista)

print("Lista ordenada:", lista)
print(f"Iteraciones (Merge Sort): {iteraciones}")