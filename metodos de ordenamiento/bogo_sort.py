'''Bogo Sort
El algoritmo más ineficiente que existe:
mezcla la lista aleatoriamente una y otra vez
hasta que por casualidad quede ordenada.
'''

import random

iteraciones = 0

def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def bogo_sort(lista):
    global iteraciones
    while not esta_ordenada(lista):
        iteraciones += 1  # contamos cada mezcla aleatoria
        random.shuffle(lista)
    return lista


lista = []
num = int(input("¿Cuántos números tiene tu lista? "))

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print("Lista original:", lista)

lista = bogo_sort(lista)

print("Lista ordenada:", lista)
print(f"Iteraciones (Bogo Sort): {iteraciones}")