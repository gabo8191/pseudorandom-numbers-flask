from flask import Flask, render_template, request, jsonify, send_file
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import mpld3
import numpy as np
import mean_squares as ms
import linear_congruence as lc
import multiplicative_congruence as mc
import uniform_distribution as ud
import normal_distribution as nd
import distribution as dist

ri_values_ms = []
ni_values_ms = []
iterations_ms = 0

ri_values_lc = []
ni_values_lc = []
iterations_lc = 0

ri_values_mc = []
ni_values_mc = []
iterations_mc = 0

ri_values_ud = []
ni_values_ud = []
iterations_ud = 0

ri_values_nd = []
ni_values_nd = []
iterations_nd = 0

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mean_squares")
def mean_squares():
    return render_template("mean_squares.html")


@app.route("/linear_congruence")
def linear_congruence():
    return render_template("linear_congruence.html")


@app.route("/multiplicative_congruence")
def multiplicative_congruence():
    return render_template("multiplicative_congruence.html")


@app.route("/normal_distribution")
def normal_distribution():
    return render_template("normal_distribution.html")


@app.route("/uniform_distribution")
def uniform_distribution():
    return render_template("uniform_distribution.html")


@app.route("/mean_squares_calculate", methods=["POST"])
def mean_squares_calculate():
    global ri_values_ms
    global ni_values_ms
    global iterations_ms
    min_value = int(request.form["min-value"])
    max_value = int(request.form["max-value"])
    iterations = int(request.form["iterations"])
    seed = int(request.form["seed"])

    iterations_ms = iterations
    i_values = []
    xi_values = []
    xi_squared_values = []
    extension_values = []
    extraction_values = []
    ri_values = []
    xi = seed

    for i in range(iterations):
        xi_result = ms.make_iteration(xi)
        xi_values.append(xi_result[0])
        xi_squared_values.append(xi_result[1])
        extension_values.append(xi_result[2])
        extraction_values.append(xi_result[3])
        ri_values.append(xi_result[4])
        xi = xi_result[3]
        i_values.append(i)
    ni_values = ms.calculate_ni(ri_values, min_value, max_value)
    ri_values_ms = ri_values
    ni_values_ms = ni_values
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
    global ri_values_lc
    global ni_values_lc
    global iterations_lc
    min_value = int(request.form["min-value"])
    max_value = int(request.form["max-value"])
    iterations = int(request.form["iteraciones"])
    input_x0 = int(request.form["inputX0"])
    input_k = int(request.form["inputk"])
    input_c = int(request.form["inputc"])
    input_m = int(request.form["inputm"])
    table = lc.calculate_table(
        input_x0, 1 + 2 * input_k, input_c, 2**input_m, iterations, min_value, max_value
    )
    ri_values_lc = table[2]
    ni_values_lc = table[3]
    iterations_lc = iterations
    return render_template("linear_congruence.html", table=table)


@app.route("/multiplicative_congruence_calculate", methods=["POST"])
def multiplicative_congruence_calculate():
    global ri_values_mc
    global ni_values_mc
    global iterations_mc
    x0 = int(request.form["inputX0"])
    t = int(request.form["inputk"])
    g = int(request.form["inputm"])
    iteraciones = int(request.form["iteraciones"])
    min_value = int(request.form["min-value"])
    max_value = int(request.form["max-value"])
    table = mc.calculate_method(x0, 8 * t + 3, 2**g, iteraciones, min_value, max_value)
    ri_values_mc = table[1]
    ni_values_mc = table[2]
    iterations_mc = iteraciones
    return render_template("multiplicative_congruence.html", table=table)


@app.route("/uniform_distribution_calculate", methods=["POST"])
def uniform_distribution_calculate():
    global ri_values_ud
    global ni_values_ud
    global iterations_ud
    min_value = int(request.form["min-value"])
    max_value = int(request.form["max-value"])
    iterations = int(request.form["iterations"])
    ri_array, ni_array = ud.uniform_distribution(iterations, max_value, min_value)
    ri_values_ud = ri_array
    ni_values_ud = ni_array
    iterations_ud = iterations
    return render_template(
        "uniform_distribution.html",
        ri_values=ri_array,
        ni_values=ni_array,
        i_values=range(1, iterations + 1),
    )


@app.route("/normal_distribution_calculate", methods=["POST"])
def normal_distribution_calculate():
    global ri_values_nd
    global ni_values_nd
    global iterations_nd
    mean = float(request.form["mean"])
    std_dev = float(request.form["standard-deviation"])
    iterations = int(request.form["iterations"])
    ri_array, ni_array = nd.normal_distribution(std_dev, iterations, mean)
    ri_values_nd = ri_array
    ni_values_nd = ni_array
    iterations_nd = iterations
    return render_template(
        "normal_distribution.html",
        ri_values=ri_array,
        ni_values=ni_array,
        i_values=range(1, iterations + 1),
    )


@app.route("/plot_mean_squares", methods=["POST"])
def plot_mean_squares():
    global ni_values_ms
    global iterations_ms
    if len(ni_values_ms) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    freq_table, freq = dist.calculate_interval(iterations_ms, ni_values_ms)
    html = dist.generate_plot(freq_table, freq)
    return html


@app.route("/plot_linear_congruence", methods=["POST"])
def plot_linear_congruence():
    global ni_values_lc
    global iterations_lc
    if len(ni_values_lc) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    intervals, freq = dist.calculate_interval(iterations_lc, ni_values_lc)
    html = dist.generate_plot(intervals, freq)
    return html


@app.route("/plot_multiplicative_congruence", methods=["POST"])
def plot_multiplicative_congruence():
    global ni_values_mc
    global iterations_mc
    if len(ni_values_mc) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    intervals, freq = dist.calculate_interval(iterations_mc, ni_values_mc)
    html = dist.generate_plot(intervals, freq)
    return html


@app.route("/plot_uniform_distribution", methods=["POST"])
def plot_uniform_distribution():
    global ni_values_ud
    global iterations_ud
    if len(ni_values_ud) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    intervals, freq = dist.calculate_interval(iterations_ud, ni_values_ud)
    html = dist.generate_plot(intervals, freq)
    return html


@app.route("/plot_normal_distribution", methods=["POST"])
def plot_normal_distribution():
    global ni_values_nd
    global iterations_nd
    if len(ni_values_nd) == 0:
        return "Vuelva a presionar el botón de calcular, por favor :)"
    intervals, freq = dist.calculate_interval(iterations_nd, ni_values_nd)
    html = dist.generate_plot(intervals, freq)
    return html


if __name__ == "__main__":
    app.run(debug=True)
