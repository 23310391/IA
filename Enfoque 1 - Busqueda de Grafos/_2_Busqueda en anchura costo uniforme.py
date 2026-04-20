'''
busqueda de costo uniforme
el grafo ahora tiene pesos
no da el camino exacto, si da el camino de menor costo
'''

GRAFO_COSTO = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
import heapq

# ====================== RECORRIDO ======================================

def imprimir_camino(historial, nombre_algoritmo):
    print(f"\n[{nombre_algoritmo}] Recorrido:")
    for i, nodo in enumerate(historial):
        print(f"Paso {i}: {nodo}")

# ====================== COSTO UNIFORME ================================

def costo_uniforme(inicio, objetivo):
    cola = [(0, inicio)]  # (costo acumulado, nodo)
    visitados = set()
    historial = []

    while cola:
        costo, actual = heapq.heappop(cola)

        if actual in visitados:
            continue

        visitados.add(actual)
        historial.append(actual)

        if actual == objetivo:
            imprimir_camino(historial, "Costo Uniforme")
            print("Costo total:", costo)
            print("Encontrado:", actual)
            return

        for vecino, peso in GRAFO_COSTO[actual]:
            if vecino not in visitados:
                heapq.heappush(cola, (costo + peso, vecino))

    imprimir_camino(historial, "Costo Uniforme")
    print("No se encontró el objetivo")

# ====================== EJECUCIÓN ======================================

costo_uniforme('A', 'F')