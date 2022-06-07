# lib matplotlib

import matplotlib.pyplot as plt
# lib pandas
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ChartBar:
    def __init__(self):
        print("")

    def showChart(self, master=None,):
        figura = plt.Figure(figsize=(4, 3), dpi=60)
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, master)

        canva.get_tk_widget().pack(side="bottom")
        np.random.seed(19680801)

        # Example data
        people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        y_pos = np.arange(len(people))
        performance = 3 + 10 * np.random.rand(len(people))
        error = np.random.rand(len(people))

        ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos, labels=people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Performance')
        ax.set_title('How fast do you want to go today?')
