import numpy as np
import matplotlib.pyplot as plt
import mpld3


def calculaFreq(ni_values, intervals):
    freq, _ = np.histogram(ni_values, bins=intervals)
    return freq.tolist()


def calculateInterval(iterations, ni_values):
    k = min(1 + 3.322 * np.log10(iterations), 100)
    intervals = np.histogram_bin_edges(ni_values, bins=min(int(k), 100))
    return intervals


def generatePlot(intervals, freq):
    fig, ax = plt.subplots()
    ax.bar(intervals[:-1], freq, width=np.diff(intervals), color="purple")
    ax.set_xlabel("Intervalos")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Frecuencia de valores de ni")
    fig.set_size_inches(12, 6)

    mpld3.show()
