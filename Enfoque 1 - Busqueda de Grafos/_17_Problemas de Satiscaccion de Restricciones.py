GRAFO = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

HEURISTICA = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

# ============================================================
# UTILIDAD
# ============================================================

def imprimir_camino(historial, nombre):
    print(f"\n[{nombre}] Recorrido:")
    for i, n in enumerate(historial):
        print(f"Paso {i}: {n}")

# ============================================================

variables = ['A', 'B', 'C']
colores = ['Rojo', 'Verde']
restricciones = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}


def es_valido(var, color, asignacion):
    for vecino in restricciones[var]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

