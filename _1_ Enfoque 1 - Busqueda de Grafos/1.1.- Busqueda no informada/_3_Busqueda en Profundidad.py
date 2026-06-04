'''
Busqueda en profundidad
Usa una lista LIFO

Busca por ramas, primero A, luego B, luego D, si D no es el objetivo, regresa a B y va a E, si E no es el objetivo, 
regresa a B y luego a A, y va a C, luego a F.

no garantiza el camino mas corto, pero si encuentra el objetivo, lo hace de forma rapida, sin revisar todos los nodos

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
    pila = [inicio]          # Pila (LIFO), el último elemento en entrar es el primero en salir
    visitados = set()       # evita visitar nodos repetidos
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