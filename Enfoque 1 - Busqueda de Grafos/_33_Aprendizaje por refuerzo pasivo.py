'''
Aprendizaje por Refuerzo Pasivo
TD(0) - Evaluación de política
'''

import random

# ====================== ESTADOS =======================================

estados = ['A', 'B', 'C']
objetivo = 'C'

# ====================== POLÍTICA FIJA ================================

politica = {
    'A': 'avanzar',
    'B': 'avanzar',
    'C': 'quedarse'
}

# ====================== TRANSICIONES ================================

transiciones = {
    'A': {'avanzar': [('B', 1.0)], 'quedarse': [('A', 1.0)]},
    'B': {'avanzar': [('C', 1.0)], 'quedarse': [('B', 1.0)]},
    'C': {'avanzar': [('C', 1.0)], 'quedarse': [('C', 1.0)]}
}

# ====================== RECOMPENSAS ==================================

def recompensa(s):
    return 100 if s == objetivo else -1

# ====================== PARÁMETROS ====================================

alpha = 0.1   # tasa de aprendizaje
gamma = 0.9   # descuento

# Inicializar valores
V = {s: 0 for s in estados}

# ====================== SIMULACIÓN ====================================

def siguiente_estado(s, a):
    posibles = transiciones[s][a]
    estados_s = [x for x, _ in posibles]
    probs = [p for _, p in posibles]
    return random.choices(estados_s, weights=probs)[0]

# ====================== TD(0) =========================================

def td_aprendizaje(episodios=20):
    global V

    for ep in range(episodios):
        estado = 'A'

        print(f"\nEpisodio {ep+1}")

        while estado != objetivo:
            accion = politica[estado]
            siguiente = siguiente_estado(estado, accion)

            r = recompensa(siguiente)

            # 🔹 actualización TD(0)
            V[estado] += alpha * (r + gamma * V[siguiente] - V[estado])

            print(f"{estado} → {siguiente} | V({estado}) = {V[estado]:.2f}")

            estado = siguiente

    print("\nValores finales:")
    for s in V:
        print(f"V({s}) = {V[s]:.2f}")

# ====================== EJECUCIÓN =====================================

td_aprendizaje()