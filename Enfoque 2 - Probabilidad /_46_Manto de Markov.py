'''
Manto de Markov
'''

# ====================== RED BAYESIANA ================================

red = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': [],
    'D': []
}

# Padres manuales
padres = {
    'A': [],
    'B': ['A'],
    'C': ['B'],
    'D': ['B']
}

# ====================== MANTO DE MARKOV ==============================

def manto_markov(nodo):
    hijos = red[nodo]

    # padres del nodo
    blanket = set(padres[nodo])

    # agregar hijos
    blanket.update(hijos)

    # agregar padres de los hijos
    for hijo in hijos:
        blanket.update(padres[hijo])

    # quitar el propio nodo
    blanket.discard(nodo)

    return blanket

# ====================== EJECUCIÓN ====================================

nodo = 'B'

print("\nManto de Markov de", nodo)
print(manto_markov(nodo))