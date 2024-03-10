import numpy as np
import matplotlib.pyplot as plt
import mpld3


def calculate_interval(iterations, data):
    result = 1 + 3.322 * np.log10(iterations)
    intervals = int(min(result, 100)) if np.isfinite(result) else 100
    min_val = min(data)
    max_val = max(data)
    diff = (max_val - min_val) / intervals if intervals > 0 else 1
    data.sort()

    freq_table = [min_val + i * diff for i in range(intervals)]

    freq = [0] * intervals

    data_index = 0
    for i in range(intervals):
        while data_index < len(data) and data[data_index] <= freq_table[i]:
            freq[i] += 1
            data_index += 1

    return freq_table, freq


def generate_plot(freq_table, freq):
    fig, ax = plt.subplots()

    centers = np.arange(len(freq_table)) + 0.5

    ax.bar(centers, freq, width=1, color="purple")

    ax.set_xlabel("Intervalos")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Frecuencia de valores de ni")
    fig.set_size_inches(12, 6)

    mpld3.show()
