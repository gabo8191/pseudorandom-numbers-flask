def calculate_table(x0, a, c, m, iteraciones, min_value, max_value):
    # Se crea una lista vacía para almacenar los valores de la tabla
    table = []
    xi = x0
    Ni_array = []

    # Se crea un ciclo para calcular los valores de las columnas
    for i in range(iteraciones):
        xi = calculate_xi(xi, a, c, m)
        ri = calculate_ri(xi, m)
        ni = calculate_ni(min_value, max_value, ri)
        #Se agrega el valor de ni a la lista de valores de ni
        Ni_array.append(ni)
        #Se agrega una lista con los valores de las columnas a la tabla
        table.append([i + 1, xi, ri, ni])

    return table

def calculate_xi(xi, a, c, m):
    #Se calcula el valor de xi con la fórmula (a * xi + c) % m
    #se hace asi para evitar que el valor de xi sea mayor a m
    return (a * xi + c) % m
def calculate_ri(xi, m):
    #Se calcula el valor de ri con la fórmula xi / (m - 1)
    #Es de esta forma para que el valor de ri sea un número entre 0 y 1
    return xi / (m - 1)

def calculate_ni(min_value, max_value, ri):
    #Se calcula el valor de ni con la fórmula min_value + (max_value - min_value) * ri
    #El calculo de ni se hace de esta forma para que el valor de ni sea un número entre min_value y max_value
    return min_value + (max_value - min_value) * ri




