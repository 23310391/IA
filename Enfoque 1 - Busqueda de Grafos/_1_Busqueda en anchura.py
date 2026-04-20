'''
Algoritmo busqueda en anchura
recorre el grafo por niveles, encuentra el objetivo, sin dar el camino mas optimo de forma explicita
utiliza una cola FIFO
'''

from collections import deque #double ended queue, permite agregar elementos al inicio y al final de la cola

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

# ====================== BÚSQUEDA EN ANCHURA ============================

def busqueda_anchura(inicio, objetivo):
    cola = deque([inicio])   # Cola FIFO
    visitados = set([inicio])
    historial = []

    while cola:
        actual = cola.popleft() #eliminamos el primer elemento que entró a la lista (fifo)
        historial.append(actual)

        if actual == objetivo:
            imprimir_camino(historial, "BFS")
            print("Encontrado:", actual)
            return

        for vecino in GRAFO[actual]:
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)

    imprimir_camino(historial, "BFS")
    print("No se encontró el objetivo")

# ====================== EJECUCIÓN ======================================

busqueda_anchura('A', 'F')