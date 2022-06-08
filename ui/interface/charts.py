from tkinter import *

from ui.charts.chart_bar import ChartBar
from ui.charts.chart_pie import ChartPie


class Charts:

    def __init__(self, master=None):

        self.firstContainer = Frame(master,)

        self.firstContainer.place(x=10, y=20)

        self.secondContainer = Frame(master, height=10, bg="red", width=500)
        self.secondContainer["pady"] = 20
        self.secondContainer.place(y=240)

        self.thirdContainer = Frame(master)

        self.thirdContainer.place(x=195, y=280)

        ChartBar(self.firstContainer)

        ChartPie(self.thirdContainer)
