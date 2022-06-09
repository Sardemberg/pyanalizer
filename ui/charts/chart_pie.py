import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class ChartPie:
    def __init__(self, master=None):
        figura = plt.Figure(figsize=(5, 3), dpi=55)
        figura.patch.set_facecolor('#F0F0F0')
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, master)
        canva.get_tk_widget().pack(side="left")
        recipe = ["375 g flour",
                  "75 g sugar",
                  "250 g butter",
                  "300 g berries"]

        data = [float(x.split()[0]) for x in recipe]
        ingredients = [x.split()[-1] for x in recipe]

        def func(pct, allvals):
            absolute = int(np.round(pct/100.*np.sum(allvals)))
            return "{:.1f}%\n({:d} g)".format(pct, absolute)

        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))

        ax.legend(wedges, ingredients,
                  title="Ingredients",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title("Matplotlib bakery: A pie")
