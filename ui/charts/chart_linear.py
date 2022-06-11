import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class ChartLinear:
    def __init__(self, master=None, problemas=[]):
        # criando a figura
        figura = plt.Figure(figsize=(6, 4), dpi=55,)
        figura.patch.set_facecolor('#F0F0F0')
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, master,)

        canva.get_tk_widget().pack(side="left")
        np.random.seed(19680801)

        # configurações do gráfico

        values = np.linspace(1, 10, 10)
        x = np.linspace(1, 7, 10)
        ax.plot(x, values, label='Problemas')
        ax.set_xlabel('Dia da semana')
        ax.set_ylabel('Quantidade')
        ax.set_title("Gráfico de eficiência")
        ax.legend()
