import random
import math


def normal_distribution(std_dev, num_samples, mean):
    ri_array = []
    ni_array = []
    for i in range(num_samples):
        u = random.uniform(0, 1)
        v = random.uniform(0, 1)
        x = math.sqrt(-2.0 * math.log(u)) * math.cos(2.0 * math.pi * v)
        ri_array.append(x * std_dev)
        ni_array.append(mean + x * std_dev)
    return ri_array, ni_array
