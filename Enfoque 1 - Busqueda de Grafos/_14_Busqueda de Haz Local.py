GRAFO = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heurística para algunos algoritmos (estimación al objetivo F)
HEURISTICA = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

# UTILIDAD GLOBAL: TRAZADO DE RECORRIDO
# ============================================================

def imprimir_camino(historial, nombre_algoritmo):
    print(f"[{nombre_algoritmo}] Recorrido:")
    for i, nodo in enumerate(historial):
        print(f"Paso {i}: {nodo}")

# 14. BEAM SEARCH
# ============================================================

def beam_search(inicio, objetivo, k=2):
    frontera = [inicio]
    nivel = 0

    while frontera:
        print(f"Nivel {nivel}: {frontera}")

        if objetivo in frontera:
            print("Encontrado en frontera")
            return

        candidatos = []
        for nodo in frontera:
            candidatos.extend(GRAFO[nodo])

        frontera = sorted(candidatos, key=lambda x: HEURISTICA[x])[:k]
        nivel += 1

    print("No encontrado")

beam_search('A', 'F')

