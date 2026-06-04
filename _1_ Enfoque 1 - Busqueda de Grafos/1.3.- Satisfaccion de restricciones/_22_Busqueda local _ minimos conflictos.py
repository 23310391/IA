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

# 22. MÍNIMOS CONFLICTOS
# ============================================================
import random
import math

def min_conflicts(max_iter=50):
    asignacion = {v: random.choice(colores) for v in variables}
    print("\nEstado inicial:", asignacion)

    for i in range(max_iter):
        conflictos = []

        for var in variables:
            for vecino in restricciones[var]:
                if asignacion[var] == asignacion[vecino]:
                    conflictos.append(var)

        if not conflictos:
            print("Solución encontrada:", asignacion)
            return asignacion

        var = random.choice(conflictos)
        print(f"Iteración {i}, conflicto en {var}")

        asignacion[var] = min(colores, key=lambda c: sum(
            1 for vecino in restricciones[var] if asignacion.get(vecino) == c
        ))

        print("Nuevo estado:", asignacion)

    print("Resultado final (no óptimo):", asignacion)
    return asignacion

min_conflicts()

