import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class ChartLinear:
    def __init__(self, master=None):
        # criando a figura
        figura = plt.Figure(figsize=(6, 4), dpi=55,)
        figura.patch.set_facecolor('#F0F0F0')
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, master,)

        canva.get_tk_widget().pack(side="left")
        np.random.seed(19680801)

        # configurações do gráfico
        x = np.linspace(0, 2, 100)  # Sample data.
        ax.plot(x, x, label='Resolvidos')  # Plot some data on the axes.
        ax.plot(x, x**2, label='Pendentes')  # Plot more data on the axes...
        # ... and some more.
        ax.set_xlabel('Periodo')  # Add an x-label to the axes.
        ax.set_ylabel('Quantidade')  # Add a y-label to the axes.
        ax.set_title("Gráfico de eficiência")  # Add a title to the axes.
        ax.legend()
