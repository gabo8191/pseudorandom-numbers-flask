def make_iteration(xi):
    square = xi**2
    extension = len(str(square))
    extaction = None

    if extension == 8:
        extaction = int(str(square)[2:6])
    elif extension == 7 or extension == 6:
        extaction = int(str(square)[1:5])
    elif extension == 5 or extension == 4:
        extaction = int(str(square)[0:4])

    if extaction is not None:
        return [xi, square, extension, extaction, round(extaction * 0.0001, 4)]
    else:
        return [xi, square, extension, 0, 0.0]


def calculate_ni(ri_values, min_value, max_value):
    ni_values = [round(min_value + (max_value - min_value) * ri, 4) for ri in ri_values]
    return ni_values
