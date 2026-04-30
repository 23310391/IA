'''
Iteración de valores (Value Iteration)
MDP simple (markov decision model)
'''

# ====================== ESTADOS =======================================

estados = ['A', 'B', 'C']

# Estado objetivo
objetivo = 'C'

# ====================== PARÁMETROS ====================================

gamma = 0.9  # factor de descuento

# ====================== TRANSICIONES ================================

# P(s' | s, a)
transiciones = {
    'A': {
        'avanzar': [('B', 1.0)],
        'quedarse': [('A', 1.0)]
    },
    'B': {
        'avanzar': [('C', 1.0)],
        'quedarse': [('B', 1.0)]
    },
    'C': {
        'avanzar': [('C', 1.0)],
        'quedarse': [('C', 1.0)]
    }
}

# ====================== RECOMPENSAS ==================================

def recompensa(s, a, s_next):
    if s_next == objetivo:
        return 100
    return -1  # costo por moverse

# ====================== VALUE ITERATION ===============================

def value_iteration(iteraciones=10):
    V = {s: 0 for s in estados}

    for it in range(iteraciones):
        nuevo_V = {}

        for s in estados:
            valores_acciones = []

            for a in transiciones[s]:
                total = 0

                for s_next, prob in transiciones[s][a]:
                    r = recompensa(s, a, s_next)
                    total += prob * (r + gamma * V[s_next])

                valores_acciones.append(total)

            nuevo_V[s] = max(valores_acciones)

        V = nuevo_V

        print(f"\nIteración {it+1}:")
        for s in V:
            print(f"V({s}) = {V[s]:.2f}")

    return V

# ====================== POLÍTICA ÓPTIMA ===============================

def obtener_politica(V):
    politica = {}

    for s in estados:
        mejor_accion = None
        mejor_valor = float('-inf')

        for a in transiciones[s]:
            total = 0
            for s_next, prob in transiciones[s][a]:
                r = recompensa(s, a, s_next)
                total += prob * (r + gamma * V[s_next])

            if total > mejor_valor:
                mejor_valor = total
                mejor_accion = a

        politica[s] = mejor_accion

    return politica

# ====================== EJECUCIÓN =====================================

V = value_iteration()
politica = obtener_politica(V)

print("\nPolítica óptima:")
for s, a in politica.items():
    print(f"{s} → {a}")