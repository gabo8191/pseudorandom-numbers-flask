import random


def uniform_distribution(num_samples, max_value, min_value):
    # Inicializa arrays
    ri_array = []
    ni_array = []
    # Itera sobre el número de muestras (Valor de las iteraciones)
    for i in range(num_samples):
        # Genera un número aleatorio entre 0 y 1 por medio de la función random.uniform que genera un número flotante
        x = random.uniform(0, 1)
        # Se agrega el valor de x a ri_array
        ri_array.append(x)
        # Se agrega el valor de min_value más x multiplicado por la diferencia entre max_value y min_value a ni_array
        ni_array.append(min_value + (max_value - min_value) * x)
        # Retorna los arrays
    return ri_array, ni_array
