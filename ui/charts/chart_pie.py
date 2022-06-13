import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class ChartPie:
    def __init__(self, master=None,  erros=[]):
        # criando a figura
        figura = plt.Figure(figsize=(5, 3), dpi=60)
        figura.patch.set_facecolor('#d9d9d9')
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, master)
        canva.get_tk_widget().pack(side="left")

        # configurações do gráfico
        elementos = []
        for erro in erros:
            elementos.append(f"{erro[1]} {erro[0]}")

        recipe = elementos

        data = [float(x.split()[0]) for x in recipe]
        ingredients = [x.split()[-1] for x in recipe]

        def func(pct, allvals):
            absolute = int(np.round(pct/100.*np.sum(allvals)))
            return "{:.1f}%\n({:d})".format(pct, absolute)

        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))

        ax.legend(wedges, ingredients,
                  title="Problemas",
                  loc="center left",
                  bbox_to_anchor=(-0.5, 0, 0, 1))

        plt.setp(autotexts, size=8, weight="bold",)

        ax.set_title("Gráfico de problemas")
