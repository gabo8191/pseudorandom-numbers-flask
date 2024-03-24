def make_iteration(xi):
    #Calculamos el cuadrado de xi
    square = xi**2
    #Calculamos la longitud del cuadrado
    extension = len(str(square))

#Por medio de la columna de extensiones, obtenemos el valor de la columna de extracciones
#Se hace un slice de la cadena de texto que representa el cuadrado de xi para obtener la extracción
#Se redondea el valor de la extracción a 4 decimales
    if extension == 8:
        extraction = int(str(square)[2:6])
    elif extension == 7:
        extraction = int(str(square)[1:5])
    elif extension == 6:
        extraction = int(str(square)[0:4])
    elif extension == 5:
        extraction = int(str(square)[0:3])
    elif extension == 4:
        extraction = int(str(square)[0:2])
    elif extension == 3:
        extraction = int(str(square)[0:1])
    else:
        extraction = None

#Regresamos una lista con los valores de las columnas
    if extraction is not None:
        #Se retorna xi, cuadrado, extensión, extracción y ri el cual es la extracción dividida entre 10000
        return [xi, square, extension, extraction, round(extraction * 0.0001, 4)]
    else:
        #En caso de que la extracción sea None, se retorna una lista con los valores de las columnas y 0 en ri
        return [xi, square, extension, 0, 0.0]


def calculate_ni(ri_values, min_value, max_value):
    #Calculamos los valores de ni con la fórmula min_value + (max_value - min_value) * ri
    #Esta formula inidica que se toma el rango de valores entre min_value y max_value y se multiplica por el valor de ri
    ni_values = [round(min_value + (max_value - min_value) * ri, 4) for ri in ri_values]
    return ni_values
