'''Selection Sort
Es un método de ordenamiento que busca el elemento mínimo de la lista
y lo coloca en su posición correcta en cada iteración.
'''
lista = []
num = int(input("Cuantos numeros tiene tu lista? "))
iteraciones = 0

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print(lista)

for i in range(len(lista)):
    indice_minimo = i
    for j in range(i + 1, len(lista)):
        iteraciones += 1  # contamos cada comparacion
        if lista[j] < lista[indice_minimo]:
            indice_minimo = j

    lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

print(lista)
print(f"Iteraciones (Selection Sort): {iteraciones}")