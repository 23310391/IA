'''
Q-Learning completo (gridworld)
'''

import random

# ====================== ENTORNO =======================================

filas, columnas = 3, 3

# Estados
estados = [(i, j) for i in range(filas) for j in range(columnas)]

inicio = (0, 0)
objetivo = (2, 2)
obstaculo = (1, 1)

acciones = ['arriba', 'abajo', 'izquierda', 'derecha']

# ====================== PARÁMETROS ====================================

alpha = 0.1
gamma = 0.9
epsilon = 0.2
episodios = 200

# ====================== Q TABLE =======================================

Q = {}
for s in estados:
    Q[s] = {a: 0 for a in acciones}

# ====================== FUNCIONES =====================================

def mover(estado, accion):
    i, j = estado

    if accion == 'arriba':
        i -= 1
    elif accion == 'abajo':
        i += 1
    elif accion == 'izquierda':
        j -= 1
    elif accion == 'derecha':
        j += 1

    # límites del grid
    i = max(0, min(i, filas - 1))
    j = max(0, min(j, columnas - 1))

    nuevo_estado = (i, j)

    # evitar obstáculo
    if nuevo_estado == obstaculo:
        return estado

    return nuevo_estado

def recompensa(estado):
    if estado == objetivo:
        return 100
    elif estado == obstaculo:
        return -100
    else:
        return -1

def elegir_accion(estado):
    if random.random() < epsilon:
        return random.choice(acciones)
    return max(Q[estado], key=Q[estado].get)

# ====================== Q-LEARNING ====================================

for ep in range(episodios):
    estado = inicio

    while estado != objetivo:
        accion = elegir_accion(estado)
        siguiente = mover(estado, accion)

        r = recompensa(siguiente)

        # actualización Q-learning
        mejor_siguiente = max(Q[siguiente].values())
        Q[estado][accion] += alpha * (
            r + gamma * mejor_siguiente - Q[estado][accion]
        )

        estado = siguiente

# ====================== POLÍTICA FINAL ================================

print("\nPolítica aprendida:\n")

for i in range(filas):
    fila = ""
    for j in range(columnas):
        estado = (i, j)

        if estado == objetivo:
            fila += " G "
        elif estado == obstaculo:
            fila += " X "
        else:
            mejor = max(Q[estado], key=Q[estado].get)
            if mejor == 'arriba':
                fila += " ↑ "
            elif mejor == 'abajo':
                fila += " ↓ "
            elif mejor == 'izquierda':
                fila += " ← "
            elif mejor == 'derecha':
                fila += " → "
    print(fila)