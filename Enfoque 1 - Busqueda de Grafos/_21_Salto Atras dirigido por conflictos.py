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

# 21. BACKJUMPING
# ============================================================

def backjumping(asignacion=None):
    if asignacion is None:
        asignacion = {}

    if len(asignacion) == len(variables):
        print("\n[Backjumping] Solución:", asignacion)
        return asignacion

    var = variables[len(asignacion)]

    for color in colores:
        print(f"Intentando {var} = {color}")
        if es_valido(var, color, asignacion):
            asignacion[var] = color
            resultado = backjumping(asignacion)
            if resultado:
                return resultado
            print(f"Salto atrás en {var}")
            del asignacion[var]

    return None

backjumping()

