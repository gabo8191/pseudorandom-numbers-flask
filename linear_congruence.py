def calculate_table(x0, a, c, m, iteraciones, min_value, max_value):
    table = []
    xi = x0
    Ni_array = []

    for i in range(iteraciones):
        xi = calculate_xi(xi, a, c, m)
        ri = calculate_ri(xi, m)
        ni = calculate_ni(min_value, max_value, ri)
        Ni_array.append(ni)
        table.append([i + 1, xi, ri, ni])

    return table


def calculate_ni(min_value, max_value, ri):
    return min_value + (max_value - min_value) * ri


def calculate_ri(xi, m):
    return xi / (m - 1)


def calculate_xi(xi, a, c, m):
    return (a * xi + c) % m
