'''
Filtrado, Predicción, Suavizado y Explicación
Modelo temporal simple
'''

# ====================== ESTADOS ======================================

estados = ['soleado', 'lluvia']

# ====================== PROBABILIDADES INICIALES =====================

belief = {
    'soleado': 0.7,
    'lluvia': 0.3
}

# ====================== TRANSICIONES ================================

transicion = {

    'soleado': {
        'soleado': 0.8,
        'lluvia': 0.2
    },

    'lluvia': {
        'soleado': 0.4,
        'lluvia': 0.6
    }
}

# ====================== OBSERVACIONES ================================

# P(paraguas | estado)

emision = {

    'soleado': {
        'paraguas': 0.1
    },

    'lluvia': {
        'paraguas': 0.9
    }
}

# ====================== FILTRADO =====================================

def filtrado(observacion):

    nuevo = {}

    for estado in estados:

        suma = 0

        for previo in estados:
            suma += (
                belief[previo] *
                transicion[previo][estado]
            )

        nuevo[estado] = (
            suma *
            emision[estado][observacion]
        )

    # Normalizar
    total = sum(nuevo.values())

    for estado in nuevo:
        nuevo[estado] /= total

    return nuevo

# ====================== PREDICCIÓN ===================================

def prediccion():

    futuro = {}

    for estado in estados:

        suma = 0

        for previo in estados:
            suma += (
                belief[previo] *
                transicion[previo][estado]
            )

        futuro[estado] = suma

    return futuro

# ====================== SUAVIZADO ====================================

def suavizado(actual, evidencia_futura):

    suavizado = {}

    for estado in estados:

        suavizado[estado] = (
            actual[estado] *
            evidencia_futura[estado]
        )

    # Normalizar
    total = sum(suavizado.values())

    for estado in suavizado:
        suavizado[estado] /= total

    return suavizado

# ====================== EXPLICACIÓN ==================================

def explicacion():

    if belief['lluvia'] > belief['soleado']:
        return "La secuencia más probable es lluvia"
    else:
        return "La secuencia más probable es soleado"

# ====================== EJECUCIÓN ====================================

print("\nBELIEF INICIAL:")
print(belief)

# Filtrado
belief_filtrado = filtrado('paraguas')

print("\nFILTRADO:")
print(belief_filtrado)

# Predicción
belief_prediccion = prediccion()

print("\nPREDICCIÓN:")
print(belief_prediccion)

# Suavizado
belief_suavizado = suavizado(
    belief_filtrado,
    belief_prediccion
)

print("\nSUAVIZADO:")
print(belief_suavizado)

# Explicación
print("\nEXPLICACIÓN:")
print(explicacion())