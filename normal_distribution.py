import random
import math


def normal_distribution(std_dev, num_samples, mean):
    # Inicializa arrays
    ri_array = []
    ni_array = []
    # Itera sobre el número de muestras (Valor de las iteraciones)
    for i in range(num_samples):
        # Genera un número aleatorio entre 0 y 1 por medio de la función random.uniform que genera un número flotante
        u = random.uniform(0, 1)
        # Genera un número aleatorio entre 0 y 1 por medio de la función random.uniform que genera un número flotante
        v = random.uniform(0, 1)
        # Esta formula corresponde a la transformación de Box-Muller Permite obtener números aleatorios con
        # distribución normal a partir de dos números aleatorios con distribución uniforme
        x = math.sqrt(-2.0 * math.log(u)) * math.cos(2.0 * math.pi * v)
        # Se agrega el valor de x multiplicado por la desviación estándar a ri_array
        #Se realiza así para que ri sea un número con distribución normal
        ri_array.append(x * std_dev)
        # Se agrega el valor de la media más x multiplicado por la desviación estándar a ni_array
        #se suma la media porque la media es el valor esperado de la distribución normal
        ni_array.append(mean + x * std_dev)
    return ri_array, ni_array
