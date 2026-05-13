'''
Búsqueda de la política (Policy Search) - CORREGIDO
'''

import random

# ====================== ENTORNO =======================================

estados = ['A', 'B', 'C']
acciones = ['avanzar', 'quedarse']
objetivo = 'C'

# ====================== TRANSICIONES ================================

transiciones = {
    'A': {'avanzar': [('B', 1.0)], 'quedarse': [('A', 1.0)]},
    'B': {'avanzar': [('C', 1.0)], 'quedarse': [('B', 1.0)]},
    'C': {'avanzar': [('C', 1.0)], 'quedarse': [('C', 1.0)]}
}

# ====================== RECOMPENSA ====================================

def recompensa(s):
    return 100 if s == objetivo else -1

# ====================== SIMULACIÓN ====================================

def simular(politica, episodios=10, max_pasos=10):
    total = 0

    for _ in range(episodios):
        estado = 'A'

        for _ in range(max_pasos):  # 🔥 evita loops infinitos
            accion = politica[estado]
            siguiente = transiciones[estado][accion][0][0]

            total += recompensa(siguiente)
            estado = siguiente

            if estado == objetivo:
                break

    return total / episodios

# ====================== GENERAR POLÍTICA ALEATORIA =====================

def politica_aleatoria():
    return {s: random.choice(acciones) for s in estados}

# ====================== BÚSQUEDA ======================================

def busqueda_politica(iteraciones=20):
    mejor_politica = None
    mejor_valor = float('-inf')

    for i in range(iteraciones):
        politica = politica_aleatoria()
        valor = simular(politica)

        print(f"Iteración {i+1}: {politica} → {valor:.2f}")

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_politica = politica.copy()  # 🔥 evitar referencia

    print("\nMejor política encontrada:")
    for s in mejor_politica:
        print(f"{s} → {mejor_politica[s]}")

    print("Valor:", round(mejor_valor, 2))

# ====================== EJECUCIÓN =====================================

busqueda_politica()