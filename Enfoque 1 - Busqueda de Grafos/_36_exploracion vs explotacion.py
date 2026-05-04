'''
Exploración vs Explotación (epsilon-greedy)
Ejemplo simple con recompensas simuladas
'''

import random

# ====================== ACCIONES ======================================

acciones = ['A', 'B', 'C']

# Recompensas reales (desconocidas para el agente)
recompensas_reales = {
    'A': 5,
    'B': 10,
    'C': 2
}

# ====================== PARÁMETROS ====================================

epsilon = 0.3   # probabilidad de explorar
episodios = 50

# Estimaciones del agente
Q = {a: 0 for a in acciones}
conteo = {a: 0 for a in acciones}

# ====================== ELECCIÓN ======================================

def elegir_accion():
    if random.random() < epsilon:
        return random.choice(acciones)  # explorar
    return max(Q, key=Q.get)            # explotar

# ====================== SIMULACIÓN ====================================

for ep in range(episodios):
    accion = elegir_accion()

    # simular recompensa (con ruido)
    recompensa = recompensas_reales[accion] + random.uniform(-1, 1)

    # actualizar promedio incremental
    conteo[accion] += 1
    Q[accion] += (recompensa - Q[accion]) / conteo[accion]

    print(f"Episodio {ep+1}: Acción={accion}, Recompensa={recompensa:.2f}")

# ====================== RESULTADO =====================================

print("\nValores aprendidos:")
for a in Q:
    print(f"{a}: {Q[a]:.2f}")

mejor = max(Q, key=Q.get)
print("\nMejor acción aprendida:", mejor)