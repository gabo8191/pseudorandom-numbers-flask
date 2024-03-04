import random


def uniform_distribution(num_samples, max_value, min_value):
    ri_array = []
    ni_array = []
    for i in range(num_samples):
        x = random.uniform(0, 1)
        ri_array.append(x)
        ni_array.append(min_value + (max_value - min_value) * x)
    return ri_array, ni_array
