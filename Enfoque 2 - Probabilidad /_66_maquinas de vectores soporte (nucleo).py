'''
Máquina de Vectores de Soporte (SVM)
Clasificación básica
'''

from sklearn import svm

# ====================== DATOS =========================================

# X = características
X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 5],
    [7, 7],
    [8, 6]
]

# y = etiquetas
y = ['A', 'A', 'A', 'B', 'B', 'B']

# ====================== MODELO ========================================

modelo = svm.SVC(kernel='linear')  # kernel lineal

# ====================== ENTRENAMIENTO =================================

modelo.fit(X, y)

# ====================== PREDICCIÓN ====================================

nuevo_punto = [[4, 4]]
prediccion = modelo.predict(nuevo_punto)

print("Predicción:", prediccion)