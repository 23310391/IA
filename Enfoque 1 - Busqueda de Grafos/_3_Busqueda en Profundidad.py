'''
Busqueda en profundidad
Usa una lista LIFO

'''
GRAFO = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# ====================== RECORRIDO ======================================

def imprimir_camino(historial, nombre_algoritmo):
    print(f"\n[{nombre_algoritmo}] Recorrido:")
    for i, nodo in enumerate(historial):
        print(f"Paso {i}: {nodo}")

# ====================== BÚSQUEDA EN PROFUNDIDAD =========================

def busqueda_profundidad(inicio, objetivo):
    pila = [inicio]          # Pila (LIFO)
    visitados = set()
    historial = []

    while pila:
        actual = pila.pop()  # Saca el último elemento
       
        if actual not in visitados:
            visitados.add(actual)
            historial.append(actual)

            if actual == objetivo:
                imprimir_camino(historial, "DFS")
                print("Encontrado:", actual)
                return

            # Agregar vecinos a la pila
            for vecino in GRAFO[actual]:
                if vecino not in visitados:
                    pila.append(vecino)

    imprimir_camino(historial, "DFS")
    print("No se encontró el objetivo")

# ====================== EJECUCIÓN ======================================

busqueda_profundidad('A', 'F')