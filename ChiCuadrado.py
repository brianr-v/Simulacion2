import numpy as np
from scipy.stats import chi2_contingency

def chi_squared_test(data):
    # Convertir la lista a una matriz NumPy
    data_observado = np.array(data)

    # Aplicar la prueba de chi-cuadrado
    chi2, p_value, _, _ = chi2_contingency(data_observado)
    
    # Imprimir resultados
    print(f"Estadístico de chi-cuadrado: {chi2}")
    print(f"Valor p: {p_value}")
    
    # Comprobar la significancia 
    alpha = 0.05
    if p_value < alpha:
        print("Los datos no parecen ser aleatorios (se rechaza la hipótesis nula).")
    else:
        print("Los datos parecen ser aleatorios (no se puede rechazar la hipótesis nula).")

  

# Datos de ejemplo 3 de la lista 1
datos3 = [
    [0.38, 0.33, 0.25, 0.05, 0.69, 0.35, 0.98, 0.52, 0.12, 0.79],
    [0.50, 0.46, 0.95, 0.42, 0.49, 0.11, 0.78, 0.34, 0.02, 0.43],
    [0.07, 0.5, 0.05, 0.91, 0.77, 0.18, 0.21, 0.04, 0.17, 0.62],
    [0.91, 0.36, 0.48, 0.88, 0.52, 0.76, 0.99, 0.73, 0.82, 0.9]
]

# Datos de ejemplo 4 de la lista 1
datos4 = [
    [0.8797, 0.3884, 0.6289, 0.8750, 0.5999, 0.8589, 0.9996, 0.2415, 0.3808, 0.9606],
    [0.9848, 0.3469, 0.7977, 0.5844, 0.8147, 0.6431, 0.7387, 0.5613, 0.0318, 0.7401],
    [0.4557, 0.1592, 0.8536, 0.8846, 0.3410, 0.1492, 0.8681, 0.5291, 0.3188, 0.5992],
    [0.8376, 0.6235, 0.3681, 0.2088, 0.1525, 0.2006, 0.4720, 0.4272, 0.6360, 0.0954]
]

# Aplicar la prueba de chi-cuadrado
#Ejercicio 3
print("Ejercicio 3 de la lista 1")
chi_squared_test(datos3)
#Ejercicio 4
print("Ejercicio 4 de la lista 1")
chi_squared_test(datos4)



