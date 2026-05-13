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
# FORWARD CHECKING
# ============================================================

def forward_checking(asignacion=None, dominios=None):
    if asignacion is None:
        asignacion = {}

    if dominios is None:
        dominios = {v: list(colores) for v in variables}

     # Caso base
    if len(asignacion) == len(variables):
        print("\n[Forward Checking] Solución:", asignacion)
        return asignacion

    var = variables[len(asignacion)]

    for color in dominios[var]:
        print(f"Probando {var} = {color}")

        # Copia de dominios
        nuevo_dom = {v: list(dominios[v]) for v in dominios}

        asignacion[var] = color

        fallo = False

        # Eliminación hacia adelante
        for vecino in restricciones[var]:
            if color in nuevo_dom[vecino]:
                nuevo_dom[vecino].remove(color)

                # ⚠️ Validación clave
                if len(nuevo_dom[vecino]) == 0:
                    fallo = True

        if not fallo:
            resultado = forward_checking(asignacion, nuevo_dom)
            if resultado:
                return resultado

        # Backtrack
        del asignacion[var]

    return None

# Ejecutar
forward_checking()

