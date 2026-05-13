'''
Deep Learning simple
Red neuronal básica


'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# ====================== DATOS ========================================

# [horas_estudio, tareas]
X = np.array([
    [1, 1],
    [2, 1],
    [2, 2],
    [3, 2],
    [4, 3],
    [5, 4]
])

# Resultado:
# 0 = reprueba
# 1 = aprueba
y = np.array([0, 0, 0, 1, 1, 1])

# ====================== MODELO =======================================

modelo = Sequential()

# Capa oculta
modelo.add(Dense( # 4 neuronas, pesos inicializados aleatoriamente
                  # ReLU descarta valores negativos, resalta patrones importantes
    input_dim=2, # 2 entradas: horas_estudio y tareas
    units=4,
    activation='relu'
))

# Capa de salida
modelo.add(Dense( 
    1,
    activation='sigmoid' # convierte la salida a probabilidad entre 0 y 1
))

# ====================== COMPILAR =====================================

modelo.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# ====================== ENTRENAMIENTO ================================

modelo.fit(
    X,
    y,
    epochs=200, # 200 iteraciones: en cada una se ajustan los pesos para reducir el error
    verbose=0
)

# ====================== PREDICCIÓN ===================================

nuevo = np.array([[4, 2]]) #con 4 horas de estudio y 2 tareas, que tan probable es que apruebe

prediccion = modelo.predict(nuevo)

print("\nDeep Learning:\n")

print("Probabilidad de aprobar:")
print(round(prediccion[0][0], 3))