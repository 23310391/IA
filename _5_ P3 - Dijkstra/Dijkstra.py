import math

# Grafo representado como diccionario
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

def mostrar_distancias(distancias):
    print("\nDistancias actuales:")
    for nodo, distancia in distancias.items():
        if distancia == math.inf:
            print(f"{nodo}: ∞")
        else:
            print(f"{nodo}: {distancia}")

def dijkstra(grafo, inicio):
    # Inicialización
    distancias = {nodo: math.inf for nodo in grafo}
    distancias[inicio] = 0

    visitados = set()
    anteriores = {}

    paso = 1

    while len(visitados) < len(grafo):

        # Buscar el nodo no visitado con menor distancia
        nodo_actual = None
        menor_distancia = math.inf

        for nodo in grafo:
            if nodo not in visitados and distancias[nodo] < menor_distancia:
                menor_distancia = distancias[nodo]
                nodo_actual = nodo

        if nodo_actual is None:
            break

        print("\n" + "=" * 50)
        print(f"PASO {paso}")
        print("=" * 50)

        print(f"\nNodo seleccionado: {nodo_actual}")
        print(f"Distancia mínima encontrada: {distancias[nodo_actual]}")

        visitados.add(nodo_actual)

        print("\nVecinos a evaluar:")

        for vecino, peso in grafo[nodo_actual].items():

            if vecino not in visitados:

                nueva_distancia = distancias[nodo_actual] + peso

                print(
                    f"\nEvaluando {nodo_actual} -> {vecino}"
                )
                print(
                    f"Distancia actual de {vecino}: "
                    f"{distancias[vecino] if distancias[vecino] != math.inf else '∞'}"
                )
                print(
                    f"Nueva distancia posible: "
                    f"{distancias[nodo_actual]} + {peso} = {nueva_distancia}"
                )

                if nueva_distancia < distancias[vecino]:
                    print(">>> Se actualiza la distancia")
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual
                else:
                    print(">>> No se actualiza")

        mostrar_distancias(distancias)

        print("\nNodos visitados:", visitados)

        paso += 1

    return distancias, anteriores

# Ejecutar algoritmo
inicio = 'A'

distancias, anteriores = dijkstra(grafo, inicio)

print("\n" + "=" * 50)
print("RESULTADO FINAL")
print("=" * 50)

for nodo, distancia in distancias.items():
    print(f"Distancia mínima desde {inicio} hasta {nodo}: {distancia}")