import numpy as np
import matplotlib.pyplot as plt
import mpld3

def calculate_interval(iterations, data):
    # Se calcula el número de intervalos con la fórmula 1 + 3.322 * log10(iterations) que es la regla de Sturges
    result = 1 + 3.322 * np.log10(iterations)
    # Se redondea el valor de result a un entero
    intervals = int(min(result, 100)) if np.isfinite(result) else 100
    # Se calcula el valor mínimo y máximo de los datos
    min_val = min(data)
    max_val = max(data)
    # Se calcula la diferencia entre el valor máximo y mínimo dividido entre el número de intervalos
    #Con el fin de obtener el tamaño de los intervalos
    diff = (max_val - min_val) / intervals if intervals > 0 else 1
    data.sort()

    # Se crea una lista con los valores de los intervalos
    freq_table = [min_val + i * diff for i in range(intervals)]
    # Se crea una lista con los valores de las frecuencias
    freq = [0] * intervals
    data_index = 0
    # Se crea un ciclo para calcular las frecuencias de los valores
    for i in range(intervals):
        # Se calcula la frecuencia de los valores con la fórmula min_val + i * diff
        # con el fin de obtener el número de valores que se encuentran en el intervalo
        while data_index < len(data) and data[data_index] <= freq_table[i]:
            freq[i] += 1
            data_index += 1

    # Se retorna la tabla de frecuencias y las frecuencias o en otras palabras, los valores de los intervalos y las frecuencias
    return freq_table, freq


def generate_plot(freq_table, freq):
    # Se crea un gráfico de barras con los valores de los intervalos y las frecuencias
    fig, ax = plt.subplots()
    # Se crea un array con los valores de los centros de los intervalos
    centers = np.arange(len(freq_table)) + 0.5
    # Se crea un gráfico de barras con los valores de los centros de los intervalos y las frecuencias
    ax.bar(centers, freq, width=1, color="purple")
    # Se establece el título del gráfico
    ax.set_xlabel("Intervalos")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Frecuencia de valores de ni")
    # Se establece el tamaño del gráfico
    fig.set_size_inches(12, 6)
    # Se retorna el gráfico
    mpld3.show()
