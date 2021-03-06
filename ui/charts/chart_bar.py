# lib matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# lib pandas
import numpy as np


class ChartBar:

    def __init__(self, master=None, erros=[]):
        # tratando dados
        labelsChartBar = []
        valuesChartBar = []
        for erro in erros:
            labelsChartBar.append(erro[0])
            valuesChartBar.append(erro[1])

        # criando a figura
        figura = plt.Figure(figsize=(15, 4), dpi=60,)
        figura.patch.set_facecolor('#d9d9d9')
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, master,)
        canva.get_tk_widget().pack(side="left")
        np.random.seed(19680801)

        # configurações do gráfico
        city = labelsChartBar
        y_pos = np.arange(len(city))
        performance = valuesChartBar
        ax.barh(y_pos, performance, align='center',)
        ax.set_yticks(y_pos, labels=city, )
        ax.invert_yaxis()
        ax.set_xlabel('Quantidade')
        ax.set_title('Gráficos de problemas por cidades')
