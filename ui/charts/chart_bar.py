# lib matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# lib pandas
import numpy as np


class ChartBar:

    def __init__(self, master=None, values=[], labels=[]):

        # criando a figura
        figura = plt.Figure(figsize=(11, 4), dpi=57,)
        figura.patch.set_facecolor('#F0F0F0')
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, master,)
        canva.get_tk_widget().pack(side="left")
        np.random.seed(19680801)

        # configurações do gráfico
        city = labels
        y_pos = np.arange(len(city))
        performance = values
        ax.barh(y_pos, performance, align='center',)
        ax.set_yticks(y_pos, labels=city, )
        ax.invert_yaxis()
        ax.set_xlabel('Quantidade')
        ax.set_title('Gráficos de problemas por cidades')
