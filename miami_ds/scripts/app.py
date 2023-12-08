import io
from flask import Response, Flask, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
app = Flask(__name__)

@app.route('/')
def plot_png():
    zs = np.random.rand(100)
    
    fig = Figure()
    output = io.BytesIO()
    axis = fig.add_subplot(1, 1, 1)
    xs = np.random.rand(100)
    ys = np.random.rand(100)
    axis.plot(xs, ys)
    FigureCanvas(fig).print_png(output)
    #I want to save the the figure
    with open('static/images/image.png', 'wb') as file:
        file.write(output.getvalue())

    return render_template('index.html', r=Response(output.getvalue(), content_type='image/png'))

app.run(debug=True, port=5000, use_reloader=False)