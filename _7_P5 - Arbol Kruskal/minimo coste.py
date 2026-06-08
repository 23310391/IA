# Algoritmo de Kruskal paso a paso

grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

# ==========================
# UNION-FIND
# ==========================

padre = {}
rango = {}

def make_set(vertices):
    for v in vertices:
        padre[v] = v
        rango[v] = 0

def find(v):
    if padre[v] != v:
        padre[v] = find(padre[v])  # Compresión de caminos
    return padre[v]

def union(v1, v2):
    raiz1 = find(v1)
    raiz2 = find(v2)

    if raiz1 != raiz2:

        if rango[raiz1] > rango[raiz2]:
            padre[raiz2] = raiz1

        elif rango[raiz1] < rango[raiz2]:
            padre[raiz1] = raiz2

        else:
            padre[raiz2] = raiz1
            rango[raiz1] += 1

# ==========================
# KRUSKAL
# ==========================

def kruskal(grafo):

    aristas = []

    # Obtener todas las aristas sin repetir
    for origen in grafo:
        for destino, peso in grafo[origen].items():

            if (destino, origen, peso) not in aristas:
                aristas.append((origen, destino, peso))

    # Ordenar por peso
    aristas.sort(key=lambda x: x[2])

    print("=" * 60)
    print("ARISTAS ORDENADAS POR PESO")
    print("=" * 60)

    for origen, destino, peso in aristas:
        print(f"{origen} -- {destino} = {peso}")

    make_set(grafo.keys())

    mst = []
    peso_total = 0
    paso = 1

    print("\n" + "=" * 60)
    print("INICIO DEL ALGORITMO DE KRUSKAL")
    print("=" * 60)

    for origen, destino, peso in aristas:

        print("\n" + "=" * 60)
        print(f"PASO {paso}")
        print("=" * 60)

        print(f"Evaluando arista: {origen} -- {destino} ({peso})")

        raiz_origen = find(origen)
        raiz_destino = find(destino)

        print(f"Raíz de {origen}: {raiz_origen}")
        print(f"Raíz de {destino}: {raiz_destino}")

        if raiz_origen != raiz_destino:

            print("✓ No forma ciclo, se agrega al árbol")

            union(origen, destino)

            mst.append((origen, destino, peso))
            peso_total += peso

        else:
            print("✗ Forma ciclo, se descarta")

        print("\nÁrbol parcial actual:")

        for a, b, p in mst:
            print(f"{a} -- {b} ({p})")

        print(f"\nPeso acumulado: {peso_total}")

        paso += 1

    return mst, peso_total

# ==========================
# EJECUCIÓN
# ==========================

arbol, peso = kruskal(grafo)

print("\n" + "=" * 60)
print("ÁRBOL DE EXPANSIÓN MÍNIMA FINAL")
print("=" * 60)

for origen, destino, peso_arista in arbol:
    print(f"{origen} -- {destino} ({peso_arista})")

print(f"\nPeso total del árbol: {peso}")