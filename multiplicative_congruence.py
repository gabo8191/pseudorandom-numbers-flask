def calculate_method(x0, t, g, iteraciones, min_value, max_value):
    table = []
    xi = x0
    ri_output = []
    ni_output = []

    for i in range(iteraciones):
        xi = calculate_xi(xi, t, g)
        ri = calculate_ri(xi, g)
        ni = calculate_ni(min_value, max_value, ri)
        ri_output.append(ri)
        ni_output.append(ni)
        table.append([i + 1, xi, ri, ni])

    return table


def calculate_xi(xi, t, g):
    return (t * xi) % g


def calculate_ri(xi, g):
    return xi / (g - 1)


def calculate_ni(min_value, max_value, ri):
    return min_value + (max_value - min_value) * ri
