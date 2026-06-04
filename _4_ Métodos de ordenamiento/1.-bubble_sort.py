'''Bubble Sort
es un metodo de ordenamiento que compara pares de elementos adyacentes y los intercambia si estan en el orden incorrecto
'''
lista = []
cambio = True
num = int(input("Cuantos numeros tiene tu lista? "))
iteraciones = 0

for i in range(num):
    n = float(input("Ingrese un elemento de la lista: "))
    lista.append(n)

print(lista)

while cambio:
    cambio = False
    for x in range(len(lista)-1):
        iteraciones += 1  # contamos cada comparacion
        if lista[x] > lista[x + 1]:
            cambio = True
            lista[x], lista[x + 1] = lista[x + 1], lista[x]

print(lista)
print(f"Iteraciones (Bubble Sort): {iteraciones}")
