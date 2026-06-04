'''
Iteración de políticas (Policy Iteration)
MDP simple
'''

# ====================== ESTADOS =======================================

estados = ['A', 'B', 'C']
objetivo = 'C'

gamma = 0.9

# ====================== TRANSICIONES ================================

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
    return -1

# ====================== EVALUACIÓN DE POLÍTICA ========================

def evaluar_politica(politica, iteraciones=10):
    V = {s: 0 for s in estados}

    for _ in range(iteraciones):
        nuevo_V = {}

        for s in estados:
            a = politica[s]
            total = 0

            for s_next, prob in transiciones[s][a]:
                r = recompensa(s, a, s_next)
                total += prob * (r + gamma * V[s_next])

            nuevo_V[s] = total

        V = nuevo_V

    return V

# ====================== MEJORA DE POLÍTICA ============================

def mejorar_politica(V, politica):
    estable = True

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

        if mejor_accion != politica[s]:
            politica[s] = mejor_accion
            estable = False

    return politica, estable

# ====================== POLICY ITERATION ==============================

def policy_iteration():
    # Política inicial aleatoria
    politica = {s: 'quedarse' for s in estados}

    while True:
        # 🔹 Evaluar política
        V = evaluar_politica(politica)

        # 🔹 Mejorar política
        politica, estable = mejorar_politica(V, politica)

        print("\nPolítica actual:")
        for s in politica:
            print(f"{s} → {politica[s]}")

        if estable:
            break

    return politica, V

# ====================== EJECUCIÓN =====================================

politica, V = policy_iteration()

print("\nPolítica óptima final:")
for s, a in politica.items():
    print(f"{s} → {a}")