'''
Arbol Parcial Minimo de Prim

'''


grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

def prim(grafo, inicio):
    
    vertices_mst = {inicio}
    aristas_mst = []
    peso_total = 0
    paso = 1

    print("=" * 60)
    print("INICIO DEL ALGORITMO DE PRIM")
    print("=" * 60)
    print(f"\nNodo inicial: {inicio}")

    while len(vertices_mst) < len(grafo):

        mejor_arista = None
        menor_peso = float('inf')

        print("\n" + "=" * 60)
        print(f"PASO {paso}")
        print("=" * 60)

        print(f"\nVértices en el árbol: {vertices_mst}")

        print("\nAristas candidatas:")

        for origen in vertices_mst:
            for destino, peso in grafo[origen].items():

                if destino not in vertices_mst:

                    print(f"{origen} -> {destino}  Peso = {peso}")

                    if peso < menor_peso:
                        menor_peso = peso
                        mejor_arista = (origen, destino, peso)

        origen, destino, peso = mejor_arista

        print("\nArista seleccionada:")
        print(f"{origen} -> {destino}  Peso = {peso}")

        vertices_mst.add(destino)
        aristas_mst.append(mejor_arista)
        peso_total += peso

        print("\nÁrbol parcial actual:")

        for a, b, p in aristas_mst:
            print(f"{a} -- {b} ({p})")

        print(f"\nPeso acumulado: {peso_total}")

        paso += 1

    return aristas_mst, peso_total


# Ejecutar algoritmo
arbol, peso = prim(grafo, 'A')

print("\n" + "=" * 60)
print("ÁRBOL DE EXPANSIÓN MÍNIMA FINAL")
print("=" * 60)

for origen, destino, peso_arista in arbol:
    print(f"{origen} -- {destino} ({peso_arista})")

print(f"\nPeso total del árbol: {peso}")