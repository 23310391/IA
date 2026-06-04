'''Dijkstra
Algoritmo de búsqueda del camino más corto en un grafo ponderado.
Explora nodos por orden de distancia acumulada desde el origen.
'''

import heapq

iteraciones = 0

def dijkstra(grafo, inicio, fin):
    global iteraciones

    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}
    visitados = set()
    heap = [(0, inicio)]  # (distancia, nodo)
    historial = []        # para la visualizacion

    while heap:
        dist_actual, nodo_actual = heapq.heappop(heap)
        iteraciones += 1

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)
        historial.append({
            'nodo': nodo_actual,
            'distancia': dist_actual,
            'visitados': set(visitados),
            'distancias': dict(distancias)
        })

        if nodo_actual == fin:
            break

        for vecino, peso in grafo[nodo_actual].items():
            if vecino not in visitados:
                nueva_dist = dist_actual + peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    predecesores[vecino] = nodo_actual
                    heapq.heappush(heap, (nueva_dist, vecino))

    # reconstruimos el camino
    camino = []
    nodo = fin
    while nodo is not None:
        camino.append(nodo)
        nodo = predecesores[nodo]
    camino.reverse()

    return distancias, camino, historial


def visualizar(grafo, historial, camino, inicio, fin):
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        import networkx as nx
    except ImportError:
        print("Instala las librerias: pip install matplotlib networkx")
        return

    G = nx.DiGraph()
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G, seed=42)

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    fig.suptitle("Visualización paso a paso - Dijkstra", fontsize=16, fontweight='bold')
    axes = axes.flatten()

    pasos = min(len(historial), 5)

    for idx in range(pasos):
        ax = axes[idx]
        paso = historial[idx]
        visitados = paso['visitados']
        distancias_paso = paso['distancias']
        nodo_actual = paso['nodo']

        # colores de nodos
        colores = []
        for nodo in G.nodes():
            if nodo == nodo_actual:
                colores.append('#FF6B6B')       # rojo = nodo actual
            elif nodo in visitados:
                colores.append('#4ECDC4')       # verde = visitado
            else:
                colores.append('#95A5A6')       # gris = sin visitar

        # colores de aristas
        edge_colors = []
        for u, v in G.edges():
            if u in visitados and v in visitados:
                edge_colors.append('#4ECDC4')
            else:
                edge_colors.append('#BDC3C7')

        nx.draw(G, pos, ax=ax, with_labels=True, node_color=colores,
                edge_color=edge_colors, node_size=800, font_size=10,
                font_weight='bold', arrows=True, arrowsize=20)

        # etiquetas de pesos
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_size=8)

        # distancias acumuladas debajo de cada nodo
        dist_labels = {n: f"{d if d != float('inf') else '∞'}" for n, d in distancias_paso.items()}
        pos_lower = {n: (x, y - 0.15) for n, (x, y) in pos.items()}
        nx.draw_networkx_labels(G, pos_lower, labels=dist_labels, ax=ax,
                                font_size=7, font_color='#2C3E50')

        ax.set_title(f"Paso {idx + 1}: visitando '{nodo_actual}' (dist: {paso['distancia']})",
                     fontsize=10)

    # ultimo panel: camino final
    ax_final = axes[5]
    colores_final = []
    for nodo in G.nodes():
        if nodo == inicio:
            colores_final.append('#F39C12')     # naranja = inicio
        elif nodo == fin:
            colores_final.append('#8E44AD')     # morado = fin
        elif nodo in camino:
            colores_final.append('#2ECC71')     # verde = en el camino
        else:
            colores_final.append('#95A5A6')     # gris = no usado

    edge_colors_final = []
    for u, v in G.edges():
        if u in camino and v in camino and camino.index(v) == camino.index(u) + 1:
            edge_colors_final.append('#E74C3C')  # rojo = arista del camino
        else:
            edge_colors_final.append('#BDC3C7')

    nx.draw(G, pos, ax=ax_final, with_labels=True, node_color=colores_final,
            edge_color=edge_colors_final, node_size=800, font_size=10,
            font_weight='bold', arrows=True, arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax_final, font_size=8)

    ax_final.set_title(f"Camino más corto: {' → '.join(camino)}", fontsize=10)

    # leyenda
    leyenda = [
        mpatches.Patch(color='#FF6B6B', label='Nodo actual'),
        mpatches.Patch(color='#4ECDC4', label='Visitado'),
        mpatches.Patch(color='#95A5A6', label='Sin visitar'),
        mpatches.Patch(color='#F39C12', label='Inicio'),
        mpatches.Patch(color='#8E44AD', label='Fin'),
        mpatches.Patch(color='#2ECC71', label='Camino final'),
    ]
    fig.legend(handles=leyenda, loc='lower center', ncol=6, fontsize=9)
    plt.tight_layout()
    plt.savefig("dijkstra.png", dpi=150, bbox_inches='tight')
    print("\nVisualizacion guardada como 'dijkstra.png'")
    plt.show()


# grafo de ejemplo (puedes modificarlo)
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'B': 1, 'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {}
}

inicio = input("Nodo de inicio: ").upper()
fin = input("Nodo de fin: ").upper()

print(f"\nBuscando camino de '{inicio}' a '{fin}'...\n")

distancias, camino, historial = dijkstra(grafo, inicio, fin)

# resultados en consola
print("Distancias mínimas desde", inicio)
for nodo, dist in distancias.items():
    print(f"  {inicio} → {nodo}: {dist if dist != float('inf') else '∞'}")

print(f"\nCamino más corto: {' → '.join(camino)}")
print(f"Distancia total:  {distancias[fin]}")
print(f"Iteraciones:      {iteraciones}")

visualizar(grafo, historial, camino, inicio, fin)