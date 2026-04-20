'''
Busqueda Tabu
visitamos al mejor vecino (segun heuristica)
evitamos regresar a los nodos ya visitados (lista tabu)
no exploramos todos los caminos
'''

GRAFO = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heurística (estimacion de que tan cerca está cada nodo del objetivo F)
HEURISTICA = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

# ==================== RECORRIDO ========================================
def imprimir_camino(historial, nombre_algoritmo):
    print(f"\n[{nombre_algoritmo}] Recorrido:")
    for i, nodo in enumerate(historial):
        print(f"Paso {i}: {nodo}")
        
# =============== Busqueda tabu =============================================
def busqueda_tabu(inicio, objetivo, max_iter=10):
    actual = inicio         #nodo donde estoy
    tabu = []               #lista tabu, nodos prohibidos, ya visitados
    historial = [actual]    #camino recorrido

    for _ in range(max_iter):
        if actual == objetivo:
            imprimir_camino(historial, "Tabú")
            print("Encontrado:", actual)
            return

        vecinos = GRAFO[actual]
        candidatos = [n for n in vecinos if n not in tabu] 
        '''
        linea 48: verificamos que los vecinos del nodo actual no estén en la lista tabu, y decidimos a cual visitar
        '''

        if not candidatos:
            break

        siguiente = min(candidatos, key=lambda x: HEURISTICA[x])
        tabu.append(actual)
        actual = siguiente
        historial.append(actual)

    imprimir_camino(historial, "Tabú")
    print("Resultado final:", actual)

busqueda_tabu('A', 'F', 4) #iniciamos en A, el objetivo es F, el numero máximo de iteraciones es 4, llegamos al objetivo
