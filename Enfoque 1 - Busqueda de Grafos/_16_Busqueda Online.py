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

# ============================================================
# UTILIDAD GLOBAL: TRAZADO DE RECORRIDO
# ============================================================

def imprimir_camino(historial, nombre_algoritmo):
    print(f"[{nombre_algoritmo}] Recorrido:")
    for i, nodo in enumerate(historial):
        print(f"Paso {i}: {nodo}")

# 16. BÚSQUEDA ONLINE
# ============================================================

def busqueda_online(inicio, objetivo):
    actual = inicio
    historial = [actual]

    while actual != objetivo:
        vecinos = GRAFO[actual]
        actual = min(vecinos, key=lambda x: HEURISTICA[x])
        historial.append(actual)

    imprimir_camino(historial, "Online")
    print("Llegó al objetivo")

busqueda_online('A', 'F')

