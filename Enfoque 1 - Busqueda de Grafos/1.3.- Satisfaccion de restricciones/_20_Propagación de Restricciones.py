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

# 20. AC-3
# ============================================================

def ac3():
    dominios = {v: list(colores) for v in variables}

    print("\n[AC-3] Inicio:", dominios)

    cambio = True
    while cambio:
        cambio = False
        for var in variables:
            for vecino in restricciones[var]:
                for color in dominios[var][:]:
                    if all(color == c for c in dominios[vecino]):
                        dominios[var].remove(color)
                        cambio = True
                        print(f"Eliminando {color} de {var}")

    print("Dominios reducidos:", dominios)

ac3()

