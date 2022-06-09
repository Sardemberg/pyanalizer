from tkinter import *

from ui.charts.chart_bar import ChartBar
from ui.charts.chart_linear import ChartLinear
from ui.charts.chart_pie import ChartPie


class Charts:

    def __init__(self, master=None):

        self.cardFirst = Frame(master, borderwidth=1, relief="raised")
        self.cardFirst.place(x=20, y=20,  width=310, height=240,)

        self.cardSecond = Frame(master, borderwidth=1, relief="raised")
        self.cardSecond.place(x=350, y=20,  width=340, height=240,),

        self.cardThird = Frame(master, borderwidth=1, relief="raised")
        self.cardThird.place(x=20, y=280,  width=670, height=250,)

        self.firstContainer = Frame(self.cardFirst,)
        self.firstContainer.place(x=0, y=30,)
        ChartPie(self.firstContainer)

        self.secondContainer = Frame(self.cardSecond)
        self.secondContainer.place(x=0, y=0,)
        ChartLinear(self.secondContainer)

        self.thirdContainer = Frame(self.cardThird)
        self.thirdContainer.place(x=40, y=0,)
        ChartBar(self.thirdContainer)
