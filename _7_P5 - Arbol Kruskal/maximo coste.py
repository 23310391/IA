# Algoritmo de Kruskal para Árbol de Máximo Coste

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
        padre[v] = find(padre[v])
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
# KRUSKAL MÁXIMO
# ==========================

def kruskal_maximo(grafo):

    aristas = []

    # Obtener aristas sin repetir
    for origen in grafo:
        for destino, peso in grafo[origen].items():

            if (destino, origen, peso) not in aristas:
                aristas.append((origen, destino, peso))

    # Ordenar de MAYOR a MENOR
    aristas.sort(key=lambda x: x[2], reverse=True)

    print("=" * 60)
    print("ARISTAS ORDENADAS DE MAYOR A MENOR")
    print("=" * 60)

    for origen, destino, peso in aristas:
        print(f"{origen} -- {destino} = {peso}")

    make_set(grafo.keys())

    arbol_maximo = []
    peso_total = 0
    paso = 1

    for origen, destino, peso in aristas:

        print("\n" + "=" * 60)
        print(f"PASO {paso}")
        print("=" * 60)

        print(f"Evaluando: {origen} -- {destino} ({peso})")

        if find(origen) != find(destino):

            print("✓ Se agrega al árbol")

            union(origen, destino)

            arbol_maximo.append((origen, destino, peso))
            peso_total += peso

        else:
            print("✗ Se descarta (forma ciclo)")

        print("\nÁrbol actual:")

        for a, b, p in arbol_maximo:
            print(f"{a} -- {b} ({p})")

        print(f"\nPeso acumulado: {peso_total}")

        paso += 1

    return arbol_maximo, peso_total

# ==========================
# EJECUCIÓN
# ==========================

arbol, peso = kruskal_maximo(grafo)

print("\n" + "=" * 60)
print("ÁRBOL DE MÁXIMO COSTE")
print("=" * 60)

for origen, destino, p in arbol:
    print(f"{origen} -- {destino} ({p})")

print(f"\nPeso total = {peso}")