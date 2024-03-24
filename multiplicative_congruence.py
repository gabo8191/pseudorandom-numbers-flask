def calculate_method(x0, t, g, iteraciones, min_value, max_value):
    # Se crea una lista vacía para almacenar los valores de la tabla
    table = []
    xi = x0
    ri_output = []
    ni_output = []

    # Se crea un ciclo para calcular los valores de las columnas
    for i in range(iteraciones):
        xi = calculate_xi(xi, t, g)
        ri = calculate_ri(xi, g)
        ni = calculate_ni(min_value, max_value, ri)
        # Se agrega el valor de ri y ni a las listas de valores de ri y ni
        ri_output.append(ri)
        ni_output.append(ni)
        # Se agrega una lista con los valores de las columnas a la tabla
        table.append([i + 1, xi, ri, ni])
# Se retorna la tabla con los valores de las columnas
    return table


def calculate_xi(xi, t, g):
    # Se calcula el valor de xi con la fórmula (t * xi) % g
    # Se hace asi para evitar que el valor de xi sea mayor a g
    return (t * xi) % g

def calculate_ri(xi, g):
    # Se calcula el valor de ri con la fórmula xi / (g - 1)
    # Es de esta forma para que el valor de ri sea un número entre 0 y 1
    return xi / (g - 1)


def calculate_ni(min_value, max_value, ri):
    # Se calcula el valor de ni con la fórmula min_value + (max_value - min_value) * ri
    # El calculo de ni se hace de esta forma para que el valor de ni sea un número entre min_value y max_value
    return min_value + (max_value - min_value) * ri
