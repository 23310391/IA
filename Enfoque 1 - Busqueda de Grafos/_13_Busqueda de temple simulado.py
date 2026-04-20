'''
temple simulado
explora mas que la busqueda tabu
no garantiza el mejor camino, es aleatorio

utilizamos un parametro temperatura, en cada vuelta reducimos la temperatura gradualmente
mientras mas alta la temperatura, acepta mas errores

al inicio tenemos una temperatura mayor, explora mas caminos
mientras mas cerca está de converger, acepta menos errores, menos probabilidad hay de tomar un camino erroneo

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


# ====================== RECORRIDO ======================================

def imprimir_camino(historial, nombre_algoritmo):
    print(f"\n[{nombre_algoritmo}] Recorrido:")
    for i, nodo in enumerate(historial):
        print(f"Paso {i}: {nodo}")

 
# ============================TEMPLE SIMULADO================================

import random
import math

def temple_simulado(inicio, objetivo, temp=10):
    actual = inicio
    historial = [actual]

    while temp > 0.1:
        if actual == objetivo:
            imprimir_camino(historial, "Temple Simulado")
            print("Encontrado:", actual)
            return

        vecino = random.choice(GRAFO[actual]) if GRAFO[actual] else actual
        delta = HEURISTICA[vecino] - HEURISTICA[actual]

        if delta < 0 or random.random() < math.exp(-delta / temp):
            actual = vecino
            historial.append(actual)

        temp *= 0.9

    imprimir_camino(historial, "Temple Simulado")
    print("Resultado final:", actual)
    
temple_simulado('A', 'F')
