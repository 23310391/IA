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

# UTILIDAD
# ============================================================

def imprimir_camino(historial, nombre):
    print(f"\n[{nombre}] Recorrido:")
    for i, n in enumerate(historial):
        print(f"Paso {i}: {n}")

# ============================================================
# 15. ALGORITMO GENÉTICO (CORREGIDO)
# ============================================================

import random
import math

TODOS_NODOS = list(GRAFO.keys())

def fitness(nodo):
    return -HEURISTICA[nodo]

def seleccionar_padre(poblacion):
    return random.choice(poblacion)


def generar_hijo(padre):
    vecinos = GRAFO[padre]
    # 🔧 SOLUCIÓN AL ERROR: evitar lista vacía
    if vecinos:
        return random.choice(vecinos)
    else:
        # fallback: elegir cualquier nodo del grafo
        return random.choice(TODOS_NODOS)


def algoritmo_genetico():
    poblacion = ['A', 'B', 'C']

    for gen in range(5):
        poblacion = sorted(poblacion, key=fitness, reverse=True)
        print(f"Generación {gen}: {poblacion}")

        nueva_poblacion = poblacion[:2]  # elitismo

        while len(nueva_poblacion) < len(poblacion):
            padre = seleccionar_padre(poblacion)
            hijo = generar_hijo(padre)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    mejor = max(poblacion, key=fitness)
    print("Mejor solución:", mejor)

algoritmo_genetico()

