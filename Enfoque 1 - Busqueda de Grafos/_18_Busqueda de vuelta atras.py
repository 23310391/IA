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

# ============================================================

def backtracking(asignacion=None):
    if asignacion is None:
        asignacion = {}

    if len(asignacion) == len(variables):
        print("\n[Backtracking] Solución:", asignacion)
        return asignacion

    var = variables[len(asignacion)]

    for color in colores:
        print(f"Intentando {var} = {color}")
        if es_valido(var, color, asignacion):
            asignacion[var] = color
            resultado = backtracking(asignacion)
            if resultado:
                return resultado
            print(f"Backtrack en {var}")
            del asignacion[var]

    return None

backtracking()

