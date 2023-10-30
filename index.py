import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from ipywidgets import interact
from flask import Flask
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
app = Flask(__name__)

@app.route('/')
def plot_png():
    zs = np.random.rand(100)
    xs = np.random.rand(100)
    @interact
    def f(x = ["xs", "zs"]):
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)

        ys = np.random.rand(100)
        axis.plot(x, ys)
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')

app.run(debug=True, port=5000, use_reloader=False)