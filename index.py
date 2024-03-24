from flask import Flask, render_template, request
import mean_squares as ms
import linear_congruence as lc
import multiplicative_congruence as mc
import uniform_distribution as ud
import normal_distribution as nd
import distribution as dist

# Variables globales usadas para guardar los valores de las columnas de las tablas de los métodos
ni_values_ms = []
iterations_ms = 0

ni_values_lc = []
iterations_lc = 0

ni_values_mc = []
iterations_mc = 0

ni_values_ud = []
iterations_ud = 0

ni_values_nd = []
iterations_nd = 0

# Inicializamos la aplicación de Flask
app = Flask(__name__)

# Definimos las rutas de la aplicación
#/ es la ruta principal de la aplicación
@app.route("/")
def index():
    return render_template("index.html")

#Mean Squares es la ruta para el método de cuadrados medios
@app.route("/mean_squares")
def mean_squares():
    return render_template("mean_squares.html")

#Linear Congruence es la ruta para el método de congruencia lineal
@app.route("/linear_congruence")
def linear_congruence():
    return render_template("linear_congruence.html")

#Multiplicative Congruence es la ruta para el método de congruencia multiplicativa
@app.route("/multiplicative_congruence")
def multiplicative_congruence():
    return render_template("multiplicative_congruence.html")

#Normal Distribution es la ruta para la distribución normal
@app.route("/normal_distribution")
def normal_distribution():
    return render_template("normal_distribution.html")

#Uniform Distribution es la ruta para la distribución uniforme
@app.route("/uniform_distribution")
def uniform_distribution():
    return render_template("uniform_distribution.html")


# Cuadrados Medios - Calculo
@app.route("/mean_squares_calculate", methods=["POST"])
def mean_squares_calculate():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_ms
    global iterations_ms
    #Recibimos los valores del formulario
    min_value = int(request.form["min-value"])
    max_value = int(request.form["max-value"])
    iterations = int(request.form["iterations"])
    seed = int(request.form["seed"])
    #Inicializamos las variables que vamos a usar
    iterations_ms = iterations
    i_values = []
    xi_values = []
    xi_squared_values = []
    extension_values = []
    extraction_values = []
    ri_values = []
    xi = seed
    #Iteramos para obtener los valores de las columnas
    for i in range(iterations):
        #Make iteration nos regresa una tupla con los valores de las columnas
        xi_result = ms.make_iteration(xi)
        xi_values.append(xi_result[0])
        xi_squared_values.append(xi_result[1])
        extension_values.append(xi_result[2])
        extraction_values.append(xi_result[3])
        ri_values.append(xi_result[4])
        xi = xi_result[3]
        i_values.append(i)
    #Calculamos los valores de ni
    ni_values = ms.calculate_ni(ri_values, min_value, max_value)
    #Guardamos los valores ni en variables globales para poder acceder a ellos desde las funciones de plot
    ni_values_ms = ni_values
    #Regresamos el template con los valores de las columnas
    return render_template(
        "mean_squares.html",
        i_values=i_values,
        xi_values=xi_values,
        xi_squared_values=xi_squared_values,
        extension_values=extension_values,
        extraction_values=extraction_values,
        ri_values=ri_values,
        ni_values=ni_values,
    )

@app.route("/linear_congruence_calculate", methods=["POST"])
def linear_congruence_calculate():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_lc
    global iterations_lc
    #Recibimos los valores del formulario
    min_value = int(request.form["min-value"])
    max_value = int(request.form["max-value"])
    iterations = int(request.form["iteraciones"])
    input_x0 = int(request.form["inputX0"])
    input_k = int(request.form["inputk"])
    input_c = int(request.form["inputc"])
    input_m = int(request.form["inputm"])
    #Calculamos la tabla con los valores de las columnas
    table = lc.calculate_table(
        input_x0, 1 + 2 * input_k, input_c, 2**input_m, iterations, min_value, max_value
    )
    #Guardamos los valores de ni en variables globales para poder acceder a ellos desde las funciones de plot
    ni_values_lc = table[3]
    iterations_lc = iterations
    #Regresamos el template con los valores de las columnas
    return render_template("linear_congruence.html", table=table)

@app.route("/multiplicative_congruence_calculate", methods=["POST"])
def multiplicative_congruence_calculate():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_mc
    global iterations_mc
    #Recibimos los valores del formulario
    x0 = int(request.form["inputX0"])
    t = int(request.form["inputk"])
    g = int(request.form["inputm"])
    iteraciones = int(request.form["iteraciones"])
    min_value = int(request.form["min-value"])
    max_value = int(request.form["max-value"])
    #Calculamos la tabla con los valores de las columnas
    table = mc.calculate_method(x0, 8 * t + 3, 2**g, iteraciones, min_value, max_value)
    #Guardamos los valores ni en variables globales para poder acceder a ellos desde las funciones de plot
    ni_values_mc = table[2]
    iterations_mc = iteraciones
    #Regresamos el template con los valores de las columnas
    return render_template("multiplicative_congruence.html", table=table)

@app.route("/uniform_distribution_calculate", methods=["POST"])
def uniform_distribution_calculate():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_ud
    global iterations_ud
    #Recibimos los valores del formulario
    min_value = int(request.form["min-value"])
    max_value = int(request.form["max-value"])
    iterations = int(request.form["iterations"])
    #Calculamos los valores de ri y ni
    ri_array, ni_array = ud.uniform_distribution(iterations, max_value, min_value)
    #Guardamos los valores ni en variables globales para poder acceder a ellos desde las funciones de plot
    ni_values_ud = ni_array
    iterations_ud = iterations
    #Regresamos el template con los valores de las columnas
    return render_template(
        "uniform_distribution.html",
        ri_values=ri_array,
        ni_values=ni_array,
        #Generamos una lista con los valores de i para poder iterar sobre ella en el template
        i_values=range(1, iterations + 1),
    )

@app.route("/normal_distribution_calculate", methods=["POST"])
def normal_distribution_calculate():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_nd
    global iterations_nd
    #Recibimos los valores del formulario
    mean = float(request.form["mean"])
    std_dev = float(request.form["standard-deviation"])
    iterations = int(request.form["iterations"])
    #Calculamos los valores de ri y ni
    ri_array, ni_array = nd.normal_distribution(std_dev, iterations, mean)
    #Guardamos los valores de ni en variables globales para poder acceder a ellos desde las funciones de plot
    ni_values_nd = ni_array
    iterations_nd = iterations
    #Regresamos el template con los valores de las columnas
    return render_template(
        "normal_distribution.html",
        ri_values=ri_array,
        ni_values=ni_array,
        #Generamos una lista con los valores de i para poder iterar sobre ella en el template
        i_values=range(1, iterations + 1),
    )


@app.route("/plot_mean_squares", methods=["POST"])
def plot_mean_squares():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_ms
    global iterations_ms
    #Si no hay valores de ni, regresamos un mensaje
    if len(ni_values_ms) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    #Calculamos los intervalos y la frecuencia de los valores de ni
    freq_table, freq = dist.calculate_interval(iterations_ms, ni_values_ms)
    #Generamos el plot con los valores de los intervalos y la frecuencia
    html = dist.generate_plot(freq_table, freq)
    #Regresamos el html del plot
    return html


@app.route("/plot_linear_congruence", methods=["POST"])
def plot_linear_congruence():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_lc
    global iterations_lc
    #Si no hay valores de ni, regresamos un mensaje
    if len(ni_values_lc) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    #Calculamos los intervalos y la frecuencia de los valores de ni
    intervals, freq = dist.calculate_interval(iterations_lc, ni_values_lc)
    #Generamos el plot con los valores de los intervalos y la frecuencia
    html = dist.generate_plot(intervals, freq)
    #Regresamos el html del plot
    return html


@app.route("/plot_multiplicative_congruence", methods=["POST"])
def plot_multiplicative_congruence():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_mc
    global iterations_mc
    #Si no hay valores de ni, regresamos un mensaje
    if len(ni_values_mc) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    #Calculamos los intervalos y la frecuencia de los valores de ni
    intervals, freq = dist.calculate_interval(iterations_mc, ni_values_mc)
    #Generamos el plot con los valores de los intervalos y la frecuencia
    html = dist.generate_plot(intervals, freq)
    #Regresamos el html del plot
    return html


@app.route("/plot_uniform_distribution", methods=["POST"])
def plot_uniform_distribution():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_ud
    global iterations_ud
    #Si no hay valores de ni, regresamos un mensaje
    if len(ni_values_ud) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    #Calculamos los intervalos y la frecuencia de los valores de ni
    intervals, freq = dist.calculate_interval(iterations_ud, ni_values_ud)
    #Generamos el plot con los valores de los intervalos y la frecuencia
    html = dist.generate_plot(intervals, freq)
    #Regresamos el html del plot
    return html


@app.route("/plot_normal_distribution", methods=["POST"])
def plot_normal_distribution():
    # Variables globales para poder acceder a ellas desde las funciones de plot
    global ni_values_nd
    global iterations_nd
    #Si no hay valores de ni, regresamos un mensaje
    if len(ni_values_nd) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    #Calculamos los intervalos y la frecuencia de los valores de ni
    intervals, freq = dist.calculate_interval(iterations_nd, ni_values_nd)
    #Generamos el plot con los valores de los intervalos y la frecuencia
    html = dist.generate_plot(intervals, freq)
    #Regresamos el html del plot
    return html

# Inicializamos la aplicación de Flask
if __name__ == "__main__":
    app.run(debug=True)
